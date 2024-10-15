from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
from .models import Transaction
from .serializers import TransactionSerializer

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def create_transaction(request):
    user = request.user
    amount = request.data.get('amount')

    transaction = Transaction.objects.create(user=user, amount=amount)
    return Response({'message': 'Transaction created successfully'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_transactions(request):
    user = request.user
    transactions = Transaction.objects.filter(user=user)
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
