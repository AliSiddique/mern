from django.conf.urls import include
from django.urls import path, re_path
from django.views.generic.base import TemplateView

accounts_urlpatterns = [
    path("api/auth/", include("dj_rest_auth.urls")),
    path("api/auth/register/", include("dj_rest_auth.registration.urls")),
       re_path(
        r"^verify-email/(?P<key>[-:\w]+)/$",
        TemplateView.as_view(),
        name="account_confirm_email",
    ),
]