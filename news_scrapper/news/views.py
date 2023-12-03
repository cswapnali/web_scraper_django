from django.shortcuts import render
from .scraper import scrape_news

# Create your views here.
def index(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        if query:
            results = scrape_news(query)
            return render(request, 'news/results.html', {'results': results, 'query': query})

    return render(request, 'news/index.html')
