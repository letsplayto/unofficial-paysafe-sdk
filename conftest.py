import pytest
from paysafe.config import PaysafeConfig
from paysafe.client import PaysafeClient
from paysafe.async_support import AsyncPaysafeClient


@pytest.fixture
def api_key():
    return "test_api_key"


@pytest.fixture
def api_secret():
    return "test_api_secret"


@pytest.fixture
def merchant_id():
    return "merchant_12345"


@pytest.fixture
def config(api_key, api_secret):
    return PaysafeConfig(api_key, api_secret, environment="TEST")


@pytest.fixture
def client(api_key, api_secret):
    return PaysafeClient(api_key, api_secret, environment="TEST")


@pytest.fixture
def async_client(api_key, api_secret):
    return AsyncPaysafeClient(api_key, api_secret, environment="TEST")


@pytest.fixture
def sample_auth_payload(merchant_id):
    return {
        "merchantAccountId": merchant_id,
        "amount": 1000,
        "currencyCode": "USD",
        "card": {
            "cardNum": "4111111111111111",
            "cvv": "123",
            "expiryMonth": 12,
            "expiryYear": 2027,
        },
        "billingDetails": {
            "street": "123 Test St",
            "city": "Testville",
            "country": "US",
            "zip": "12345",
        },
    }


@pytest.fixture
def sample_auth_response():
    return {
        "id": "auth_abc123",
        "merchantRefNum": "ref_001",
        "amount": 1000,
        "status": "COMPLETED",
        "txnTime": "2026-09-06T12:00:00Z",
    }
