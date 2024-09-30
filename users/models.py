from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinLengthValidator

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('El email debe ser proporcionado')
        if not password:
            raise ValueError('La contraseña debe ser proporcionada')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Almacena el password de forma segura
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)  # Esto es importante para el superusuario

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):  
    email = models.EmailField(unique=True, max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Puedes agregar otros campos obligatorios si es necesario

    def __str__(self):
        return self.email
