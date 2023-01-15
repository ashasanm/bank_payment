from django.db.models import Q
from rest_framework import serializers

from .models import Transaction
from .validators import TransactionValidator
from .utils import ServerCommunicationUtils


class TransactionSerializer(serializers.ModelSerializer):
    """Bank Account Serializer Class"""

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

    class Meta:
        """Transaction Meta"""

        model = Transaction
        exclude = ("created_at", "updated_at", "deleted_at")


class UpdateTransactionSerializer(serializers.Serializer):
    TRANSACTION_CHOICE = (("withdraw", "Withdraw"), ("deposit", "Deposit"))
    user_id = serializers.CharField()
    transaction_type = serializers.CharField()
    transaction_amount = serializers.FloatField()

    def validate(self, attrs):
        """Validate data input"""
        # Validate current account balance
        response = ServerCommunicationUtils.get_account_balance(payload={"user_id": attrs["user_id"]})
        if response["status_code"] < 300:
            TransactionValidator.validate_account_balance(response["total_balance"])

        TransactionValidator.validate_decimal(attrs["transaction_amount"])
        if attrs["transaction_type"] == "deposit":
            TransactionValidator.validate_deposit(attrs["transaction_amount"])
        elif attrs["transaction_type"] == "withdraw":
            TransactionValidator.validate_withdraw(attrs["transaction_amount"])
        attrs["transaction_amount"] = TransactionValidator.calculate_withdraw_charge(
            attrs["transaction_amount"]
        )
        return attrs
