from django.db import models

# Create your models here.

class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'actors'

class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField(default = 0)
    actors = models.ManyToManyField(
        Actor,
        related_name='movie_actor'
    )
    class Meta:
        db_table = 'movies'


