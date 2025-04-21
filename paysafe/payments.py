from .utils import make_request
from .exceptions import ValidationError

class PaymentsAPI:
    def __init__(self, config):
        self.config = config

    def authorize_card(self, payload: dict):
        if "amount" not in payload or "card" not in payload:
            raise ValidationError("Payload must include 'amount' and 'card' data.")

        url = f"{self.config.base_url}/cardpayments/v1/accounts/{{payload.get('merchantAccountId', 'YOUR_MERCHANT_ID')}}/auths"
        headers = {
            "Content-Type": "application/json",
            **self.config.get_auth_header()
        }
        return make_request("POST", url, headers=headers, json=payload)

    def capture_payment(self, auth_id: str, merchant_id: str, payload: dict = None):
        url = f"{self.config.base_url}/cardpayments/v1/accounts/{merchant_id}/auths/{auth_id}/captures"
        headers = {
            "Content-Type": "application/json",
            **self.config.get_auth_header()
        }
        return make_request("POST", url, headers=headers, json=payload or {})

    def refund_payment(self, settlement_id: str, merchant_id: str, payload: dict = None):
        url = f"{self.config.base_url}/cardpayments/v1/accounts/{merchant_id}/settlements/{settlement_id}/refunds"
        headers = {
            "Content-Type": "application/json",
            **self.config.get_auth_header()
        }
        return make_request("POST", url, headers=headers, json=payload or {})
