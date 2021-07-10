from django.db import models
#v useful abstract class for user - always recommended by Django for future use
from django.contrib.auth.models import AbstractUser



# Create your models here.

class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Lead(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    #Foreign Keys are a one to many from the present class to the Foreign Key 
    #Foreign Key for table must be above ^^^ without string, or as string within THIS dir
    agent=models.ForeignKey("Agent", on_delete=models.CASCADE) #CASCADE

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
