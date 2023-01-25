from django.conf.urls import include
from django.urls import path
from .views import create_listing, update_listing, delete_listing, create_mail, create_tour, get_mail, get_mails, get_tour, get_tours, get_listing,get_listings, ListingList

listing_urlpatterns = [
    path("api/listing/all", get_listings),
    path("api/listing/create", create_listing),
    path("api/listing/update/<int:pk>", update_listing),
    path("api/listing/delete/<int:pk>", delete_listing),
    path("api/listing/<int:pk>", get_listing),
    path('api/listing/search', ListingList.as_view(), name='search'),
    # mail
    path("api/mail/create", create_mail),
    path("api/mail/<int:pk>", get_mail),
    path("api/mails", get_mails),
    # tour
    path("api/tour/create", create_tour),
    path("api/tour/<int:pk>", get_tour),
    path("api/tours", get_tours),
  
  
]
