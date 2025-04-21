import aiohttp
from .config import PaysafeConfig
from .exceptions import PaysafeException, APIConnectionError

class AsyncPaysafeClient:
    def __init__(self, api_key, api_secret, environment="TEST"):
        self.config = PaysafeConfig(api_key, api_secret, environment)

    async def authorize_card(self, payload: dict):
        url = f"{self.config.base_url}/cardpayments/v1/accounts/{payload.get('merchantAccountId', 'YOUR_MERCHANT_ID')}/auths"
        headers = {
            "Content-Type": "application/json",
            **self.config.get_auth_header()
        }
        return await self._request("POST", url, headers, payload)

    async def _request(self, method, url, headers, json_data):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.request(method, url, headers=headers, json=json_data) as response:
                    if response.status >= 400:
                        text = await response.text()
                        raise PaysafeException(f"API Error {response.status}: {text}")
                    return await response.json()
        except aiohttp.ClientError as e:
            raise APIConnectionError(f"Connection failed: {str(e)}")
