from rest_framework import serializers

from api.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=256, required=True)
    text = serializers.CharField(max_length=2000, required=True)
    author = serializers.CharField(max_length=150, required=False)

    class Meta:
        model = Article
        fields = ('title', 'text', 'author', 'pub_date', 'is_private', 'pk')
