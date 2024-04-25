from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.EntryView.as_view(), name="index"),
    path("entries/<int:pk>/delete", views.SingleEntryDeleteView.as_view(), name="single-entry-delete"),
    path("entries/<int:pk>/", views.SingleEntryView, name="single-entry"),
    path("register/", views.register, name="register"),
    path("admin/", admin.site.urls)
]
