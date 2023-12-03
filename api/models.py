from django.db import models
from django.contrib.auth.models import AbstractUser


class custom(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    birthday = models.DateField()
    occupation = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    additional_data = models.JSONField(blank=True, null=True)


class sell(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    birthday = models.DateField()
    occupation = models.CharField(max_length=255)
    active = models.BooleanField(default=False)

class admin(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class image_upload(models.Model):
    image = models.ImageField(upload_to='uploads/')


