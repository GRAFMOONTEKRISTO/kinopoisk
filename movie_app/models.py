from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Director(models.Model):
    name_director = models.CharField(max_length=100)
    surname_director = models.CharField(max_length=100)
    director_email = models.EmailField(default='Zalupa@s.gorы')

    def __str__(self):
        return f' {self.name_director} {self.surname_director} {self.director_email}'


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
    slug = models.SlugField(default='', null=False)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='RUB')

    # """SLUG"""
    #
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return f' {self.name} {self.rating}% {self.budget} {self.year}'

    """Перенаправление фильма на all_movies.html, для создания ссылки"""

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

# In [1]: from movie_app.models import Movie
