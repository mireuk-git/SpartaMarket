from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


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
@login_required
def new(request):
    form = ArticleForm()
    context={"form":form}
    return render(request, "articles/new.html",context)

# posting new article, will redirect to posted article`s detail page
@login_required
def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        article = Article(title=title, content=content)
        article.save()
        return redirect("articles:article_detail", article.id)

# show the article`s content`
def article_detail(request, pk):
    # wrong article id given in url
    article = get_object_or_404(Article, pk=pk)
    context = {
        "article": article,
    }
    return render(request, "articles/article_detail.html", context)

# delete current article, redirect to articles list page
@require_http_methods(["POST"])
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    else: return redirect("accounts:login")
    return redirect("articles:articles")

# page for editing current article
@login_required
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context={
        "article": article,
    }
    return render(request, "articles/edit.html", context)

# save the changes of current article, redirect to the article detail page
@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get("title")
    article.content = request.POST.get("content")
    article.save()
    return redirect("articles:article_detail", article.pk)