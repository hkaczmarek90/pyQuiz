from django.contrib.auth.models import User as DjangoUser
from django.db import models


class User(DjangoUser):
    def __str__(self):
        return self.username
