from django.contrib import admin
from django.urls import path, re_path, include
from APP.views import index,valasztas, urlap

urlpatterns = [
    path('', index),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    re_path(r'valasztas/.*', valasztas),
    re_path(r'urlap/.*', urlap),
]
