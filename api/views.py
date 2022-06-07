from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import Article
from api.permissions import IsAuthorOrReadOnly
from api.serializers import ArticleSerializer, ArticleUserSerializer


class ArticleView(ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Article.objects.all()
        return Article.objects.filter(is_private=False)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(['POST'])
def sign_up(request):
    serializer = ArticleUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
