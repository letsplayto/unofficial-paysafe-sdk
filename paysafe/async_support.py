import aiohttp
from .config import PaysafeConfig
from .exceptions import PaysafeException, APIConnectionError, ValidationError


class AsyncPaysafeClient:
    def __init__(self, api_key, api_secret, environment="TEST"):
        self.config = PaysafeConfig(api_key, api_secret, environment)
        self._session = None

    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self._session:
            await self._session.close()
            self._session = None

    async def _get_session(self):
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
        return self._session

    async def authorize_card(self, payload: dict):
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
        return await self._request("POST", url, headers, payload)

    async def capture_payment(self, auth_id: str, merchant_id: str, payload: dict = None):
        if not auth_id or not merchant_id:
            raise ValidationError("auth_id and merchant_id are required.")

        url = f"{self.config.base_url}/cardpayments/v1/accounts/{merchant_id}/auths/{auth_id}/captures"
        headers = {
            "Content-Type": "application/json",
            **self.config.get_auth_header(),
        }
        return await self._request("POST", url, headers, payload or {})

    async def refund_payment(self, settlement_id: str, merchant_id: str, payload: dict = None):
        if not settlement_id or not merchant_id:
            raise ValidationError("settlement_id and merchant_id are required.")

        url = f"{self.config.base_url}/cardpayments/v1/accounts/{merchant_id}/settlements/{settlement_id}/refunds"
        headers = {
            "Content-Type": "application/json",
            **self.config.get_auth_header(),
        }
        return await self._request("POST", url, headers, payload or {})

    async def _request(self, method, url, headers, json_data):
        try:
            session = await self._get_session()
            async with session.request(method, url, headers=headers, json=json_data) as response:
                if response.status >= 400:
                    text = await response.text()
                    raise PaysafeException(f"API Error {response.status}: {text}")
                return await response.json()
        except aiohttp.ClientError as e:
            raise APIConnectionError(f"Connection failed: {str(e)}")
