from enum import Enum


class TransactionEnum(Enum):
    """Transaction Enum Class"""
    WITHDRAW_MINIMUM = 10
    DEPOSIT_MINIMUM = 500
    DECIMAL_NUMBER_MAX = 2
    MINIMUM_BALANCE = 10
