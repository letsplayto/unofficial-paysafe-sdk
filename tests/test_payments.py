import pytest
import responses
from paysafe.payments import PaymentsAPI
from paysafe.exceptions import ValidationError, PaysafeException


def test_authorize_missing_amount(config, sample_auth_payload):
    api = PaymentsAPI(config)
    del sample_auth_payload["amount"]
    with pytest.raises(ValidationError, match="amount"):
        api.authorize_card(sample_auth_payload)


def test_authorize_missing_card(config, sample_auth_payload):
    api = PaymentsAPI(config)
    del sample_auth_payload["card"]
    with pytest.raises(ValidationError, match="card"):
        api.authorize_card(sample_auth_payload)


def test_authorize_missing_merchant_id(config, sample_auth_payload):
    api = PaymentsAPI(config)
    del sample_auth_payload["merchantAccountId"]
    with pytest.raises(ValidationError, match="merchantAccountId"):
        api.authorize_card(sample_auth_payload)


@responses.activate
def test_authorize_card_success(config, sample_auth_payload, sample_auth_response, merchant_id):
    url = f"https://api.test.paysafe.com/cardpayments/v1/accounts/{merchant_id}/auths"
    responses.add(responses.POST, url, json=sample_auth_response, status=200)

    api = PaymentsAPI(config)
    result = api.authorize_card(sample_auth_payload)

    assert result == sample_auth_response
    assert len(responses.calls) == 1
    assert responses.calls[0].request.headers["Authorization"].startswith("Basic ")


@responses.activate
def test_authorize_card_api_error(config, sample_auth_payload, merchant_id):
    url = f"https://api.test.paysafe.com/cardpayments/v1/accounts/{merchant_id}/auths"
    responses.add(responses.POST, url, body="Card declined", status=402)

    api = PaymentsAPI(config)
    with pytest.raises(PaysafeException) as exc:
        api.authorize_card(sample_auth_payload)
    assert "402" in str(exc.value)


@responses.activate
def test_capture_payment_success(config, merchant_id):
    auth_id = "auth_abc123"
    url = f"https://api.test.paysafe.com/cardpayments/v1/accounts/{merchant_id}/auths/{auth_id}/captures"
    responses.add(responses.POST, url, json={"id": "capture_xyz", "status": "COMPLETED"}, status=200)

    api = PaymentsAPI(config)
    result = api.capture_payment(auth_id, merchant_id, payload={"amount": 1000})

    assert result["id"] == "capture_xyz"
    assert result["status"] == "COMPLETED"


def test_capture_missing_ids(config):
    api = PaymentsAPI(config)
    with pytest.raises(ValidationError):
        api.capture_payment("", "merchant_123")
    with pytest.raises(ValidationError):
        api.capture_payment("auth_123", "")


@responses.activate
def test_refund_payment_success(config, merchant_id):
    settlement_id = "settle_789"
    url = f"https://api.test.paysafe.com/cardpayments/v1/accounts/{merchant_id}/settlements/{settlement_id}/refunds"
    responses.add(responses.POST, url, json={"id": "refund_001", "status": "COMPLETED"}, status=200)

    api = PaymentsAPI(config)
    result = api.refund_payment(settlement_id, merchant_id, payload={"amount": 500})

    assert result["id"] == "refund_001"


def test_refund_missing_ids(config):
    api = PaymentsAPI(config)
    with pytest.raises(ValidationError):
        api.refund_payment("", "merchant_123")
