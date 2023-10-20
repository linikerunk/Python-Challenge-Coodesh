from django.db import models
from models.base import Base
# from django.core.validators import MaxValueValidator, MinValueValidator


class Products(Base):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    @property
    def _number_total_products(self):
        return '0'

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Product"
