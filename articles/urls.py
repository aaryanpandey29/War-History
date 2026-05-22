from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="battles"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]
