from rest_framework import permissions

from api.models import ArticleUser


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated
                    and request.user.role == ArticleUser.AUTHOR)
                or request.user.is_authenticated
                and request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        return ((request.method in permissions.SAFE_METHODS)
                or (request.user == obj.author)
                or (request.user.is_authenticated
                and request.user.is_superuser)
                )
