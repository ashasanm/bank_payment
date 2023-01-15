from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import DecimalExceed, LowDepositAmount, LowWithdrawAmount, LowBalance
from .serializers import TransactionSerializer, UpdateTransactionSerializer
from .utils import ServerCommunicationUtils


# Create your views here.
class TransactionView(APIView, ServerCommunicationUtils):
    serializer_class = TransactionSerializer
    update_serializer = UpdateTransactionSerializer

    def post(self, request, format=None):
        """Return User Transaction Detail"""
        try:
            update_serializer = self.update_serializer(data=request.data)
            if update_serializer.is_valid(raise_exception=True):
                # Communicate with account service to update balance
                update_response = self.update_account_balance(
                    payload=update_serializer.data
                )
                if update_response["status_code"] > 300:
                    return Response(
                        update_response, status=update_response["status_code"]
                    )
                update_response.update(request.data)

            serializer = self.serializer_class(data=update_response)
            if serializer.is_valid(raise_exception=True):
                serializer.create(serializer.data)
                return Response(update_response, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DecimalExceed as err:
            return Response(err.default_detail, status=err.status_code)
        except LowWithdrawAmount as err:
            return Response(err.default_detail, status=err.status_code)
        except LowDepositAmount as err:
            return Response(err.default_detail, status=err.status_code)
        except LowBalance as err:
            return Response(err.default_detail, status=err.status_code)
        except Exception as err:
            error_response = {"msg": "Internal Server Error", "error": str(err)}
            return Response(
                error_response,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
