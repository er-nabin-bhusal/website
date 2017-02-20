from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MatchDate(models.Model):
	upcoming_match = models.DateField(null=True)
	match_link = models.URLField(max_length=200,null=True)
	match_time = models.TimeField(null=True)

	def __str__(self):
		return('{}'.format(self.upcoming_match))


class Photos(models.Model):
	user = models.ForeignKey(MatchDate,on_delete=models.CASCADE)
	image = models.ImageField(upload_to='profileimage/',null=True,blank=True)

	def __str__(self):
		return ('{}'.format(self.user))