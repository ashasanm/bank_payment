from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import WrongUserId
from .models import Account
from .serializers import AccountSerializer, BalanceSerializer
from .utils import AccountUtils


# Create your views here.
class AccountView(APIView, AccountUtils):
    """
    View to Manage account in the system.
    """

    serializer_class = AccountSerializer

    def get(self, request, format=None):
        try:
            accounts = Account.objects.all()
            if accounts:
                accounts = self.serializer_class(accounts, many=True).data
                return Response({"accounts": accounts}, status=status.HTTP_200_OK)
            return Response({"accounts": accounts}, status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            error_response = {"msg": "Internal Server Error", "error": str(err)}
            return Response(
                error_response,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def post(self, request, format=None):
        """Return result of account creation"""
        try:
            data = self.create_account_number(request.data)
            serializer = self.serializer_class(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.create(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            error_response = {"msg": "Internal Server Error", "error": str(err)}
            return Response(
                error_response,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class BalanceView(APIView):
    """
    View to Manage balance in the system.
    """

    serializer_class = BalanceSerializer

    def get_queryset(self, account_id) -> object:
        """Function to get Queryset of Account"""
        try:
            account = Account.objects.filter(pk=account_id).values()[0]
            return account
        except IndexError as index_err:
            return None

    def post(self, request, format=None) -> Response:
        """Function to retrive account balance based on user id"""
        try:
            # Get Account detail
            data = self.get_queryset(request.data["user_id"])
            if not data:
                raise WrongUserId

            # Serialize Account data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid(raise_exception=True):
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except WrongUserId as user_id_err:
            return Response(
                WrongUserId.default_detail,
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as err:
            error_response = {"msg": "Internal Server Error", "error": str(err)}
            return Response(
                error_response,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
