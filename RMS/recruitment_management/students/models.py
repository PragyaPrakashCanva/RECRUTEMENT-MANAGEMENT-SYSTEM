from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    enrollment = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    tenth = models.FloatField()
    twelfth = models.FloatField()
    resume = models.FileField(upload_to='resumes/')
    profile_picture = models.ImageField(upload_to='profile_pictures/')

    def __str__(self):
        return self.name
