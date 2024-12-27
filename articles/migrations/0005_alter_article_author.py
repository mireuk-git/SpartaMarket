# Generated by Django 4.2 on 2024-12-27 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0004_article_liked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(blank=True, default='(알수없음)', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='my_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
