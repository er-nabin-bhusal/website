from django.contrib import admin
from .models import MatchDate,Photos

class MatchDateAdmin(admin.ModelAdmin):
	list_display = ['upcoming_match']

class PhotosAdmin(admin.ModelAdmin):
	list_display = ['user']


# Register your models here.
admin.site.register(MatchDate,MatchDateAdmin)
admin.site.register(Photos,PhotosAdmin)