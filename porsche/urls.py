from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='porsche_index'),
    path('gallery/', views.gallery, name='porsche_gallery'),
    path('specs/', views.specs, name='porsche_specs'),
]
