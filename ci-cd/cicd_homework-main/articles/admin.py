from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope


class ArticleScopeInLineFormset(BaseInlineFormSet):
    def clean(self):
        c = 0
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['is_main']:
                c += 1
            else:
                continue
        if c == 0:
            raise ValidationError('Не указан основной tag!')
        if c > 1:
            raise ValidationError('Основной tag может быть только один!')
        else:
            return super().clean()


class ArticleScopeInLine(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInLineFormset
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at']
    inlines = [ArticleScopeInLine]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['name']
