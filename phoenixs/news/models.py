from django.db import models


class News(models.Model):
    poster = models.ImageField(null=True, blank=True, upload_to='news/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=128, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title