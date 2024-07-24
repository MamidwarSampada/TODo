from django.db import models

# Create your models here.
class Breed(models.Model):
    name=models.CharField(max_length=50)
    size=models.CharField(max_length=50,choices=[('Tiny','Tiny'),('Small','Small'),('Medium','Medium'), ('Large','Large')])
    friendliness=models.IntegerField(choices=[(i,str(i)) for i in range(1,6)]) 
    trainability=models.IntegerField(choices=[(i,str(i)) for i in range(1,6)]) 
    sheddingamount=models.IntegerField(choices=[(i,str(i)) for i in range(1,6)]) 
    exerciseneeds=models.IntegerField(choices=[(i,str(i)) for i in range(1,6)]) 
   
    def __str__(self):
       return self.name
    
class Dog(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    breed=models.ForeignKey(Breed,on_delete=models.PROTECT,related_name='dogs')
    gender=models.CharField(max_length=6)
    color=models.CharField(max_length=15)
    favoritefood=models.CharField(max_length=30)
    favoritetoy=models.CharField(max_length=50)
    
    
