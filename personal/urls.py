from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^contact/', views.contact, name='contact'),
    url('^search/', views.search),
]
