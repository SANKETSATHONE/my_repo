from django.db import models
from address.models import Address

# Create your models here.

class Campus(models.Model):
    class Meta:
        db_table = 'campus'
        verbose_name = 'campus'
        verbose_name_plural = 'campuses'

    name = models.CharField(max_length=20, verbose_name='name', null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

