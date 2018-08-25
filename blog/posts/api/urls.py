from django.urls import path, include
from rest_framework import routers
from .views import (
            PostView,
            PostDetail,
        )
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', PostView.as_view()),
    path('<int:pk>', PostDetail.as_view()),
]

