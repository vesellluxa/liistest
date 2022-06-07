from django.urls import include, path
from rest_framework import routers

from api.views import ArticleView, sign_up

router_v1 = routers.DefaultRouter()
router_v1.register('articles', ArticleView, basename='articles')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/signup/', sign_up)
]
