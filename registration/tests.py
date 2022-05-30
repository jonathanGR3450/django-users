from django.test import TestCase
from registration.models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):

    def setUp(self):
        User.objects.create_user('test', 'test@test.com', 'lol123lol')
    
    def test_exist_profile(self):
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True)
