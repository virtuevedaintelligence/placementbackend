from django.urls import path, include, re_path
from entity import views

urlpatterns = [
    re_path(r'^entity$', views.entityApi),
    re_path(r'^entity/([0-9]+)$', views.entityApi)
]