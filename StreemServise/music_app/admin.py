from django.contrib import admin

from .models import Song, SongWriter, Album


class SongWriterAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'image')
    list_display_links = ('name',)
    empty_value_display = '-пусто-'


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('pk', 'album_title', 'song_writer')
    list_display_links = ('album_title',)
    empty_value_display = '-пусто-'


class SongAdmin(admin.ModelAdmin):
    list_display = ('pk', 'song_title', 'song_writer')
    list_display_links = ('song_title', 'song_writer')
    empty_value_display = '-пусто-'


admin.site.register(Album, AlbumAdmin)
admin.site.register(SongWriter, SongWriterAdmin)
admin.site.register(Song, SongAdmin)
