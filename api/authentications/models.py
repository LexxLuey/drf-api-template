from django.contrib.auth.models import AbstractUser, PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    pass

    # REQUIRED_FIELDS = []

    # objects = UserManager()

    # def __str__(self):
    #     return self.email
