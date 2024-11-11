from django.contrib import admin
from django.urls import path
from linkshortener.views import LinksAPIView


urlpatterns = [
    path('', LinksAPIView.as_view(), name='home'),
    path('<int:link_id>', LinksAPIView.as_view(), name='link-id'),
]
