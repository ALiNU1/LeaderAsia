from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='logo/')
    address = models.CharField(max_length=150)
    nomer = models.CharField(max_length=100)
    email = models.EmailField(blank=True,null=True)
    twitter_link = models.URLField(blank=True,null=True)
    facebook_link = models.URLField(blank=True,null=True)
    linkedin_link = models.URLField(blank=True,null=True)
    instagram_link = models.URLField(blank=True,null=True)
    youtube_link = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'