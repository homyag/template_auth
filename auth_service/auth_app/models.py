from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Добавьте дополнительные поля, если необходимо

    class Meta:
        # Укажите аргумент related_name для groups и user_permissions
        # чтобы избежать конфликта имен
        # Например, используйте "customuser_groups" и "customuser_user_permissions"
        # или любые другие уникальные значения
        permissions = [
            ("can_do_something", "Can do something"),
        ]
        abstract = False
        swappable = "AUTH_USER_MODEL"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"