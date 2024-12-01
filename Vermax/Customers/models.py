from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    LIVE=1                          #VARIABLES FOR DISPLAYING PRIORITY PRODUCTS LIKE SEASONAL PRODUCTS
    DELETE=0                        #The prority product will go live when it is 1
                                    #and get deletes when it is 0                                                
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete')) #tuples
    name=models.CharField(max_length=50)
    address=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')
    phone=models.CharField(max_length=10)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)  #Shows when product was added automatically
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title