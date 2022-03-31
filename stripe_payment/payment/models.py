from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):

    name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    image = models.ImageField(upload_to="profile_images", null=True, blank=True)
    cover_image = models.ImageField(upload_to="profile_images", null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    timezone = models.CharField(max_length=255, null=True, blank=True)
    country_code = models.CharField(max_length=10, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    terms_and_condition = models.BooleanField(default=False)
    certify = models.BooleanField(default=False)

    credits = models.PositiveIntegerField(default=0)
    amount = models.FloatField(default=0.0)

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class TimeStampModel(models.Model):
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class ErrorLog(TimeStampModel):
    error = models.TextField()

    def __str__(self):
        return str(self.error)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = "4- Error while buying credits"


