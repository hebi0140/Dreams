from django.db import models
import PIL
from PIL import Image


# Create your models here.

class Dreams(models.Model):
    title = models.CharField('Исполнитель', max_length=150)
    content = models.TextField('Информация', blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def thumbnail(filename, size=(50, 50), output_filename=None):
        image = Image.open(filename)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(output_filename, image.format)
        return output_filename
