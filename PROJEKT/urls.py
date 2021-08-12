from django.contrib import admin
from django.urls import path, include
from APP.views import VIEW

urlpatterns = [
    path('', VIEW),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
