from django.db import models
from address.models import Address
from department.models import Department
from campus.models import Campus
from student.models import Students
# Create your models here.


class Professor(models.Model):
    class Meta:
        db_table = 'professor'

    name = models.CharField(max_length=20, null=False, blank=False)
    subject = models.CharField(max_length=30, null=False, blank=False)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='professor', on_delete=models.CASCADE)
    campus = models.OneToOneField(Campus, on_delete=models.CASCADE)
    students = models.ManyToManyField(Students, related_name='professor')

    def __str__(self):
        return f'{self.name}'
