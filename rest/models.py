from django.db import models


class camera(models.Model):
    active = models.CharField(null=True, blank=True, default="hello", max_length=6)
    image = models.FileField(blank=True, null=True, upload_to='camera_video/')

    def __str__(self):
        return 'camera'
