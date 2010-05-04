from django.db import models

# Create your models here.
class BlogEntry(models.Model):

    time = models.DateTimeField(auto_now_add=True)
    entry = models.TextField()

class Gallery(models.Model):
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class PortraitGallery(models.Model):
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class ImageRef(models.Model):
    name = models.CharField(max_length=100)
    filename = models.CharField(max_length=300)
    gallery = models.ForeignKey(Gallery)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["filename"]

class PortraitRef(models.Model):
    name = models.CharField(max_length=100)
    filename = models.CharField(max_length=300)
    gallery = models.ForeignKey(PortraitGallery)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["filename"]

class VideoRef(models.Model):
    name = models.CharField(max_length=100)
    filename = models.CharField(max_length=300)
    desc = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["filename"]
