from django.db import models
from enum import Enum


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.TextField(verbose_name="status", max_length=20, default=None)
    phone = models.TextField(verbose_name="phone")
    address = models.TextField(verbose_name="address")
    pizza = models.TextField(verbose_name="pizza")


class OrderStatus(Enum):
    cooking = "cooking"
    onTheWay = "on the way"
    delivered = "delivered"
