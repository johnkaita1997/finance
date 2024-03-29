# urls.py

from django.urls import path

from .views import *

urlpatterns = [
    path('create', GrantCreateView.as_view(), name="grant-create"),
    path('list', GrantListView.as_view(), name="grant-list"),
    path('<str:pk>', GrantDetailView.as_view(), name="grant-detail")
]
