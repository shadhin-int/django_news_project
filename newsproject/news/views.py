from django.shortcuts import render
from newsapi import NewsApiClient


def index(request):
	newsapi = NewsApiClient(api_key='cb8bca17789d40578a5c1b83184006f7')
	top = newsapi.get_top_headlines(sources='techcrunch')

	lm = top['articles']
	desc = []
	news = []
	img = []

	for i in range(len(lm)):
		f = lm[i]
		news.append(f['title'])
		desc.append(f['description'])
		img.append(f['urlToImage'])
	mylist = zip(news, desc, img)

	return render(request, 'index.html', context={"mylist": mylist})
