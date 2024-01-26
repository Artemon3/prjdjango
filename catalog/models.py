from django.db import models

from users.models import User

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
    category = models.ForeignKey(Category, **NULLABLE, on_delete=models.SET_NULL)
    price_one = models.IntegerField(verbose_name='цена за 1шт.', **NULLABLE)
    date_creation = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    date_lastmod = models.DateTimeField(verbose_name='дата изменения', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)
    is_published = models.BooleanField(verbose_name='опубликован', default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'



class Version(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    version_number = models.IntegerField(default=0, verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    is_active_version = models.BooleanField(default=True, verbose_name="статус версии")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'