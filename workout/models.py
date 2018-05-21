from django.db import models

# Create your models here.
class Workout(models.Model):
    movement = models.CharField(max_length=30)
    reps = models.IntegerField(max_length=4)
    
