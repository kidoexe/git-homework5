from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Student(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    grade = models.PositiveSmallIntegerField(validators=[
            MaxValueValidator(12),
            MinValueValidator(1)])
    is_active = models.BooleanField(True)


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField(validators=[
            MaxValueValidator(65),
            MinValueValidator(0)])
    is_active = models.BooleanField(True)

class Class(models.Model):
    name = models.CharField(max_length= 20)
    start_date = models.DateField()
    end_date = models.DateField()   
    is_active = models.BooleanField(True)