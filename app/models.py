from django.db import models
from django.utils.translation import ugettext_lazy as _
from .at import send_message

class Subscriber(models.Model):
	fname = models.CharField(_('first name'), max_length=50)
	lname = models.CharField(_('last name'), max_length=50)
	address = models.CharField(_('address'), max_length=50)
	gender = models.CharField(_('gender'), max_length=50)
	email = models.EmailField(_('email'), max_length=50, unique=True, null=True, blank=True)
	phone = models.CharField(_('phone number'), max_length=50, unique=True)

	def __str__(self):
		return self.phone if self.phone else ''

	def get_full_name(self):
		return f'{self.fname} {self.lname}'

	def get_email(self):
		return self.email or ''

	def welcome_subcriber(self):
		message = f'Dear {self.get_full_name()} welcome to Adashe !'
		send_message(message=message, recipients=[self.phone,])

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		self.welcome_subcriber()
		return self