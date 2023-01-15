import uuid

from django.db import models


# Create your models here.
class Transaction(models.Model):
    """A database model of Bank Account"""

    transaction_id = models.CharField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=2000
    )
    user_id = models.CharField(max_length=2000)
    account_number = models.CharField(max_length=2000)

    transaction_type = models.CharField(max_length=20)
    transaction_amount = models.FloatField()

    # Timestmap
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.transaction_id} - {self.account_number}"
