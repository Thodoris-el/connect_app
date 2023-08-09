from django.urls import path
from .views import CreatePostAPIView, FinaAllView, FindByIdView

urlpatterns = [
    path('create/', CreatePostAPIView.as_view(), name="create"),
    path('findall/', FinaAllView.as_view(), name="find all"),
    path('findid/', FindByIdView.as_view(), name="find by id"),
]
