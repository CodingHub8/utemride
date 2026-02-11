from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_utem_email


class User(AbstractUser):
    """Custom user model with UTeM email validation"""
    email = models.EmailField(
        unique=True,
        validators=[validate_utem_email],
        error_messages={
            'unique': 'This email is already registered.',
            'invalid': 'Enter a valid UTeM email address.',
        }
    )

    # User type
    USER_TYPE_CHOICES = (
        ('passenger', 'Passenger'),
        ('driver', 'Driver'),
        ('admin', 'Administrator'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='passenger')

    # Driver verification fields
    is_verified_driver = models.BooleanField(default=False)
    student_id = models.CharField(max_length=20, blank=True, null=True)
    license_number = models.CharField(max_length=50, blank=True, null=True)

    # Basic info
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.username} - {self.email}"