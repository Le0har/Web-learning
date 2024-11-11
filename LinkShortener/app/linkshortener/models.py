from django.db import models


class Links(models.Model):
    full_link = models.CharField(max_length=255, unique=True)
    short_link = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_link
