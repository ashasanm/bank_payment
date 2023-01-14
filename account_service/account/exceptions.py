from rest_framework import status
from rest_framework.exceptions import APIException

from .enums import DepositAmountEnum


class AlreadyExist(APIException):
    """Exception handler for same phone number or tax id"""

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {
        "msg": "Phone Number or Tax Id is already Taken",
        "code": "already_exist",
        "status_code": status.HTTP_400_BAD_REQUEST,
    }
    default_code = "already_exist"


class InvalidTaxId(APIException):
    """Exception handler for tax id length"""

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {
        "msg": "Tax id length must be 6",
        "code": "invalid_tax_id_length",
        "status_code": status.HTTP_400_BAD_REQUEST,
    }
    default_code = "invalid_tax_id_length"


class LowInitalDeposit(APIException):
    """Exception handler for initial deposit does not meet requirement"""

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {
        "msg": f"Initial Deposit should bigger than {DepositAmountEnum.DEPOSIT_MINIMUM.value}",
        "code": "low_inital_deposit",
        "status_code": status.HTTP_400_BAD_REQUEST,
    }
    default_code = "low_inital_deposit"


class WrongUserId(APIException):
    """Exception handler for initial deposit does not meet requirement"""

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {
        "msg": "Wrong User Id",
        "code": "wrong_user_id",
        "status_code": status.HTTP_400_BAD_REQUEST,
    }
    default_code = "wrong_user_id"
