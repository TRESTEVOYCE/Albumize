from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Album(models.Model):
    title = models.CharField(max_length=255,null=False,blank=False)
    artist = models.ForeignKey(User,on_delete=models.CASCADE,related_name='albums',null=False,blank=False)
    release_date = models.DateField(null=False,blank=False )
    cover_image = CloudinaryField('image',folder='album_covers/',null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return f"{self.title} by {self.artist.username}"


class Photo(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos',null=False,blank=False)
    album = models.ForeignKey(Album,related_name='photos',on_delete=models.CASCADE,null=False,blank=False)
    image = CloudinaryField('image',folder='album_photos/',null=False,blank=False)
    caption = models.CharField(max_length=255,blank=True,null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']
    def __str__(self):
        return f"Photo for {self.album.title}"