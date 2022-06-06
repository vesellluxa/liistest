from rest_framework import routers

from api.views import ArticleView


router_v1 = routers.DefaultRouter()
router_v1.register('articles', ArticleView, basename='articles')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
