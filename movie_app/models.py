from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Director(models.Model):
    name_director = models.CharField(max_length=100)
    surname_director = models.CharField(max_length=100)
    director_email = models.EmailField(default='Zalupa@s.gorы')
    slug = models.SlugField(default='', null=False, db_index=True)

    def __str__(self):
        return f' {self.name_director} {self.surname_director} {self.director_email}'

    def get_url_director(self):
        return reverse('one_dir', args=[self.id])


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]

    name_actor = models.CharField(max_length=100)
    surname_actor = models.CharField(max_length=100)

    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер {self.name_actor} {self.surname_actor}'
        else:
            return f'Актриса {self.name_actor} {self.surname_actor}'


class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'

    """Поле CHOICES используется, когда есть ограниченое множество элементов (пол, сезон года, )"""

    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=10000, validators=[MinValueValidator(0), MaxValueValidator(10000000)])
    slug = models.SlugField(default='', null=False, db_index=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='RUB')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return f' {self.name} {self.rating}% {self.budget} {self.year}'

    """Перенаправление фильма на all_movies.html, для создания ссылки"""

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

# In [1]: from movie_app.models import Movie
