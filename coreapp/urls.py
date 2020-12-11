from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('pizzas/', views.PizzaList.as_view()),
    path('pizzas/<int:pk>/', views.PizzaDetail.as_view()),
    path('pizzas/regular/', views.CreateRegularPizza.as_view()),
    path('pizzas/square/', views.CreateSquarePizza.as_view()),

]