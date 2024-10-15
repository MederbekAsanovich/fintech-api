from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from .views import register, create_transaction, get_transactions

urlpatterns += [
    path('register/', register, name='register'),
    path('transactions/', create_transaction, name='create_transaction'),
    path('transactions/all/', get_transactions, name='get_transactions'),
]
