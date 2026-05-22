from django.urls import path

from . import views

urlpatterns = [
    path("", views.battles, name="battles"),
    path("<int:article_id>/", views.detail, name="detail"),
]
