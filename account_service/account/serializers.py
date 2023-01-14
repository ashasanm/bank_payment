from django.db.models import Q
from rest_framework import serializers

from .models import Account
from .validators import AccountValidator


class AccountSerializer(serializers.ModelSerializer):
    """Bank Account Serializer Class"""

    def validate(self, data):
        """Validate data input"""
        AccountValidator.check_account_phone_and_tax(
            phone_number=data["phone_number"], tax_id=data["tax_id"]
        )

        return data

    def create(self, validated_data):
        """Save validated data"""
        return Account.objects.create(**validated_data)

    class Meta:
        """DB Model META"""

        model = Account
        exclude = ("created_at", "updated_at", "deleted_at")


class BalanceSerializer(serializers.ModelSerializer):
    """Serializer Bank Account Balance"""

    class Meta:
        """DB Model META"""

        model = Account
        exclude = ("created_at", "updated_at", "deleted_at")

    def to_representation(self, data):
        """Reformat Account data format"""
        account_detail = {
            "total balance": data["deposit_amount"],
            "name": data["name"],
            "email": data["email_address"],
            "address": data["address"],
            "phone_number": data["phone_number"],
        }
        return account_detail
