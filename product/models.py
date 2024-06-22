from django.db import models
from django.contrib.auth.models import User


class category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name





class Product(models.Model):
    name = models.CharField(max_length=15)
    pic = models.ImageField(upload_to='Prod_pic/', null=True, blank=True)
    description = models.TextField()
    price = models.FloatField()
    stock = models.PositiveIntegerField()
    discount_price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.user)

    def total_price(self):
        return self.quantity * self.product.price