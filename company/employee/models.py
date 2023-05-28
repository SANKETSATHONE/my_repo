from django.db import models

# Create your models here.
class Employee(models.Model):

    name = models.CharField(max_length=20, null=False, blank=False, verbose_name='name')
    age = models.IntegerField()
    address = models.CharField(max_length=50, null=False, verbose_name='address')
    department = models.CharField(max_length=20, null=False)

    def __str__(self):
        return f'{self.name} -> {self.address}'

    def __repr__(self):
        return f'{str(self)}'

