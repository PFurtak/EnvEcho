from django.shortcuts import render
from .models import Article

def index(request):
    articles = Article.objects.all()
    
    context = {
        'articles': articles
    }

    return render(request, 'articles/articles.html', context)

def article(request):
    return render(request, 'articles/article.html')

def search(request):
    return render(request, 'articles/search.html')
