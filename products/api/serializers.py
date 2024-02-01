from rest_framework import serializers 
from products.models import CoffeeProducts,ProductPrice,CoffeeCategory

class PriceSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ['size','price','currency']

class CoffeeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeCategory
        fields = ['category_name']

class ProductSerializer(serializers.ModelSerializer):
    prices = PriceSerializers(many=True,read_only=True)
    name = serializers.SerializerMethodField()
    class Meta:
        model = CoffeeProducts 
        fields = ['id','prices','name','description','rosted','special_ingredient','ingredients','average_rating','rating_counts','imagelink_square','imagelink_portrait']

    def get_name(self,obj):
      
        return CoffeeCategory.objects.get(id= obj.name.id).category_name