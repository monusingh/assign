from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add = True)
    movie_descp = models.TextField()
    slug = models.SlugField(max_length=40, unique=True)
    
    def __unicode__(self):
        return self.name

