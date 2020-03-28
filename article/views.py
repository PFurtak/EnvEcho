from django.shortcuts import render
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
    return render(request, 'articles/article.html')

def search(request):
    return render(request, 'articles/search.html')
