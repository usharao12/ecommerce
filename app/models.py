from django.db import models


class Product(models.Model):
    name=models.CharField(max_length=25,blank=False)
    number=models.IntegerField()
    cost=models.IntegerField()
    def __str__(self):
        return self.name