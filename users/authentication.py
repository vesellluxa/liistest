from django.core.exceptions import ObjectDoesNotExist
from rest_framework import authentication, exceptions

from api.models import ArticleUser


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        email = request.headers.get('email')
        password = request.headers.get('password')
        if not email or not password:
            return None
        try:
            user = ArticleUser.objects.get(email=email)
        except ObjectDoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        if user.check_password(password) and user.is_active:
            return user, None
