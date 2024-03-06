from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
    )

    gender = models.CharField('Пол', max_length=1, choices=GENDERS, default='')
    birth_date = models.DateField('День рождения', default='2000-01-01')
    avatar = models.ImageField('Аватарка', upload_to='users/avatars/', blank=True, null=True, default='default_avatar.png')

    def __str__(self):
        return self.username