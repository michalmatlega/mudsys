from django.db import models

class FileManager(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank = True)
    creation_date = models.DateTimeField(auto_now_add=True)
    folder = models.FileField(upload_to="media/")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']