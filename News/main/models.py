from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


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