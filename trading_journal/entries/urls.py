from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.EntryView.as_view()),
    path("entries/<int:id>", views.SingleEntryView.as_view(), name="single-entry"),
    path("admin", admin.site.urls)
]