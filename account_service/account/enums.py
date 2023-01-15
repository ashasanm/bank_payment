from enum import Enum


class DepositAmountEnum(Enum):
    """Deposit Amount Enum"""

    DEPOSIT_MINIMUM = 5000

class TaxEnum(Enum):
    """Tax Enum"""
    TAX_ID_LENGTH = 6

class BalanceEnum(Enum):
    """BALANCE ENUM"""
    MINIMUM_BALANCE = 10