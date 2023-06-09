from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(blank=True, null=True)
    created_date = models.DateField(auto_now=True)
    modified_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.CharField(max_length=256)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
