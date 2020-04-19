from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    article = models.Article.objects.all()
    return render(request, 'index_web/index.html', {'article': article})


def book(request, article_cate):
    article = models.Article.objects.filter(category=article_cate)
    return render(request, 'index_web/book.html', {'article': article})


def tech(request, article_cate):
    article = models.Article.objects.filter(category=article_cate)
    return render(request, 'index_web/tech.html', {'article': article})


def text_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    article.views += 1
    article.save(update_fields=['views'])
    return render(request, 'index_web/pageinfo.html', {"article": article})


def edit_page(request, article_id):
    if str(article_id) == "99999999":
        return render(request, 'index_web/ed_article.html')
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request, 'index_web/ed_article.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    category = request.POST.get('category')
    article_id = request.POST.get('article_id')
    if article_id == '99999999':
        models.Article.objects.create(title=title, content=content, category=category)
        article = models.Article.objects.all()
        return render(request, 'index_web/index.html', {'article': article})
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.category = category
    article.save()
    return render(request, 'index_web/pageinfo.html', {"article": article})







