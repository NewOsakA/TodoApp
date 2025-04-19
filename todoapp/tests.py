from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from .models import Todo


def generate_test_image():
    image = Image.new('RGB', (100, 100), color='blue')
    byte_io = BytesIO()
    image.save(byte_io, 'JPEG')
    byte_io.seek(0)
    return SimpleUploadedFile('test.jpg', byte_io.read(), content_type='image/jpeg')


class TodoAppTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='strongpass123')

    def test_signup_valid(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password1': 'StrongPassword123',
            'password2': 'StrongPassword123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_signup_invalid_username(self):
        response = self.client.post(reverse('signup'), {
            'username': 'Invalid User',
            'password1': 'StrongPassword123',
            'password2': 'StrongPassword123'
        })
        self.assertContains(response, "Enter a valid username")

    def test_login_valid(self):
        login = self.client.login(username='testuser', password='strongpass123')
        self.assertTrue(login)

    def test_create_todo_without_image(self):
        self.client.login(username='testuser', password='strongpass123')
        response = self.client.post(reverse('todo_create'), {
            'title': 'Write Report',
            'description': 'Complete weekly report',
            'status': 'pending'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Todo.objects.filter(title='Write Report').exists())

    def test_create_todo_with_image(self):
        self.client.login(username='testuser', password='strongpass123')
        img = generate_test_image()
        response = self.client.post(reverse('todo_create'), {
            'title': 'Design Logo',
            'description': 'Upload logo sketch',
            'status': 'in_progress',
            'image': img
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Todo.objects.filter(title='Design Logo').exists())

    def test_delete_todo(self):
        self.client.login(username='testuser', password='strongpass123')
        todo = Todo.objects.create(title='Trash Me', user=self.user, status='pending')
        response = self.client.post(reverse('todo_delete', args=[todo.id]))
        self.assertRedirects(response, reverse('todo_list'))
        self.assertFalse(Todo.objects.filter(id=todo.id).exists())
