from django.contrib import admin
from .models import Flag, Color, FavoriteFlag, FavoriteColor

admin.site.register(Flag)
admin.site.register(Color)
admin.site.register(FavoriteFlag)
admin.site.register(FavoriteColor)

# Register your models here.
