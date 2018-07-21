from django.contrib import admin
from django.urls import path
from core.views import main

urlpatterns = [
    path('', main),
    path('admin/', admin.site.urls),
]
