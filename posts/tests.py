from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post

# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email='bH9tZ@example.com',
            password='secret'
        )
        cls.post = Post.objects.create(
            author=cls.user,
            title='this is title',
            body='this is body'
        )
    
    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.title, 'this is title')
        self.assertEqual(self.post.body, 'this is body')
        self.assertEqual(str(self.post), 'this is title')