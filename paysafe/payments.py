from .utils import make_request
from .exceptions import ValidationError


class PaymentsAPI:
    def __init__(self, config):
        self.config = config

    def authorize_card(self, payload: dict):
        if "amount" not in payload or "card" not in payload:
            raise ValidationError("Payload must include 'amount' and 'card' data.")

        merchant_id = payload.get("merchantAccountId")
        if not merchant_id:
            raise ValidationError("Payload must include 'merchantAccountId'.")

        url = f"{self.config.base_url}/cardpayments/v1/accounts/{merchant_id}/auths"
        headers = {
            "Content-Type": "application/json",
            **self.config.get_auth_header(),
        }
        return make_request("POST", url, headers=headers, json=payload)

    def capture_payment(self, auth_id: str, merchant_id: str, payload: dict = None):
        if not auth_id or not merchant_id:
            raise ValidationError("auth_id and merchant_id are required.")

        url = f"{self.config.base_url}/cardpayments/v1/accounts/{merchant_id}/auths/{auth_id}/captures"
        headers = {
            "Content-Type": "application/json",
            **self.config.get_auth_header(),
        }
        return make_request("POST", url, headers=headers, json=payload or {})

    def refund_payment(self, settlement_id: str, merchant_id: str, payload: dict = None):
        if not settlement_id or not merchant_id:
            raise ValidationError("settlement_id and merchant_id are required.")

        url = f"{self.config.base_url}/cardpayments/v1/accounts/{merchant_id}/settlements/{settlement_id}/refunds"
        headers = {
            "Content-Type": "application/json",
            **self.config.get_auth_header(),
        }
        return make_request("POST", url, headers=headers, json=payload or {})
