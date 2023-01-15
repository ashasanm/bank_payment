import account.models
from django.db.models import Q

from .enums import DepositAmountEnum, TaxEnum, BalanceEnum
from .exceptions import AlreadyExist, InvalidTaxId, LowInitalDeposit, LowBalance

class AccountValidator:
    """Account Validator"""

    @classmethod
    def validate_inital_deposit(cls, value):
        """Validate intial account deposit"""
        if value < DepositAmountEnum.DEPOSIT_MINIMUM.value:
            raise LowInitalDeposit()
        return value

    @classmethod
    def validate_tax_id(cls, value):
        """validate tax id"""
        if len(value) != TaxEnum.TAX_ID_LENGTH.value:
            raise InvalidTaxId()
        return value

    @classmethod
    def check_account_phone_and_tax(cls, phone_number: str, tax_id: str) -> object:
        """Function to check if phone number or tax id is already exist in database"""
        try:
            account.models.Account.objects.get(
                Q(phone_number=phone_number) | Q(tax_id=tax_id)
            )
            raise AlreadyExist
        except account.models.Account.DoesNotExist:
            return None
    
    @classmethod
    def validate_account_balance(cls, value):
        if value < BalanceEnum.MINIMUM_BALANCE.value:
            raise LowBalance
