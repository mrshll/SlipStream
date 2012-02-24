from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=40)
    url = models.URLField()

class Show(models.Model):
    name = models.CharField(max_length=40)
    def __unicode__(self):
        return self.name

class Episode(models.Model):
    title = models.CharField(max_length=100)
    show = models.ForeignKey(Show)
    air_date = models.DateTimeField()
    providers = models.ManyToManyField(Provider)