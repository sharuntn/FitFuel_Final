from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    
    class Meta:
        db_table = "foodlens_Warehouse"

class Nutrients(models.Model):
    food = models.CharField(max_length=100)
    desc = models.TextField()
    energy = models.FloatField()
    carbohydrates = models.FloatField()
    protien = models.FloatField()
    fat = models.FloatField()
    sugar = models.FloatField()
    health_score = models.FloatField()

class Intake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    calories = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)