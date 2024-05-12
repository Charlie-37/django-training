from django.db import models

# Create your models here.
class fruits(models.Model):
    fruit_name = models.CharField(max_length=100, null=True)
    price = models.IntegerField()
    manufacture_date = models.DateField()
    fruit_descriptions = models.TextField(null=True, blank=True)
    is_fresh = models.BooleanField(default=True)
    
    def __str__(self):
        return self.fruit_name
    
    class Meta:
        db_table = 'home_fruits'
        verbose_name = 'home_fruits'
        ordering = ['-fruit_name']
        constraints = [models.UniqueConstraint(fields=("fruit_name","fruit_descriptions"), name="unique_fruit_desc")]
        
        
class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

class car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)
    
    def __str__(self):
        return self.car_name
    
