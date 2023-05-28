from django.db import models
from address.models import Address
from campus.models import Campus
from department.models import Department

# Create your models here.


class Students(models.Model):
    class Meta:
        db_table = 'student'

    name = models.CharField(max_length=20,null=False)
    address = models.ForeignKey(Address, related_name='student', on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus,related_name='student',on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department')

    def __str__(self):
        return f"{self.name}"