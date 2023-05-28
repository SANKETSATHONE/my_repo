from django.db import models

# Create your models here.

class Address(models.Model):
    class Meta:
        db_table = 'address'
        verbose_name = 'address'
        verbose_name_plural = 'addresses'


    city = models.CharField(max_length=20, verbose_name='city', unique=True, null=False, blank=False)
    state = models.CharField(max_length=30, verbose_name='state', blank=True, null=False)

    def __str__(self):
        return f'{self.city}'
