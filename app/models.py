from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=3)
    price = models.IntegerField()
    image = models.ImageField(upload_to="img",blank=True,null=True)
def __str__(self):
    return self.name
