from django.urls import path

from users.views import sign_up

urlpatterns = [
    path('signup/', sign_up)
]
