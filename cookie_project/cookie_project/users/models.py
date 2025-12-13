from django.db import models
from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db.models import EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class User(AbstractUser):
    """
    Default custom user model for cookie-project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]
    email = EmailField(_("email address"), unique=True)
    username = None  # type: ignore[assignment]
    phone = models.CharField(_("Phone"), max_length=20, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})

class Course(models.Model):
    COURSE_CHOICES = {
    "PR": "Programming",
    "LE": "Literature",
    "GE": "Geography",
    }

    PAYMENT_CHOICES = {
    "CC": "credit card",
    "CA": "cash",
    }

    STATUS_CHOICES = {
    "AC": "active",
    "CO": "completed",
    "DR": "dropped",
    "NW": "new",
    }

    name = models.CharField(max_length=200, choices=COURSE_CHOICES)
    date = models.DateField(null=True, blank=True)
    payment = models.CharField(max_length=2, choices=PAYMENT_CHOICES)
    student = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="NW")

    def __str__(self):
        return self.name
