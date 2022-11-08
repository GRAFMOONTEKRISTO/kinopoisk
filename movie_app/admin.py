from django.contrib import admin
from .models import Movie, Director

# Register your models here.

admin.site.register(Director)

"""С помощью класса, принято называть его MovieAdmin, и обращаться admin.ModelAdmin
1. с помощью list_display выводим в админке поля, которые нам нужны,
2. с помощью list_editable, разрешаем редактирование написанных полей
3. с помощью ordering сортируем нужные поля (по методам сортировки Django)
4. с помощью list_per_page можем показать сколько хотим видеть фильмов на одной странице
5. с помощью search_fields можем добавить мини-поисковик, где можно использовать методы поиска DJANGO
6. с помощью readonly_fields можем сделать запрет на редактирование этого поля
7. с помощью exclude можем исключить поля редактирования
8. с помощью prepopulated_fields можем без создания класса, сделать автоматическим поле SLUG"""

"""Создаем новый класс RatingFilter, ФУНКЦИЯ lookups отвечает """


class RatingFilter(admin.SimpleListFilter):
    title = 'Filter by rating'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Low Rating'),
            ('от 40 до 59', 'Middle Rating'),
            ('от 60 до 79', 'High Rating'),
            ('>=80', 'Very High Rating'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value() == 'от 60 до 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=80)
        if self.value() == '>=80':
            return queryset.filter(rating__gte=80)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'currency', 'budget', 'rating_status']
    list_editable = ['rating', 'currency', 'budget']
    ordering = ['rating', 'currency']
    list_per_page = 10
    search_fields = ['name__startswith', 'rating']
    list_filter = ['name', 'currency', RatingFilter]
    readonly_fields = ['year']
    prepopulated_fields = {'slug': ('name',)}
    # exclude = ['name', 'rating']

    """С помощью новой функии можем добавить новое поле,
     при условии, что навание функции добавим в list_display"""

    """Переменная в функции может называтся как угодно и чтобы наша IDE давала подсказки
    нужно проанонсировать, нужно подсказать PyCharm какой у нее тип - Movie. Но можно и без этого"""

    """При навешивании декоратора мы можем, в наше новое вычисляемое поле, добавить сортировку
    и добавляем rating - потому что они эквивалентны - отсортируется рейтинг синхронно с новым полем
    description - меняет название поля"""

    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Зачем это смотреть!?'
        if mov.rating < 70:
            return 'Разок можно глянуть'
        if mov.rating <= 85:
            return 'Зачет'
        return 'Топчик'

# """Привязка нашей модели Movie с классом MovieAdmin"""
# """Регистрация нашего класса и что к нему привязвается """
# """Можно навесить декоратор"""
# admin.site.register(Movie, MovieAdmin)
