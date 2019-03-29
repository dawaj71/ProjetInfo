from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=500, blank=True, default='')
    img64 = models.TextField()

    class Meta:
        ordering = ['name']

class Result(models.Model):
    score1 = models.CharField(max_length=500, blank=False, default='')
    score2 = models.CharField(max_length=500, blank=False, default='')
    score3 = models.CharField(max_length=500, blank=False, default='')

    img1b64 = models.TextField()
    img2b64 = models.TextField()
    img3b64 = models.TextField()

    class Meta:
        ordering = ['id']