from django.db import models
from campus.models import Campus
# Create your models here.

IF = 'information technology'
CE = 'computer engineering'
CIVIL = 'civil engineering'
MECH = 'mechanical engineering'

dept_code = ((IF, 'information technology'), (CE, 'computer engineering'), (CIVIL, 'civil engineering'),
             (MECH, 'mechanical engineering'))


class Department(models.Model):
    class Meta:
        db_table = 'department'
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    name = models.CharField(max_length=50, unique=True, null=False)
    code = models.CharField(max_length=200, choices=dept_code)
    campus = models.ForeignKey(Campus, related_name='department', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'