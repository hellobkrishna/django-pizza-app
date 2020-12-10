from django.contrib import admin

# Register your models here.
from .models import Pizza, Type, Size, Topping

admin.site.register(Pizza)
admin.site.register(Type)
admin.site.register(Size)
admin.site.register(Topping)