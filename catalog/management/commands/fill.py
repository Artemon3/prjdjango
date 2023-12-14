from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name_cat': 'Крупы', 'desc_cat': 'зерно'},
            {'name_cat': 'Сладости', 'desc_cat': 'конфеты и шоколад'},
            {'name_cat': 'Напитки', 'desc_cat': 'Газировка, сок, энергетик'},
            {'name_cat': 'Табак', 'desc_cat': 'Сигареты'}
        ]

        cat_for_create = []
        for cat_item in category_list:
            cat_for_create.append(
                Category(**cat_item)
            )

        Category.objects.bulk_create(cat_for_create)