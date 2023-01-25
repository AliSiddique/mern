from django.contrib import admin
from .models import Listing, ListingViews, ListingTour, ListingMail
# Register your models here.

admin.site.register(Listing)
admin.site.register(ListingViews)
admin.site.register(ListingTour)
admin.site.register(ListingMail)