from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='gtr_landing_page'),  # Landing page URL
    path('index/', views.index, name='gtr_index'),         # Index page URL
    path('gallery/', views.gallery, name='gtr_gallery'),     # Gallery page URL
    path('specs/', views.specs, name='gtr_specs'),         # Specs page URL
]
