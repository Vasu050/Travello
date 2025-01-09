from django.db import models

# Create your models here.
class Destination(models.Model): #models.Model is only for database not without it 
 # it is valid when not using databse or postgres
 ''' id:int        # created automatically in database so no need to specify explicitly
    name:str
    image:str
    desc:str
    price:int
    offer:bool'''
 name=models.CharField(max_length=100)
 img=models.ImageField(upload_to='pics')   # when want to wokk with images openig.saving etc in python project we use pillow library 
 desc=models.TextField()
 price=models.IntegerField()
 offer=models.BooleanField(default=False)
