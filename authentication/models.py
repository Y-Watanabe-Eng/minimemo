from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class CustomUser(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(validators=[
                                    RegexValidator(
                                        regex = r'^(?=.*?[a-z])(?=.*?[0-9]).*$',
                                        message='Passwordは大文字・小文字・数字・記号のうち少なくとも2種類を含める必要があります。',
                                    ),
                                ])
    
    def __str__(self):
        return self.username
    
    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        if password:
            user = self.model(username=username, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
        else:
            raise ValueError("Passwordは必須です。")


