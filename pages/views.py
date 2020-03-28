from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article



def index(request):
    articles = Article.objects.order_by('-create_date').filter(is_published=True)[:3]

    context = {
        'articles': articles
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
