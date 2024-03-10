"""Copyright 2024 Velamniro

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(File)
class FilesAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name')

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