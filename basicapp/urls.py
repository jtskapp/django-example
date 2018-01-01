from django.urls import path, re_path, include
from basicapp import views

urlpatterns = [
    re_path(r'^$', views.index, name = 'index'),
    re_path(r'^index/$', views.index, name = 'index'),
    re_path(r'^other/$', views.other, name = 'other'),
    re_path(r'^about/$', views.about, name = 'about'),
]
