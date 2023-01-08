from django.db import models

# Create your models here.


class Women(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    id_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

