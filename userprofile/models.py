from django.contrib.auth.models import User
from django.db import models
from show.models import Show

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    shows = models.ManyToManyField(Show)
