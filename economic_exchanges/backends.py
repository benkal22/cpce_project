from typing import Any
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.http import HttpRequest

class SuperUserAdminBackend(ModelBackend):
    def authenticate(self, request: HttpRequest, username: str | None, password: str | None, **kwargs: Any):
        user = User.objects.filter(username=username).first()
        if user and user.is_superuser and user.check_password(password, user.password):
            return user
        return None
