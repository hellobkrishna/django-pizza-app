from django.db import models

# Create your models here.

class Size(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=200)
    pizza = models.ManyToManyField(Pizza)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
