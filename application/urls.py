from django.urls import path
from . import views


urlpatterns = [
    path('authenticated/', views.Authenticated),
    path('create/', views.create),
]