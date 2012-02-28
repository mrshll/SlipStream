from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=40)
    url = models.URLField()

class Show(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(blank=True)

    img_url = models.URLField(blank=True)

    first_aired = models.CharField(max_length=100, null=True)
    air_day_of_week = models.CharField(max_length=20, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    rating_count = models.IntegerField(null=True)
    status = models.CharField(max_length=10, null=True)

    #network
    #genre

    imdb_id = models.IntegerField(null=True)
    api_id = models.IntegerField(null=True)
    last_update = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.name

class Episode(models.Model):
    title = models.CharField(max_length=100)
    show = models.ForeignKey(Show)
    air_date = models.DateTimeField()
    providers = models.ManyToManyField(Provider)