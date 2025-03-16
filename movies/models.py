from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='названия')
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    video_file = models.FileField(upload_to='movies/', verbose_name='фильм')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title