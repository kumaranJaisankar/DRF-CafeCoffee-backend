from django.db import models
from django.utils.text import slugify
import uuid
# Create your models here.

class CoffeeCategory(models.Model):
    category_name = models.CharField(max_length=50)
    slug =models.SlugField(max_length=200,blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.category_name)
        super(CoffeeCategory,self).save(*args,**kwargs)

    def __str__(self) -> str:
        return self.category_name



class CoffeeProducts(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.ForeignKey(CoffeeCategory,related_name='names', on_delete=models.CASCADE)
    type = models.CharField( max_length=50,blank = True)
    description =models.TextField()
    rosted = models.CharField( max_length=50)
    ingredients = models.CharField(max_length=50)
    special_ingredient = models.CharField(max_length=100)
    average_rating = models.DecimalField(max_digits=5, decimal_places=1)
    rating_counts = models.IntegerField()
    imagelink_square=models.ImageField(upload_to="cafeCoffee")
    imagelink_portrait=models.ImageField(upload_to="cafeCoffee")

    def __str__(self) -> str:
        return f"{self.name.category_name} - {self.type}"
     
class ProductPrice(models.Model):
    product = models.ForeignKey(CoffeeProducts, related_name="prices",on_delete=models.CASCADE)
    size= models.CharField(max_length=50)
    price = models.IntegerField()
    currency = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.product.name.category_name} - {self.size} - {self.price}"
    
