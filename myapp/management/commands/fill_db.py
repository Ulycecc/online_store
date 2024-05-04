import datetime
from random import choices
from django.core.management.base import BaseCommand
from myapp.models import Сonsumer, Product, Order
import random
import decimal


class Command(BaseCommand):
    help = "Generate fake date."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Сonsumer ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, 101):
            product = Product(name=f'Product_{i}', price=decimal.Decimal(
                random.randrange(10000))/100, quantity=random.randint(0, 99999), description=f'description_{i}')
            product.save()
        for i in range(1, count + 1):
            consumer = Сonsumer(name=f'Сonsumer_{i}', email=f'mail{i}@mail.ru')
            consumer.save()
            for j in range(1, random.randint(1, 50)):
                start = datetime.datetime(2023, 1, 1)
                end = datetime.datetime.today()
                random_date = start + \
                    datetime.timedelta(seconds=random.randint(
                        0, int((end - start).total_seconds())))
                for pk in range(1, 11):
                    order = Order(date=random_date, consumer=consumer,
                                  product=random.choice(Product.objects.all()), amount=10)
                    order.save()
