from django.shortcuts import render
import requests
import json
from django.conf import settings

def news_list(request):
    api_key = '6d897a0909b946059f456926072b159a'
    search_query = request.GET.get('search', '')  # Get the search query from the request

    # If there's no search query, display general news
    if not search_query:
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'  # You can specify a country code or remove the 'country' parameter
    else:
        url = f'https://newsapi.org/v2/everything?q={search_query}&apiKey={api_key}'

    response = requests.get(url)
    data = json.loads(response.text)
    articles = data.get('articles', [])
    return render(request, 'news.html', {'articles': articles, 'search_query': search_query})
