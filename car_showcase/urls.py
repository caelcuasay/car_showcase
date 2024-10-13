from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('porsche/', include('porsche.urls')),
    path('gtr/', include('gtr.urls')),
    path('', include('gtr.urls')),
]
