from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=20, choices=[
        ('Male','Male'),
        ('Female','Female'),
    ],default='Male')
    mobile = models.CharField(max_length=15, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    abdomen = models.FloatField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    output = models.CharField(blank=True,null=True)
    bmi = models.FloatField(blank=True, null=True)
    activity_level = models.FloatField(max_length=20,choices=[
        ( 1.55,'Sedentary'),
        ( 1.85, 'Moderately active'),
        ( 2.2, 'Vigorously active'),
        ( 2.4, 'Extremely active')
    ],default=1.85)
    diabetic = models.CharField(max_length=20, choices=[
        ('diabetic', 'Diabetic'),
        ('not_diabetic', 'Not Diabetic'),
        ('not_sure', 'Not Sure'),
    ], default='not_sure')

    def __str__(self):
        return self.user.username