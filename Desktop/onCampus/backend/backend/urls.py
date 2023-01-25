from accounts.urls import accounts_urlpatterns
from django.contrib import admin
from django.urls import path
from listing.urls import listing_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += accounts_urlpatterns
urlpatterns += listing_urlpatterns