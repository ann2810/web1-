from django.db import models

class Agent1(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField(max_length=500)
    picture = models.ImageField()
    time = models.DateTimeField()

    def __str__(self):
        return self.email

class Agent2(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField(max_length=500)
    picture = models.ImageField()
    time = models.DateTimeField()

    def __str__(self):
        return self.email

class Client(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField(max_length=500)
    picture = models.ImageField()
    time = models.DateTimeField()

    def __str__(self):
        return self.email
