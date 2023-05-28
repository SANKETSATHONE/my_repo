from django.db import models

# Create your models here.


class Books(models.Model):

    name = models.CharField(max_length=20, verbose_name='book name', null=False, blank=False)
    subject = models.CharField(max_length=20, verbose_name='subject name', null=True)
    price = models.FloatField(verbose_name='book price')
    qty = models.IntegerField(verbose_name='book quantity', null=False, default=1)
    purchase_date = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'library_books'
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __str__(self):
        return f'{self.name} -> {self.price} '

    def __repr__(self):
        return f'{str(self)}'


