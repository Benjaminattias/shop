from django.db import models


class Contact(models.Model):
    subject = models.CharField(max_length=264)
    email = models.EmailField(max_length=264)
    text = models.TextField(max_length=264)


