from django.db.models.signals import post_syncdb
import news.models
from gta.populators import populate_news

post_syncdb.connect(populate_news, sender=news.models)
