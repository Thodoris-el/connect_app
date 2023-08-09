from django.urls import path
from .views import CreateUserAPIView, GetAllUser, SearchUserByName, SearchUserByAge, SearchCustom

urlpatterns = [
    path('create/', CreateUserAPIView.as_view(), name="create"),
    path('allusers/', GetAllUser.as_view(), name="all users"),
    path('filter/', SearchUserByName.as_view(), name="filter"),
    path('filterb/', SearchUserByAge.as_view(), name="filter"),
    path('filterall/', SearchCustom.as_view(), name="filter"),
]