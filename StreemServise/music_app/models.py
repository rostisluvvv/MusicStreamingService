from django.db import models
from django.core.validators import FileExtensionValidator


class SongWriter(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='song_writer_image/%Y/%m/%d/',
                              blank=True,
                              null=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    song_title = models.CharField(max_length=100)
    song_writer = models.ForeignKey(SongWriter,
                                    on_delete=models.CASCADE,
                                    related_name='songs',
                                    verbose_name='songwriter')
    file = models.FileField(
        upload_to='music/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=['mp3'])]
    )

    def __str__(self):
        return self.song_title


class Album(models.Model):
    album_title = models.CharField(max_length=100)
    song_writer = models.ForeignKey(SongWriter,
                                    related_name='albums',
                                    on_delete=models.CASCADE)

    image = models.ImageField(upload_to='song_image/%Y/%m/%d/')
    release_date = models.DateTimeField(auto_now_add=True)
    songs = models.ManyToManyField(Song, related_name='albums')

    def __str__(self):
        return self.album_title

    class Meta:
        ordering = ['-release_date']
