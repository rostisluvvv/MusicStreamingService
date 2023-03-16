from django.shortcuts import render, get_object_or_404
from django.http import StreamingHttpResponse

from .models import Song, Album, SongWriter


def music_list_page(request):
    albums = Album.objects.all()
    context = {
        'albums': albums,
    }
    template_name = 'music_app/home.html'
    return render(request, template_name, context)


# def music_list_page(request, album_id):
#     albums = Album.objects.get(id=album_id)
#     context = {
#         'albums': albums,
#     }
#     template_name = 'music_app/home.html'
#     return render(request, template_name, context)


def single_music_page(request, pk):
    song = get_object_or_404(Song, id=pk)
    album = song.albums.last()
    template_name = 'music_app/music_page.html'
    context = {
        'song': song,
        'album': album,
    }
    return render(request, template_name, context)
