from api.models import Article, ArticleUser
from django.contrib import admin


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleUser, ArticleAdmin)
