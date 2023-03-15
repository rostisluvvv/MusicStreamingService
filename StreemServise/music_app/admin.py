from django.contrib import admin

from .models import Music


class MusicAdmin(admin.ModelAdmin):
    list_display = ('pk', 'song_title', 'songwriter')
    list_display_links = ('song_title', 'songwriter')
    empty_value_display = '-пусто-'


admin.site.register(Music, MusicAdmin)
