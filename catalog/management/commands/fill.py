from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Крупы', 'desc': 'зерно'},
            {'name': 'Сладости', 'desc': 'конфеты и шоколад'},
            {'name': 'Напитки', 'desc': 'Газировка, сок, энергетик'},
            {'name': 'Табак', 'desc': 'Сигареты'}
        ]

        cat_for_create = []
        for cat_item in category_list:
            cat_for_create.append(
                Category(**cat_item)
            )

        Category.objects.bulk_create(cat_for_create)