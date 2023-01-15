from rest_framework import status
from rest_framework.exceptions import APIException

from .enums import TransactionEnum


class LowDepositAmount(APIException):
    """Exception handler for initial deposit does not meet requirement"""

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {
        "msg": f"Deposit amount should bigger than {TransactionEnum.DEPOSIT_MINIMUM.value}",
        "code": "low_deposit_amount",
        "status_code": status.HTTP_400_BAD_REQUEST,
    }
    default_code = "low_deposit_amount"


class LowWithdrawAmount(APIException):
    """Exception handler for initial withdraw does not meet requirement"""

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {
        "msg": f"withdraw amount should bigger than {TransactionEnum.DEPOSIT_MINIMUM.value}",
        "code": "low_withdraw_amount",
        "status_code": status.HTTP_400_BAD_REQUEST,
    }
    default_code = "low_withdraw_amount"


class DecimalExceed(APIException):
    """Exception handler for maximum decimal number exceed maximum"""

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {
        "msg": f"Maximum decimal number is {TransactionEnum.DECIMAL_NUMBER_MAX.value}",
        "code": "decimal_exceed",
        "status_code": status.HTTP_400_BAD_REQUEST,
    }
    default_code = "decimal_exceed"


class LowBalance(APIException):
    """Exception handler for maximum decimal number exceed maximum"""

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {
        "msg": f"You cannot with drow with balance lower than {TransactionEnum.MINIMUM_BALANCE.value}",
        "code": "low_balance",
        "status_code": status.HTTP_400_BAD_REQUEST,
    }
    default_code = "low_balance"
