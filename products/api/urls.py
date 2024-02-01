from django.urls import path 
from .views import CoffeeListView


urlpatterns = [
    path('coffee/',CoffeeListView.as_view(),name="coffee list")
]
