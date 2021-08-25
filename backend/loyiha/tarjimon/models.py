from django.db import models
class Lugat(models.Model):

    inglizcha = models.CharField('Inglizcha',max_length= 128)
    ozbekcha = models.CharField('O`zbekcha',max_length= 128)
# Create your models here.
