from django.db import models
from django.core.validators import FileExtensionValidator


class Music(models.Model):
    song_title = models.CharField(max_length=100)
    songwriter = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/%Y/%m/%d/')
    file = models.FileField(
        upload_to='music/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=['mp3'])]
    )
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.song_title

    class Meta:
        ordering = ['-release_date']
