import base64

class PaysafeConfig:
    def __init__(self, api_key: str, api_secret: str, environment: str = "TEST"):
        self.api_key = api_key
        self.api_secret = api_secret
        self.environment = environment.upper()
        self.base_url = self._set_base_url()

    def _set_base_url(self):
        if self.environment == "TEST":
            return "https://api.test.paysafe.com"
        elif self.environment == "LIVE":
            return "https://api.paysafe.com"
        else:
            raise ValueError("Invalid environment. Use 'TEST' or 'LIVE'.")

    def get_auth_header(self):
        key_secret = f"{self.api_key}:{self.api_secret}"
        token = base64.b64encode(key_secret.encode()).decode()
        return {"Authorization": f"Basic {token}"}
