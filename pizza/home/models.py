from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4,editable=False, primary_key=True) 
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class pizza_category(BaseModel):
    category_name = models.CharField(max_length=100)

class pizza(BaseModel):
    category = models.ForeignKey(pizza_category,on_delete=models.CASCADE, related_name="pizzas")
    pizza_name = models.CharField(max_length=100)
    price = models.ImageField(default=100)
    images = models.ImageField(upload_to='pizza')
    
class cart(BaseModel):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='carts')
    is_paid = models.BooleanField(default=False)
    
class cart_items(BaseModel):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE, name='cart_items')
    pizza = models.ForeignKey(pizza,on_delete=models.CASCADE)