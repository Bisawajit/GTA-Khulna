from django.db import models
from django.conf import settings

class News(models.Model):
	title = models.CharField(max_length=200)
	link = models.URLField()
	description = models.TextField()
	is_approved = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title[0:25]	+ "..."

	class Meta:
		verbose_name_plural = "News"
