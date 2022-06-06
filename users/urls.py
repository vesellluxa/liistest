from django.urls import path

from users.views import sign_up

urlpatterns = [
    path('v1/signup/', sign_up)
]
