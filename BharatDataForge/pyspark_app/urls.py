from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.run_pipeline, name="run_pipeline"),
]