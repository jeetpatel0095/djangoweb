from django.db import models

# Create your models here.

class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=50)
    
    def __str__(self):
        return self.cname
    
class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50)
    pdis = models.TextField()
    pprice = models.FloatField()
    pimage = models.ImageField(upload_to='product')
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.pname