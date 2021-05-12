from django.db import models


class checker(models.Model):
    active = models.CharField(null=True, blank=True, default="on", max_length=6)

    def __str__(self):
        return 'camera_off_on'


class camera(models.Model):
    image = models.FileField(blank=True, null=True, upload_to='camera_video/')

    def __str__(self):
        return 'camera'
