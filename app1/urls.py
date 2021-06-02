from django.urls import path
from app1 import views
urlpatterns = [
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("hours/", views.hours, name="hours"),
    path("gallery/", views.about, name="gallery"),
    path("booking/", views.about, name="booking"),
    path("contact/", views.contact, name="contact"),
]