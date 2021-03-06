from django.db import models

from users.models import ArticleUser


class Article(models.Model):
    title = models.CharField('Article title', max_length=256,
                             null=False, blank=False)
    text = models.CharField('Article text', max_length=2000,
                            null=False, blank=False)
    author = models.ForeignKey(to=ArticleUser, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Publication date', auto_now_add=True)
    is_private = models.BooleanField(default=False, db_index=True)
