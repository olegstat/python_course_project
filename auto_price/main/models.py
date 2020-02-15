from django.db import models

class CarBase(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    year = models.IntegerField()
    engine = models.IntegerField(default=0)
    gearbox = models.CharField(max_length=50)
    ad_url = models.URLField()
    ad_date = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
    
    def __str__(self):
        return(self.make + " " + self.model)
