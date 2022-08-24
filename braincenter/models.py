from django.db import models
"""
1. Create the following models:
	a). Series_type:
			- id => Primary key, Auto increment
			- Name => Varchar with max_length = 30
			- Mnemonic => Varchar with max_length = 4
"""
class SeriesType(models.Model):
    id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=30)
    mnemonic  = models.CharField(max_length=4)
    
    def __str__(self):
        return self.name
"""
1. b). Series:
			- id => Primary key, Auto increment
			- Name => Varchar with max_length = 255
			- Series_type => Foreign key refererring from Series_type.id
"""

class Series(models.Model):
    id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=225)
    series_type =  models.ForeignKey(SeriesType, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
   
"""
1. c). Series_set:
			- id => Primary key, Auto increment
			- Name => Varchar with max_length = 255
			- Series => Forign key refererring from Series.id
"""    
class SeriesSet(models.Model):
    id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=225)
    series  =  models.ForeignKey(Series, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

