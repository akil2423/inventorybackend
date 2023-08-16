from django.db import models

# Create your models here.

class Product(models.Model):
  product_id = models.AutoField(primary_key = True)
  product_name= models.CharField(max_length=200)

  def __str__(self):
    return self.product_id
 

  
class Location(models.Model):
  location_id = models.AutoField(primary_key = True)
  location_name = models.CharField(max_length=200)

  def __str__(self):
    return str(self.location_id)
 
  
class ProductMovement(models.Model):
  productmovement_id = models.AutoField(primary_key = True)
  timestamp = models.DateTimeField()
  from_location = models.CharField(max_length=200)
  to_location = models.CharField(max_length=200)
  product_id = models.ForeignKey(Product, blank=True, null= True, on_delete=models.CASCADE)
  Location_id = models.ForeignKey(Location, blank=True, null= True,  on_delete=models.CASCADE)
  quantity = models.IntegerField()
 
   
  def __str__(self):
    return str(self.productmovement_id)