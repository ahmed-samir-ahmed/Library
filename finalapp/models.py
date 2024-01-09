from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name
class Book(models.Model):

    status_book = [

        ('available','available'),
        ('rental','rental'),
        ('solid','solid'),

    ]

    title = models.CharField(max_length=300)
    auther = models.CharField(max_length=300,null=True,blank=True)
    photo_book = models.ImageField(upload_to='photos',null=True,blank=True)
    photo_auther = models.ImageField(upload_to='photos', null=True, blank=True)
    pages = models.IntegerField(null=True,blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    retal_price_day = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    retal_period = models.IntegerField(null=True,blank=True)
    total_rental = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50,choices=status_book)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.title
