from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from .models import *

def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(
			user=instance,
			first_name=instance.first_name,
			last_name=instance.last_name,
			email=instance.email,
			)
		print("Profile Created!")


def update_profile(sender, instance, created, **kwargs):
	if created == False:
		instance.profile.first_name = instance.first_name
		instance.profile.last_name = instance.last_name
		instance.profile.email = instance.email
		instance.profile.save()
		print("Profile updated!")

post_save.connect(create_profile, sender=User)
post_save.connect(update_profile, sender=User)


def update_username(sender, instance, **kwargs):
	instance.username = instance.email
	print("Username updated!", instance.username)

pre_save.connect(update_username, sender=User)