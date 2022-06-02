from django.db import models


class Entity(models.Model):
    name = models.CharField(max_length=0x50)
    code = models.CharField(max_length=0x50, unique=True)
    developmentMode = models.BooleanField()
    supportEmail = models.EmailField()
    noReplyEmail = models.EmailField()
    developerEmail = models.EmailField()
    timezone = models.CharField(max_length=0x10)
