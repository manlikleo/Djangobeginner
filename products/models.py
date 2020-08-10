from django.db import models

# Create your models here.
class product(models.Model):
    title = models.CharField(max_length=120,) #max_length is required
    Description  = models.TextField(blank=True,null= True)
    Price= models.DecimalField(decimal_places=2,max_digits=1000)
    summary = models.TextField(blank=False,null=False)
    featured = models.BooleanField(default=False) #null = true default = True