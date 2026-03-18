from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()

class UserProfileSignalTest(TestCase):
    def test_profile_created_on_user_signup(self):
        """
        Verify that a UserProfile is automatically created when a new user is created.
        """
        email = "testuser@example.com"
        password = "password123"
        user = User.objects.create_user(email=email, password=password)
        
        # Check if profile exists
        self.assertTrue(hasattr(user, 'userprofile'))
        self.assertEqual(user.userprofile.user, user)
        
    def test_profile_saved_on_user_save(self):
        """
        Verify that the profile is saved when the user object is saved.
        """
        user = User.objects.create_user(email="testsave@example.com", password="password123")
        user.userprofile.bio = "Initial bio"
        user.userprofile.save()
        
        user.name = "Updated Name"
        user.save()
        
        # Refresh from DB
        user.refresh_from_db()
        self.assertEqual(user.userprofile.bio, "Initial bio")
