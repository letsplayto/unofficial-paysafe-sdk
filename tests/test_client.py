from paysafe.client import PaysafeClient
from paysafe.payments import PaymentsAPI


def test_client_initialization(api_key, api_secret):
    client = PaysafeClient(api_key, api_secret, environment="TEST")
    assert isinstance(client.payments, PaymentsAPI)
    assert client.config.environment == "TEST"
    assert client.config.base_url == "https://api.test.paysafe.com"


def test_client_live_environment(api_key, api_secret):
    client = PaysafeClient(api_key, api_secret, environment="LIVE")
    assert client.config.base_url == "https://api.paysafe.com"
