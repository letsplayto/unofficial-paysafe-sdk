from .config import PaysafeConfig
from .payments import PaymentsAPI

class PaysafeClient:
    def __init__(self, api_key, api_secret, environment="TEST"):
        self.config = PaysafeConfig(api_key, api_secret, environment)
        self.payments = PaymentsAPI(self.config)
