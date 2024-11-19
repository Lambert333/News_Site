from distutils.log import fatal

from django.db import models

# class File(models.Model):
#     title = models.CharField("Название файла",max_length=100,null=True,blank=True)
#     file = models.FileField("Загрузить файл",upload_to="files/", blank= False)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name_plural = 'Файлы'
#         verbose_name = 'Файл'
#

class Image(models.Model):
    title = models.CharField("Название", max_length=150,blank= True, null=True)
    image = models.FileField("Загрузить файл", upload_to='files/', blank= False, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Файлы'
        verbose_name = 'Файл'
class News(models.Model):
    # id = models.IntegerField(primary_key=True)
    date = models.DateTimeField("Дата")
    author = models.CharField("Автор", max_length=50)
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Содержание", max_length=2000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'