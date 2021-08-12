from django.contrib import admin
from django.urls import path
from APP.views import VIEW
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', VIEW),
]
