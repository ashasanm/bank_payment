import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Account

# Create your tests here.
class AccountTest(APITestCase):
    """Test Case for Account Service"""

    TRANSACTION_URL = "http://localhost:8000/api/account/"
    BASE_PAYLOAD = {
        "name": "",
        "deposit_amount": 5000.0,
        "phone_number": "",
        "tax_id": "",
        "email_address": "email@gmail.com",
        "address": "address",
    }

    def test_create_account(self):
        """Function to test account creation expected to be success"""
        self.BASE_PAYLOAD["name"] = "test1"
        self.BASE_PAYLOAD["phone_number"] = "08539209999"
        self.BASE_PAYLOAD["tax_id"] = "123321"

        response = self.client.post(
            path=self.TRANSACTION_URL,
            data=json.dumps(self.BASE_PAYLOAD),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

    def test_create_account_with_same_phone_or_tax(self):
        """Function to test account creation expected to be success"""
        mock_data = {
            "name": "TEST",
            "total_balance": 5000.0,
            "phone_number": "08539209999",
            "tax_id": "123321",
            "email_address": "email@gmail.com",
            "address": "address",
        }
        Account.objects.create(**mock_data)
        response = self.client.post(
            path=self.TRANSACTION_URL,
            data=json.dumps(self.BASE_PAYLOAD),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["code"], "already_exist")

    def test_create_account_with_low_deposit(self):
        """Function to test account creation expected to be success"""
        self.BASE_PAYLOAD["name"] = "test1"
        self.BASE_PAYLOAD["phone_number"] = "08539209999"
        self.BASE_PAYLOAD["tax_id"] = "123321"
        self.BASE_PAYLOAD["deposit_amount"] = 10

        response = self.client.post(
            path=self.TRANSACTION_URL,
            data=json.dumps(self.BASE_PAYLOAD),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["code"], "low_inital_deposit")


class BalanceTest(APITestCase):
    """Test Case for Balance Check"""

    TRANSACTION_URL = "http://localhost:8000/api/account/balance"
    BASE_PAYLOAD = {"user_id": "c16365f9-c8e7-4bee-aa9b-0f47682241f5"}

    def test_check_balance(self):
        """Function to test check balance expected to be success"""
        mock_data = {
            "name": "TEST",
            "account_number": "08539209999123321",
            "total_balance": 5000.0,
            "phone_number": "08539209999",
            "tax_id": "123321",
            "email_address": "email@gmail.com",
            "address": "address",
        }

        account = Account.objects.create(**mock_data)
        self.BASE_PAYLOAD["user_id"] = str(account.user_id)

        response = self.client.post(
            path=self.TRANSACTION_URL,
            data=json.dumps(self.BASE_PAYLOAD),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_invalid_user_id(self):
        """Function to test check balance with invalid user_id"""
        mock_data = {
            "name": "TEST",
            "account_number": "08539209999123321",
            "total_balance": 5000.0,
            "phone_number": "08539209999",
            "tax_id": "123321",
            "email_address": "email@gmail.com",
            "address": "address",
        }

        account = Account.objects.create(**mock_data)
        self.BASE_PAYLOAD["user_id"] = "aksdjioasjdioajd"

        response = self.client.post(
            path=self.TRANSACTION_URL,
            data=json.dumps(self.BASE_PAYLOAD),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["code"], "wrong_user_id")
