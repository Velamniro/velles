from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(File)
class FilesAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title')

@admin.register(FileImage)
class FileImageAdmin(admin.ModelAdmin):
    list_display = ('img_preview', 'id')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    search_fields = ('name', 'id')
    list_display = ('name', 'id')

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    search_fields = ('name', 'games', 'id')
    list_display = ('name', 'id')