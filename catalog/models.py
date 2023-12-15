from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='название категории', default='SOME STRING')
    desc = models.TextField(verbose_name='описание категории', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.desc}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    desc = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products', verbose_name='аватар', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price_one = models.IntegerField(verbose_name='цена за 1шт.')
    date_creation = models.DateTimeField(verbose_name='дата создания')
    date_lastmod = models.DateTimeField(verbose_name='дата изменения')

    def __str__(self):
        return f'{self.name} {self.desc} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


