from rest_framework import routers

from api.views import ArticleView


router = routers.DefaultRouter()

router.register('articles', ArticleView, basename='articles')

urlpatterns = []

urlpatterns += router.urls
