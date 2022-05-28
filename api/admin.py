from django.contrib import admin

from api.models import Article, ArticleUser


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleUser, ArticleAdmin)
