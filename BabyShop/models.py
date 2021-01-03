from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название книги')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Автор')
    page = models.IntegerField(verbose_name='Количество страниц')
    wtitten = models.IntegerField(verbose_name='Написана')
    img = models.ImageField(upload_to="Products/")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

class Author(models.Model):
    fullname = models.CharField(max_length=50, verbose_name='Имя и фамилия автора')

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'