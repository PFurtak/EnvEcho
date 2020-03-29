from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Article


def index(request):
    articles = Article.objects.order_by('-create_date').filter(is_published=True)

    paginator = Paginator(articles, 6)
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)

    
    context = {
        'articles': paged_articles
    }

    return render(request, 'articles/articles.html', context)

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article
    }

    return render(request, 'articles/article.html', context)

def search(request):
    return render(request, 'articles/search.html')
