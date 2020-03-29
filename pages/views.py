from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from techs.models import Tech



def index(request):
    articles = Article.objects.order_by('-create_date').filter(is_published=True)[:3]

    context = {
        'articles': articles
    }

    return render(request, 'pages/index.html', context)

def about(request):
    techs = Tech.objects.order_by('-hire_date')

    context = {
        'techs': techs,
    }

    return render(request, 'pages/about.html', context)
