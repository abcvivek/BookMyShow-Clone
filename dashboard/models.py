from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator
from django import forms
from django.contrib.auth.models import User

#Create your models here.

class theatre_manager(models.Model) :

    name = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone = models.BigIntegerField()

    def __str__(self) :
        return self.name

    def get_absolute_url(self) :
        return reverse("dashboard:theatre-manager-view")

class theatre(models.Model) :
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    theatre_manager = models.ForeignKey(theatre_manager,related_name="theatre",on_delete=models.CASCADE)

    def __str__(self) :
        return self.name

    def get_absolute_url(self) :
        return reverse("dashboard:theatre-view")

class screen(models.Model) :
    name = models.CharField(max_length=20)
    no_of_rows = models.IntegerField(validators=[MaxValueValidator(75)])
    no_of_columns = models.IntegerField(validators=[MaxValueValidator(50)])
    theatre = models.ForeignKey(theatre,related_name="screen",on_delete=models.CASCADE)

    def __str__(self) :
        return "{x} {y}".format(x=self.name,y=self.theatre.name)

    def get_absolute_url(self) :
        return reverse("dashboard:screen-view")


class movie(models.Model) :
    name = models.CharField(max_length=50)
    hero = models.CharField(max_length=30)
    heroine = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    genre = models.CharField(max_length=150,help_text='Seperate genre with spaces',null=True)
    language = models.CharField(max_length=150,help_text='Seperate language with spaces',null=True)
    description = models.TextField(default='Description Text')
    release_date = models.DateField(help_text='mm/dd/yyyy')
    runtime_in_minutes = models.IntegerField(validators=[MaxValueValidator(200)])
    trailer = models.CharField(max_length=1000)
    thumbnail_image = models.ImageField(upload_to='movie_thumbs')
    slideshow_image = models.ImageField(upload_to='movie_thumbs',default='true')

    def __str__(self) :
        return self.name

    def get_absolute_url(self) :
        return reverse("dashboard:movie-view")

class show(models.Model) :
    date = models.DateField()
    time = models.TimeField()
    price = models.IntegerField()
    screen = models.ForeignKey(screen,related_name="show_screen",on_delete=models.CASCADE)
    theatre = models.ForeignKey(theatre,related_name="show_theatre",on_delete=models.CASCADE)
    movie = models.ForeignKey(movie,related_name="show_movie",on_delete=models.CASCADE)

    def __str__(self) :
        return "Date : {}".format(self.date)

    def get_absolute_url(self) :
        return reverse("dashboard:show-view")