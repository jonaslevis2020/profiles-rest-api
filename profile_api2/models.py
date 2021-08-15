

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.fields import BooleanField, CharField, EmailField


# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)

        user.save(using=self.db)

        return user

    def create_superuser(self, email, name, password):
        """create and save a new superuser with given details"""

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin, models.Model):
    """Database model for users in the system"""
    email = EmailField(max_length=50, unique=True)
    name = CharField(max_length=100)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserProfileManager()

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def __str__(self):
        """Return a string representation of the user"""
        return self.email
    # class Meta:
    #     odering = ['-id']
