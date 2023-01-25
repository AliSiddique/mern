from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    address = models.CharField(max_length=200)
    property_type = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    sqft = models.IntegerField()
    bathrooms = models.IntegerField()
    is_published = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='listing/images')
    photo_1 = models.ImageField(upload_to='listing/images', blank=True,null=True)
    photo_2 = models.ImageField(upload_to='listing/images', blank=True)
    photo_3 = models.ImageField(upload_to='listing/images', blank=True)
    photo_4 = models.ImageField(upload_to='listing/images', blank=True)
    photo_5 = models.ImageField(upload_to='listing/images', blank=True)
    photo_6 = models.ImageField(upload_to='listing/images', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title



class ListingViews(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.listing.title        



class ListingTour(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.listing.title



class ListingMail(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.TextField()
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.listing.title