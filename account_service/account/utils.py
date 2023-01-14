class AccountUtils:
    def create_account_number(self, data):
        """Generate Account Number"""
        phone_number = data["phone_number"]
        tax_id = data["tax_id"]
        data["account_number"] = f"{phone_number}{tax_id}"
        return data