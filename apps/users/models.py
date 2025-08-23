from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Provider(models.Model):
    name = models.CharField(max_length=20, unique=True)
    display_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'providers'
    
    def __str__(self):
        return self.display_name


class UserManager(BaseUserManager):
    def create_user(self, email, ci, provider, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not ci:
            raise ValueError('The CI field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, ci=ci, provider=provider, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, ci, provider, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, ci, provider, **extra_fields)


class User(AbstractBaseUser):
    di = models.CharField(max_length=100, unique=True, default='', help_text="DI - 우리 서비스의 고유 사용자 식별자")
    email = models.EmailField(unique=True)
    ci = models.CharField(max_length=200, default='', help_text="CI - 소셜 플랫폼의 고유 식별자")
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, blank=True)
    profile_image = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['ci', 'provider']
    
    class Meta:
        db_table = 'users'
        unique_together = ['ci', 'provider']
    
    def __str__(self):
        return f"{self.email} ({self.provider})"
    
    def save(self, *args, **kwargs):
        if not self.di:
            import uuid
            self.di = str(uuid.uuid4()).replace('-', '')[:20]
        super().save(*args, **kwargs)
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return self.is_superuser
