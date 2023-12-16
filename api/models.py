from django.db import models

# Create your models here.

class Location(models.Model):
    locationName = models.CharField(max_length=50, primary_key = True)
    
    def __str__(self):
        return self.locationName
    
class Item(models.Model):
    itemName = models.CharField(max_length=50)
    dateAdded = models.DateField(auto_now_add=True)
    
    # add location name as foreign key to item
    itemLocation = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.itemName
    
class Order(models.Model):
    orderName = models.CharField(max_length=50)
    dateAdded = models.DateField(auto_now_add=True)

    
