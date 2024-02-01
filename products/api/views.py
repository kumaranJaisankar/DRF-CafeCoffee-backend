from rest_framework import generics 
from products.models import CoffeeProducts
from .serializers import ProductSerializer



class CoffeeListView(generics.ListCreateAPIView):
    queryset = CoffeeProducts.objects.all()
    serializer_class = ProductSerializer
    
