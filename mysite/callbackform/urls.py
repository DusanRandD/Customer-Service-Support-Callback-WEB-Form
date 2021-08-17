from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_callback_form),
    path('confirmation/',views.display_confirmation),
]