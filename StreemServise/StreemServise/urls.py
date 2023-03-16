from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include(('music_app.urls', 'music_app'), namespace='music_app')),
    path('admin/', admin.site.urls),
]
