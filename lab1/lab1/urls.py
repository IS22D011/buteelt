from django.urls import path
from django.contrib import admin
from app import views

urlpatterns = [
    path("admin/",admin.site.urls),
    path("", views.index, name="index"),
    path("contact/", views.index, name="contact"),
    path("resume/", views.index, name="resume"),
    path("project/", views.index, name="project"),
]
