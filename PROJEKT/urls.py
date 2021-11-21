from django.contrib import admin
from django.urls import path, re_path, include
from APP.views import foindex, index,valasztas, urlap, nevsor, nemjelentkeztek

urlpatterns = [
    path('', foindex),
    path('tesi/', index),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    re_path(r'tesi/valasztas/.*', valasztas),
    re_path(r'tesi/urlap/.*', urlap),
    re_path(r'tesi/nevsor/.*', nevsor),
    path('tesi/nemjelentkeztek/', nemjelentkeztek),
    path('orarend/', include('APP_orarend.urls')),
]
