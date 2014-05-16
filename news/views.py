from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.paginator import Paginator
from news.forms import NewsForm
from news.models import News

class CreateNews(View):
	def post(self, request):
		form = NewsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/news')

		return render(request, "news/news_form.html", {
				"form" : form
			})

	def get(self, request):
		form = NewsForm()
		return render(request, "news/news_form.html", {
				"form" : form
			})


class ListNews(View):
	def get(self, request, page=1):
		all_news = News.objects.all()#filter(is_approved=True)
		paginator = Paginator(all_news, 10)

		try:
			news = paginator.page(page)
		except PageNotAnInteger:
			news = paginator.page(1)
		except EmptyPage:
			news = paginator.page(paginator.num_pages)

		return render(request, "news/news_list.html", {
       			"news": news,
       			"paginator": paginator
       		})