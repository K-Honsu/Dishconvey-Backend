from django.urls import path
from djoser.views import TokenCreateView, TokenDestroyView

urlpatterns = [
    path('token/login/', TokenCreateView.as_view(), name='login'),
    path('logout/', TokenDestroyView.as_view(), name='logout'),
]
