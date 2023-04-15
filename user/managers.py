from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy

class CustomUserManager(BaseUserManager):

	def create_user(self,email,password, **extra_fields):
		if not email:
			raise ValueError(gettext_lazy('The email must br set'))
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save()
		return user
	def creat_superuser(self,email,password, **extra_fields):
		extra_fields.setdefault('is_active',True)
		extra_fields.setdefault('is_superuser',True)
		extra_fields.setdefault('is_staff',True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError(gettext_lazy('Superuser must have is_staff=True.'))
		if extra_fields.get('is_superuser') is not True:
			raise ValueError(gettext_lazy('Superuer must have is_superuser=True.'))
		return self.create_user(email,password, **extra_fields)
