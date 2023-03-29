import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.expressions import Value
from django.http.request import validate_host





class AccountManager(BaseUserManager):
    def create_user(self, fullName, email, phoneNumber, role, password=None):
        if not fullName:
            return ValueError('full name required')
        if not email:
            raise ValueError('email required')
        if not phoneNumber:
            raise ValueError('phone number required')
        if not role:
            raise ValueError('role required')
        user = self.model(
            fullName=fullName,
            email=self.normalize_email(email),
            phoneNumber=phoneNumber,
            role=role
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, fullName, email, phoneNumber, role, password):
        user = self.create_user(
            fullName=fullName,
            email=self.normalize_email(email),
            phoneNumber=phoneNumber,
            role=role,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    ROLES = [
        ('admin', 'admin'),
        ('client', 'client'),
        ('technician', 'technician'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullName = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    phoneNumber = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=30,choices=ROLES)
    county = models.CharField(max_length=200, null=True, blank=True)
    # businessDescription = models.TextField(null=True, blank=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullName', 'phoneNumber', 'role']

    def __str__(self):
        return self.fullName
        
    objects = AccountManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons

    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app?
    def has_module_perms(self, app_label):
        return True
