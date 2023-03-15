from django.shortcuts import render, get_object_or_404
from django.http import StreamingHttpResponse

from .models import Music


def music_list_page(request):
    template_name = 'music_app/home.html'
    context = {'music_list': Music.objects.all()}
    return render(request, template_name, context)


def single_music_page(requesr, pk):
    music = get_object_or_404(Music, id=pk)
    template_name = 'music_app/music.html'
    context = {'music': music}
    return render(requesr, template_name, context)
