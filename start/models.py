from django.db import models

# Create your models here.


class Card(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    img = models.ImageField(upload_to="image/")
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"