from django.db import models
from django.contrib.auth.models import User


class Image (models.Model):

    image = models.ImageField(upload_to='images')
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='image')
