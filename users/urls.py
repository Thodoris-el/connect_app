from django.urls import path
from .views import CreateUserAPIView, GetAllUser, SearchUserByName, SearchUserByAge, SearchCustom, LoginView, UpdateView, DeleteView, EnableView

urlpatterns = [
    path('create/', CreateUserAPIView.as_view(), name="create"),
    path('allusers/', GetAllUser.as_view(), name="all users"),
    path('filter/', SearchUserByName.as_view(), name="filter"),
    path('filterb/', SearchUserByAge.as_view(), name="filter age"),
    path('filterall/', SearchCustom.as_view(), name="filter custom"),
    path('login/', LoginView.as_view(), name="login"),
    path('update/', UpdateView.as_view(), name="update"),
    path('delete/', DeleteView.as_view(), name="delete"),
    path('enable/', EnableView.as_view(), name="enable"),
]