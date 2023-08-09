from django.urls import path
from .views import CreatePostAPIView, FinaAllView, FindByIdView, FindByUserView, LikePostView, DislikePostView, Top100View, FindByDateView, FindByLocationView

urlpatterns = [
    path('create/', CreatePostAPIView.as_view(), name="create"),
    path('findall/', FinaAllView.as_view(), name="find all"),
    path('findid/', FindByIdView.as_view(), name="find by id"),
    path('finduser/', FindByUserView.as_view(), name="find by user id"),
    path('like/', LikePostView.as_view(), name="like post"),
    path('dislike/', DislikePostView.as_view(), name="dislike post"),
    path('top100/', Top100View.as_view(), name="top 100 posts"),
    path('finddate/', FindByDateView.as_view(), name="find by date"),
    path('findlocation/', FindByLocationView.as_view(), name="find by location"),
]
