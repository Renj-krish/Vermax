from django.db import models

# Model for Product

class Product(models.Model):
    LIVE=1                          #VARIABLES FOR DISPLAYING PRIORITY PRODUCTS LIKE SEASONAL PRODUCTS
    DELETE=0                        #The prority product will go live when it is 1
                                    #and get deletes when it is 0                                                
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete')) #tuples
    title=models.CharField(max_length=50)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='media')
    priority=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)  #Shows when product was added automatically
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title