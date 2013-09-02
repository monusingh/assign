import models
from django.contrib import admin



class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(models.Movie, MovieAdmin)



