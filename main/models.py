from django.db import models

# Create your models here.
class Person(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    prog_lang=models.CharField(max_length=100)
    start_date=models.DateField()
    confirm=models.BooleanField()