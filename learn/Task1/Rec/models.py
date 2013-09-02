from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=64)
    details = models.TextField()
    slug = models.SlugField(max_length=40, unique=True)
    
    def __unicode__(self):
        return self.name

