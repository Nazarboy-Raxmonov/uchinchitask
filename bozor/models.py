from django.db import models
from datetime import datetime

class sotuvchi(models.Model):
    ism = models.TextField(max_length=25)
    familiya = models.TextField(max_length= 25)
    tugilgan_sana = models.DateField()
   
    def __str__(self) -> str:
        return self.ism
    
    class Meta:
        db_table = 'sotuvchi'


class mahsulot(models.Model):
    nomi = models.TextField(max_length=25)
    ics = models.DateField(default = datetime.now)
    miqdori = models.IntegerField()
    owner = models.ForeignKey(sotuvchi, on_delete= models.CASCADE)
    def __str__(self) -> str:
        return self.nomi
    

    class Meta:
        db_table = 'mahsulot'


# Create your models here.
