from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to="images", blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return self.name
