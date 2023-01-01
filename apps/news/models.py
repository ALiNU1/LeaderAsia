from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.IntegerField()
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        