from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


#Controla la creacion de usuarios y superusuarios
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        #Verifica que haya email
        if not email:
            raise ValueError("The email field must be set")
        
        #Normaliza el email, lo convierte a minusculas entre otras cosas
        email = self.normalize_email(email)
        #le asigna el email, y las extra_fields
        user = self.model(email=email, **extra_fields)
        #Hashea la password
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):   
        #Establece los valores default de un superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        #Validaciones
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    nickname = models.CharField("Nicname", max_length=155, null=False,blank=False, unique=True)
    first_name = models.CharField('First Name', max_length=155, null=False,blank=False)
    last_name = models.CharField('Last Name', max_length=155, null=False,blank=False)
    email = models.EmailField(unique=True, null=False,blank=False)
    profile_picture = models.ImageField(upload_to='profile_picture/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #Especifica que el modelo usa CustomUserManager para la creacion de usuarios
    objects = CustomUserManager()

    #Define que el correo electrónico es el identificador principal para la autenticación.
    USERNAME_FIELD = 'email'

    #Campos que son obligatorios
    REQUIRED_FIELDS = ['nickname', 'first_name', 'last_name']

    def __str__(self) -> str:
        return self.nickname