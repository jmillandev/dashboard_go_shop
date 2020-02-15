from django.core.management.base import BaseCommand, CommandError

from store.products.models import Product
from store.products.views import filter_bad_products 
from store.store import Store
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import logging

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

class Command(BaseCommand):
    help = 'Publica nuevos producto en las cuenta de mercado libre'

    def handle(self, *args, **options):
        logging.info('Aplicando filtro de malas palabras a productos')
        filter_bad_products()

        start = datetime.now()
        logging.info('Consultando la base de datos')
        products = Product.objects.filter(
            sku=None,
            quantity__gt=0,
            available=True,
            category__leaf=True).select_related('category')
        logging.info(f'Fin de la consulta, tiempo de ejecucion {datetime.now()-start}')

        store = Store()
        slices = 100
        for lap, _products in enumerate(chunks(products, slices)):
            logging.info(f'PUBLICANDO {(lap)*100}-{(lap+1)*100}')
            with ThreadPoolExecutor(max_workers=8) as executor:
                response = executor.map(store.publish, _products)
                limit_per_day = False
                for product in response:
                    if not response['ok']:
                        limit_per_day = (response['data'].get('message') ==  'daily_quota.reached')
                    if limit_per_day:
                        break
                if limit_per_day:
                        break