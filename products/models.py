from django.db import models

from categories.models import Category

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products", blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)
