from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.serializers import ArticleUserSerializer


@api_view(['POST'])
def sign_up(request):
    serializer = ArticleUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
