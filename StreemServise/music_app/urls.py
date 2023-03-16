from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_mame = 'music_app'

urlpatterns = [
    # path('album/<album.id>/', views.single_music_page, name='album'),
    path('album/<int:pk>/', views.single_music_page, name='album'),
    path('', views.music_list_page, name='home'),

]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)