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
    queryset_list = Article.objects.order_by('-create_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    
    if 'type' in request.GET:
        type = request.GET['type']
        if type:
            queryset_list = queryset_list.filter(type__icontains=type)

    if 'vendor' in request.GET:
        vendor = request.GET['vendor']
        if vendor:
            queryset_list = queryset_list.filter(vendor__icontains=vendor)

    if 'serial' in request.GET:
        serial = request.GET['serial']
        if serial:
            queryset_list = queryset_list.filter(serial__iexact=serial)

    if 'created' in request.GET:
        created = request.GET['created']
        if created:
            queryset_list = queryset_list.filter(create_date__icontains=created)

    context = {
        'articles': queryset_list,
        'values': request.GET

    }

    return render(request, 'articles/search.html', context)
