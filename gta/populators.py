from django_faker import Faker
from news.models import News
from django.conf import settings


def populate_news(**kwargs):
	if settings.DEBUG:
		News.objects.all().delete()

		populator = Faker.getPopulator()
		populator.addEntity(News, 23, {
				'link': lambda x: populator.generator.url()
			})

		populator.execute()
		print("Populated sample news data..")