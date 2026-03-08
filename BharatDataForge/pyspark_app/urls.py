from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.file_selection_page, name="file_selection_page"),
]