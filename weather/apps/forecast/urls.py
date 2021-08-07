from django.conf.urls import url

from .views import (
    WeatherRetrieveAPIView
)

urlpatterns = [
    url(r'^weather/?$', WeatherRetrieveAPIView.as_view()),
    
]
