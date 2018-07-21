from django.contrib import admin
from django.urls import path, include
from core.views import main

urlpatterns = [
    path('', main),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls'))
]
