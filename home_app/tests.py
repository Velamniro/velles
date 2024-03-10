"""Copyright 2024 Velamniro

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch

# Create your tests here.
class TestViews(TestCase): 
    def setUp(self) -> None:
        # Create user
        from users_app.models import CustomUser
        user = CustomUser.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

    def test_HomeView_getrequest_200code(self) -> None:
        # Act
        response = self.client.get(reverse('home'))
        # Assert
        self.assertEqual(response.status_code, 200)
    
    @patch('home_app.views.get_object_or_404')
    def test_FileView_getrequestwithmockobj_200code(self, mock_get_object_or_404) -> None:
        # Arrange
        mock_get_object_or_404.return_value = FakeFileObject('a', 'a', 'a', {'username': 'a'})
        self.client.login(username='testuser', password='12345')
        # Act
        response = self.client.get(reverse('file', args=[mock_get_object_or_404.return_value.slug]))
        # Assert
        self.assertEqual(response.status_code, 200)
        # Final
        self.client.logout()

    
    def test_FileView_getrequestNOTexists_404code(self) -> None:
        # Arrange
        slug = 'DOESNT-EXIST-SLUG'
        # Act
        response = self.client.get(reverse('file', args=[slug]))
        # Assert
        self.assertEqual(response.status_code, 404)
    
    def test_about_getrequest_200code(self) -> None:
        # Act
        response = self.client.get(reverse('about'))
        # Assert
        self.assertEqual(response.status_code, 200)

class TestModels(TestCase):
    def setUp(self) -> None:
        from .models import File, Game, Type
        self.game_obj = Game.objects.create(name="Game name")
        self.type_obj = Type.objects.create(name="Type name")
        self.type_obj.games.add(self.game_obj.id)
        self.file_obj = File.objects.create(
            name="Test name",
            about="About of file",
            description="Description of file",
            url='https://example.com/',
            slug='slug_of_file',
            type=self.type_obj,
            game=self.game_obj,
        )
    
    def test_FileImage_addFileImageToFile_correctlyAdding(self):
        # Arrange
        from .models import FileImage
        from django.core.files.uploadedfile import SimpleUploadedFile
        # Act
        FileImage_obj1 = FileImage.objects.create(file=self.file_obj, main=True,
                                                  image=SimpleUploadedFile('test_name.png',
                                                                           b'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAA1JREFUGFdj+P///38ACfsD/QVDRcoAAAAASUVORK5CYII='))
        FileImage_obj2 = FileImage.objects.create(file=self.file_obj, main=False,
                                                  image=SimpleUploadedFile('test_name2.jpg',
                                                                           ''))
        # Assert
        self.assertEqual(self.file_obj.images.filter(main=True).first(), FileImage_obj1)
        self.assertNotEqual(self.file_obj.images.filter(main=False).first(), FileImage_obj1)

        self.assertEqual(self.file_obj.images.filter(main=False).first(), FileImage_obj2)
        self.assertNotEqual(self.file_obj.images.filter(main=True).first(), FileImage_obj2)

        self.assertEqual(FileImage_obj1.file, FileImage_obj2.file)
        self.assertEqual(FileImage_obj1.file, self.file_obj)
        self.assertEqual(FileImage_obj2.file, self.file_obj)


class FakeFileObject():
    def __init__(self, game, type, create_datetime, author, name = 'a', description = 'a', slug = 'a') -> None:
        self.name = name
        self.description = description
        self.game = game
        self.type = type
        self.create_datetime = create_datetime
        self.author = author
        self.slug = slug