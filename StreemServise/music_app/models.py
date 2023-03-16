from django.db import models
from django.core.validators import FileExtensionValidator


class SongWriter(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='song_writer_image/%Y/%m/%d/',
                              blank=True,
                              null=True)


class Song(models.Model):
    song_title = models.CharField(max_length=100)
    song_writer = models.ForeignKey(SongWriter,
                                    on_delete=models.CASCADE,
                                    related_name='song',
                                    verbose_name='songwriter',
                                    max_length=100)
    file = models.FileField(
        upload_to='music/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=['mp3'])]
    )
    image = models.ForeignKey('Album', on_delete=models.CASCADE)

    def __str__(self):
        return self.song_title

    class Meta:
        ordering = ['-release_date']


class Album(models.Model):
    album_title = models.CharField(max_length=100)
    song_writer = models.ForeignKey(SongWriter,
                                    related_name='song_writer',
                                    on_delete=models.CASCADE)
    file = models.ForeignKey(Song,
                             related_name='song',
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='song_image/%Y/%m/%d/')
    release_date = models.DateTimeField(auto_now_add=True)
