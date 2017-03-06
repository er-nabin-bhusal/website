from django.contrib import admin
from .models import MatchDate,Photos,Viewers

class MatchDateAdmin(admin.ModelAdmin):
	list_display = ['upcoming_match']

class PhotosAdmin(admin.ModelAdmin):
	list_display = ['user']

class ViewersAdmin(admin.ModelAdmin):
	list_display = ['date','count']
		
# Register your models here.
admin.site.register(MatchDate,MatchDateAdmin)
admin.site.register(Photos,PhotosAdmin)
admin.site.register(Viewers,ViewersAdmin)