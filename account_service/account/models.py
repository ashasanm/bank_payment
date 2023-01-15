import uuid

from django.db import models

from .validators import AccountValidator

class Account(models.Model):
    """A database model of Bank Account"""

    user_id = models.CharField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=2000
    )
    account_number = models.CharField(max_length=200)
    name = models.CharField(max_length=25)
    total_balance = models.FloatField()
    phone_number = models.CharField(max_length=30)
    tax_id = models.CharField(
        max_length=6, validators=[AccountValidator.validate_tax_id]
    )
    email_address = models.EmailField()
    address = models.CharField(max_length=200)

    # Timestmap
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} - {str(self.phone_number)} - {self.email_address}"
