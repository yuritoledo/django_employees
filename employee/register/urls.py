from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index),
    path("new", view=views.index, name="new"),
    path("edit", view=views.index, name="edit"),
    path("remove", view=views.index, name="remove"),
]
