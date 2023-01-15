from django.db.models import Q

from .enums import TransactionEnum
from .exceptions import LowDepositAmount, LowWithdrawAmount, DecimalExceed, LowBalance


class TransactionValidator:
    """Transaction Validator"""

    @classmethod
    def validate_decimal(cls, value):
        """Validate decimal in transaction amount
        validation: max two digits after decimal points
        """
        decimalpoint = str(value).split('.')[1]
        if int(decimalpoint) > 2:
            raise DecimalExceed

    @classmethod
    def validate_deposit(cls, value):
        """Validate deposit amount
        validation: deposit amount should higher than deposit minimum
        """
        if value < TransactionEnum.DEPOSIT_MINIMUM.value:
            raise LowDepositAmount

    @classmethod
    def validate_withdraw(cls, value):
        """Validate withdraw amount
        validation: withdraw amount should higher than deposit minimum
        """
        if value < TransactionEnum.WITHDRAW_MINIMUM.value:
            raise LowWithdrawAmount

    @classmethod
    def validate_account_balance(cls, value):
        if value < TransactionEnum.MINIMUM_BALANCE.value:
            raise LowBalance

    @classmethod
    def calculate_withdraw_charge(cls, value):
        """Calculate withdraw charge
        In between 0-500 -> 0
        In between 501-5000 -> 10
        5001 and above -> 20
        """
        if 500 > value > 0:
            return value

        if 5000 > value > 501:
            value += 10
        else:
            value += 20
        return value
