from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    return render(request, "articles/index.html")

# default page, list all articles
def articles(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "articles/articles.html", context)

# page for writing a new article
def new(request):
    form = ArticleForm()
    context={"form":form}
    return render(request, "articles/new.html",context)

# posting new article, will redirect to posted article`s detail page
def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")

    article = Article(title=title, content=content)
    article.save()
    return redirect("articles:article_detail", article.id)

# show the article`s content`
def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article": article,
    }
    return render(request, "articles/article_detail.html", context)

# delete current article, redirect to articles list page
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect("articles:articles")
    return redirect("articles:articles")

# page for editing current article
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context={
        "article": article,
    }
    return render(request, "articles/edit.html", context)

# save the changes of current article, redirect to the article detail page
def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get("title")
    article.content = request.POST.get("content")
    article.save()
    return redirect("articles:article_detail", article.pk)