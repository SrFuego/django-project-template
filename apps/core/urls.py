# Python imports


# Django imports
from django.conf.urls import include, url


# Third party apps imports


# Local imports
from .views import IndexView


# Create your urlpatterns here.
urlpatterns = [
    url(r"^$", IndexView.as_view(), name="index"),
]
