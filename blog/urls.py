from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page),
    path('about/',views.about_page),
    path('interests/',views.interest_page),
    path('contact/',views.contact_page),
]