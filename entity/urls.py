from django.conf.urls import url
from entity import views

urlpatterns = [
    url(r'^entity$', views.entityApi),
    url(r'^entity/([0-9]+)$', views.entityApi())
]