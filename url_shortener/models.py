from django.db import models


class Url(models.Model):
    short_url = models.CharField(max_length=75)
    long_url = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.short_url
