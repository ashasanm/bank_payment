"""Module to test Transaction API
    Note: Replace user id in TRANSACTION PAYLOAD with existing account user id
"""
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Transaction

# Create your tests here.


class SuccessTransactionTest(APITestCase):
    """Test Case for success transaction"""

    TRANSACTION_URL = "http://localhost:8001/api/transaction/"
    TRANSACITON_PAYLOAD = {
        "user_id": "c16365f9-c8e7-4bee-aa9b-0f47682241f5",
        "transaction_type": "",
        "transaction_amount": 0,
    }

    def test_deposit_success(self):
        """Function to test deposit expected to be success"""
        self.TRANSACITON_PAYLOAD["transaction_type"] = "deposit"
        self.TRANSACITON_PAYLOAD["transaction_amount"] = 500

        response = self.client.post(
            path=self.TRANSACTION_URL,
            data=json.dumps(self.TRANSACITON_PAYLOAD),
            content_type="application/json",
        )
        self.assertEqual(response.json()["status_code"], 200)

    def test_withdraw_success(self):
        """Function to test withdraw expected to be success"""
        self.TRANSACITON_PAYLOAD["transaction_type"] = "withdraw"
        self.TRANSACITON_PAYLOAD["transaction_amount"] = 123

        response = self.client.post(
            path=self.TRANSACTION_URL,
            data=json.dumps(self.TRANSACITON_PAYLOAD),
            content_type="application/json",
        )
        self.assertEqual(response.json()["status_code"], 200)


class ErrorTransactionTest(APITestCase):
    """Test Case for error transaction"""

    TRANSACTION_URL = "http://localhost:8001/api/transaction/"
    TRANSACITON_PAYLOAD = {
        "user_id": "c16365f9-c8e7-4bee-aa9b-0f47682241f5",
        "transaction_type": "",
        "transaction_amount": 0,
    }

    def test_decimal_exceed(self):
        """Function to test transaction amount with exceeded decimal"""
        self.TRANSACITON_PAYLOAD["transaction_type"] = "withdraw"
        self.TRANSACITON_PAYLOAD["transaction_amount"] = 2000.3030

        response = self.client.post(
            path=self.TRANSACTION_URL,
            data=json.dumps(self.TRANSACITON_PAYLOAD),
            content_type="application/json",
        )

        self.assertEqual(response.json()["status_code"], 400)
        self.assertEqual(response.json()["code"], "decimal_exceed")

    def test_deposit_minimum(self):
        """Function to test transaction when deposit under minimum amount"""
        self.TRANSACITON_PAYLOAD["transaction_type"] = "deposit"
        self.TRANSACITON_PAYLOAD["transaction_amount"] = 200

        response = self.client.post(
            path=self.TRANSACTION_URL,
            data=json.dumps(self.TRANSACITON_PAYLOAD),
            content_type="application/json",
        )

        self.assertEqual(response.json()["status_code"], 400)
        self.assertEqual(response.json()["code"], "low_deposit_amount")

    def test_withdraw_minimum(self):
        """Function to test transaction when withdraw under minimum amount"""
        self.TRANSACITON_PAYLOAD["transaction_type"] = "withdraw"
        self.TRANSACITON_PAYLOAD["transaction_amount"] = 5

        response = self.client.post(
            path=self.TRANSACTION_URL,
            data=json.dumps(self.TRANSACITON_PAYLOAD),
            content_type="application/json",
        )

        self.assertEqual(response.json()["status_code"], 400)
        self.assertEqual(response.json()["code"], "low_withdraw_amount")

    def test_low_balance(self):
        """Function to test withdraw or deposit user balance below minimum"""
        payload = self.TRANSACITON_PAYLOAD.copy()
        payload["user_id"] = "b7a190e1-c696-447f-a502-2ccc346debaa"
        payload["transaction_type"] = "withdraw"
        payload["transaction_amount"] = 500

        response = self.client.post(
            path=self.TRANSACTION_URL,
            data=json.dumps(payload),
            content_type="application/json",
        )

        self.assertEqual(response.json()["status_code"], 400)
        self.assertEqual(response.json()["code"], "low_balance")

    def test_invalid_id(self):
        """Function to test transaction when user id does not exist"""
        payload = self.TRANSACITON_PAYLOAD.copy()
        payload["user_id"] = "asdiuhasjdpaojd"
        payload["transaction_type"] = "withdraw"
        payload["transaction_amount"] = 200

        response = self.client.post(
            path=self.TRANSACTION_URL,
            data=json.dumps(payload),
            content_type="application/json",
        )

        self.assertEqual(response.json()["status_code"], 400)
        self.assertEqual(response.json()["code"], "wrong_user_id")
