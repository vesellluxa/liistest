from rest_framework.viewsets import ModelViewSet

from api.models import Article
from api.permissions import IsAuthorOrReadOnly
from api.serializers import ArticleSerializer


class ArticleView(ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Article.objects.all()
        return Article.objects.filter(is_private=False)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
