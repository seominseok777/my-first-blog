from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(r'^010[1-9]\d{7}$')])
