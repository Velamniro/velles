from django.db import models
from django.utils.html import mark_safe

from users_app.models import CustomUser

# Create your models here.
class File(models.Model):
    title = models.CharField("Название файла", max_length=128)
    about = models.CharField("О чем этот файл", max_length=250)
    description = models.TextField("Полное описание")

    url = models.URLField("Ссылка для скачивания", max_length=120)
    slug = models.SlugField("URL", unique=True, db_index=True)
    create_datetime = models.DateTimeField("Дата и время создания", auto_now_add=True)

    game = models.ForeignKey('Game', on_delete=models.PROTECT, blank=False, null=False, related_name='files')
    type = models.ForeignKey('Type', on_delete=models.PROTECT, blank=False, null=False, related_name='files')

    favourite = models.ManyToManyField(CustomUser, default=None, blank=True, related_name='favourites')
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='files')

    objects = models.Manager()

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
        

class FileImage(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField("Изображение", upload_to='files/images')
    main = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Изображение файла"
        verbose_name_plural = "Изображении файла"

    def img_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')

class Game(models.Model):
    name = models.CharField("Название игры", max_length=128)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

class Type(models.Model):
    name = models.CharField("Тип(например мод)", max_length=128)
    games = models.ManyToManyField(Game, default=None, blank=True, related_name='types')

    def __str__(self):
        games = []
        for game in self.games.all():
            games.append(game.pk)
        return f'{self.name} [{games}]'
    
    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"
    