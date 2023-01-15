from django.db.models import Q
from rest_framework import serializers

from .models import Account
from .validators import AccountValidator


class AccountSerializer(serializers.ModelSerializer):
    """Bank Account Serializer Class"""

    class Meta:
        """DB Model META"""

        model = Account
        exclude = ("created_at", "updated_at", "deleted_at")


class CreateAccountSerializer(serializers.ModelSerializer):
    """Create bank Account Serializer Class"""

    deposit_amount = serializers.FloatField()

    def validate(self, attrs):
        """Validate data input"""
        AccountValidator.check_account_phone_and_tax(
            phone_number=attrs["phone_number"], tax_id=attrs["tax_id"]
        )

        return attrs

    def create(self, validated_data):
        """Save validated data"""
        # Remove deposit amount when creating account
        validated_data["total_balance"] = validated_data["deposit_amount"]
        validated_data.pop("deposit_amount")
        return Account.objects.create(**validated_data)

    class Meta:
        """DB Model META"""

        model = Account
        exclude = ("created_at", "updated_at", "deleted_at", "total_balance")


class BalanceSerializer(serializers.ModelSerializer):
    """Serializer Bank Account Balance"""

    class Meta:
        """DB Model META"""

        model = Account
        exclude = ("created_at", "updated_at", "deleted_at")

    def to_representation(self, data):
        """Reformat Account data format"""
        account_detail = {
            "total balance": data["total_balance"],
            "name": data["name"],
            "email": data["email_address"],
            "address": data["address"],
            "phone_number": data["phone_number"],
        }
        return account_detail


class BalanceUpdateSerializer(serializers.Serializer):
    """Serializer to update Bank Account Balance"""

    TRANSACTION_TYPE_CHOICES = (
        ("withdraw", "Withdraw"),
        ("deposit", "Deposit"),
    )
    user_id = serializers.CharField()
    transaction_type = serializers.ChoiceField(choices=TRANSACTION_TYPE_CHOICES)
    transaction_amount = serializers.FloatField()

    def update(self, instance, validated_data):
        # Serialize Account data
        if validated_data["transaction_type"] == "withdraw":
            instance.total_balance -= validated_data["transaction_amount"]
        elif validated_data["transaction_type"] == "deposit":
            instance.total_balance += validated_data["transaction_amount"]
        instance.name = validated_data.get("balance", instance.name)
        return instance


class AccountBalanceSerializer(serializers.ModelSerializer):
    """Bank Account Serializer Class"""

    def create(self, validated_data):
        """Save validated data"""
        return Account.objects.create(**validated_data)

    class Meta:
        """DB Model META"""

        model = Account
        fields = ("user_id", "account_number", "name", "total_balance")
