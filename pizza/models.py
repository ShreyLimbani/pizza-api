from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Shape(models.Model):
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 60)

    def __str__(self):
        return f"{self.name} - {self.description}"


class Size(models.Model):
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 60)

    def __str__(self):
        return f"{self.name} - {self.description}"


class Topping(models.Model):
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 60)

    def __str__(self):
        return f"{self.name} - {self.description}"


class Pizza(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name} - {self.description}"


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping, blank=True, null=True)