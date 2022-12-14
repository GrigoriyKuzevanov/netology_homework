# Generated by Django 4.1.3 on 2022-11-17 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                    )
                 ),
                ('title', models.CharField(
                    max_length=256,
                    verbose_name='Название'
                    )
                 ),
                ('text', models.TextField(verbose_name='Текст')),
                ('published_at', models.DateTimeField(
                    verbose_name='Дата публикации'
                        )
                 ),
                ('image', models.ImageField(
                    blank=True,
                    null=True,
                    upload_to='',
                    verbose_name='Изображение'
                    )
                 ),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ['-published_at'],
            },
        ),
        migrations.CreateModel(
            name='ArticleScope',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                    )
                 ),
                ('is_main', models.BooleanField(verbose_name='Основной')),
                ('article', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='scopes',
                    to='articles.article'
                    )
                 ),
            ],
            options={
                'ordering': ['-is_main', 'tag'],
            },
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                    )
                 ),
                ('name', models.CharField(
                    max_length=100,
                    verbose_name='Название'
                    )
                 ),
                ('articles', models.ManyToManyField(
                    through='articles.ArticleScope',
                    to='articles.article'
                        )
                 ),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='articlescope',
            name='tag',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='articles.scope',
                verbose_name='Раздел'
                ),
        ),
    ]
