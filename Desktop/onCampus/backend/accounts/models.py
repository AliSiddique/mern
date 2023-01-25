from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from twilio.rest import Client
account_sid = "ACeb0ed1563fc23141dc75167b759cb037"
auth_token = "0b4b2b938986b42b4c42bc2278a1b822"
client = Client(account_sid, auth_token)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # custom fields for user
    plan = models.CharField(max_length=200, default="free", blank=True)
    is_landlord = models.BooleanField(default=False)
    plan = models.CharField(max_length=200, default="free", blank=True)
    image = models.ImageField(upload_to="profile_images", blank=True)
    phone = models.CharField(max_length=200, blank=True,null=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    monday = models.CharField(max_length=200, blank=True)
    tuesday = models.CharField(max_length=200, blank=True)
    wednesday = models.CharField(max_length=200, blank=True)
    thursday = models.CharField(max_length=200, blank=True)
    friday = models.CharField(max_length=200, blank=True)
    saturday = models.CharField(max_length=200, blank=True)
    sunday = models.CharField(max_length=200, blank=True)
    want_location = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        subject = "welcome"
        msg = "welcome to our site"

        email = EmailMessage(subject, msg, to=[instance.email])
        email.send()
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()