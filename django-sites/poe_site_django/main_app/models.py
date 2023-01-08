from django.db import models


class StarterListDescription(models.Model):
    title = models.CharField(max_length=50)
    ascendancy = models.CharField(max_length=20)
    main_skill = models.CharField(max_length=50)
    description_build = models.TextField()
    survivability = models.CharField(max_length=20)
    img_character = models.ImageField(upload_to='character/%Y/%m/%d/')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title





