from django.db import models
from django.contrib.auth.models import AbstractUser


class Base(models.Model):
    is_active = models.BooleanField(default=False)

    inserted_since = models.DateField(auto_now_add=True)
    inserted_by = models.ForeignKey('User', related_name="entries_inserted", null=True, on_delete=models.PROTECT)

    last_updated_since = models.DateField(auto_now=True)
    updated_by = models.ForeignKey('User', related_name="entries_updated", null=True, on_delete=models.PROTECT)

    class Meta:
        abstract = True


class User(AbstractUser, Base):
    sigaa_registration_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    sigaa_user_name = models.CharField(max_length=50, unique=True, blank=True, null=True)
    sigaa_token = models.CharField(max_length=200, blank=True, null=True)
    photo = models.ImageField(upload_to='avatars/', null=True, blank=True)
