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

class Topping(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=200)
    topping = models.ManyToManyField(Topping)
    size = models.ForeignKey(Size, related_name='pizzas', on_delete=models.CASCADE)
    type = models.ForeignKey(Type, related_name='pizzas', on_delete=models.CASCADE)


    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
