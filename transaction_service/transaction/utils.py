import requests
from django.conf import settings


class ServerCommunicationUtils:
    """Utility to communicate between services"""

    @classmethod
    def get_account_balance(cls, payload: dict) -> dict:
        """Function to get user balance in account service"""
        try:
            url = settings.ACCOUNT_SERVICE_URL + "/api/account/balance"
            response = requests.post(url=url, json=payload, timeout=100)
            data = {"status_code": response.status_code}
            data.update(response.json())
            return data
        except TimeoutError as timeout_err:
            raise timeout_err
        except Exception as err:
            raise err

    def update_account_balance(self, payload: dict) -> dict:
        """Function to update balance in account service"""
        try:
            url = settings.ACCOUNT_SERVICE_URL + "/api/account/balance"
            response = requests.put(url=url, json=payload, timeout=100)
            data = {"status_code": response.status_code}
            data.update(response.json())
            return data
        except TimeoutError as timeout_err:
            raise timeout_err
        except Exception as err:
            raise err
