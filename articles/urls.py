from django.urls import path
from . import views

app_name="articles"
urlpatterns = [
    path("", views.articles, name="articles"),
    path("<int:pk>/", views.article_detail, name="article_detail"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/edit",views.edit,name="edit"),
    path("<int:pk>/update/", views.update, name="update"),
]