from django.db import models

# Create your models here.

class School(models.Model):
    sname=models.CharField(max_length=100, primary_key=True)
    slocation=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)

    def __str__(self):
        return self.sname
    
class college(models.Model):
    sname=models.ForeignKey(School,on_delete=models.CASCADE)
    Emali=models.EmailField()
    snumber=models.IntegerField()
    date=models.DateField()

    

     

