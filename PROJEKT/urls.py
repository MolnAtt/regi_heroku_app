from django.contrib import admin
from django.urls import path, re_path, include
from APP.views import foindex, index,valasztas, urlap, nevsor, nemjelentkeztek

urlpatterns = [
    path('', foindex),
    path('tesi/', index),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('tesi/valasztas/<str:szurestipus>/', valasztas),
    path('tesi/valasztas/', valasztas),
    path('tesi/urlap/<str:melyik>/', urlap),
    path('tesi/nevsor/<str:a_kod>/', nevsor),
    path('tesi/nemjelentkeztek/', nemjelentkeztek),
    path('orarend/', include('APP_orarend.urls')),
]
