from django.db import models

from django.contrib.auth.models import User

class Continent(models.Model):
    label = models.CharField(max_length=40)
    last_modified_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_continent')
    def __str__(self):
        return self.label

class Country(models.Model):
    continent = models.ForeignKey(Continent,on_delete=models.CASCADE,related_name='continent_country')
    label = models.CharField(max_length=35)
    last_modified_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_country')
    def __str__(self):
        return self.label
    def continentLabel(self):
        return self.continent

class City(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE,related_name='country_city')
    label = models.CharField(max_length=150)
    last_modified_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_city')
    def __str__(self):
        return self.label 
    def countryLabel(self):
        return self.country