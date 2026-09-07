import base64
import pytest
from paysafe.config import PaysafeConfig


def test_config_test_environment(api_key, api_secret):
    config = PaysafeConfig(api_key, api_secret, environment="TEST")
    assert config.environment == "TEST"
    assert config.base_url == "https://api.test.paysafe.com"


def test_config_live_environment(api_key, api_secret):
    config = PaysafeConfig(api_key, api_secret, environment="LIVE")
    assert config.environment == "LIVE"
    assert config.base_url == "https://api.paysafe.com"


def test_config_case_insensitive(api_key, api_secret):
    config = PaysafeConfig(api_key, api_secret, environment="test")
    assert config.environment == "TEST"
    assert config.base_url == "https://api.test.paysafe.com"


def test_config_invalid_environment(api_key, api_secret):
    with pytest.raises(ValueError, match="Invalid environment"):
        PaysafeConfig(api_key, api_secret, environment="STAGING")


def test_get_auth_header(api_key, api_secret):
    config = PaysafeConfig(api_key, api_secret)
    headers = config.get_auth_header()

    expected_token = base64.b64encode(f"{api_key}:{api_secret}".encode()).decode()
    assert headers == {"Authorization": f"Basic {expected_token}"}
