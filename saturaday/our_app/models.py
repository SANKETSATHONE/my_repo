from django.db import models

# Create your models here.
class our_model(models.Model):

    name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    pin = models.IntegerField()