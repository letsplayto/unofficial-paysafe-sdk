import pytest
from aioresponses import aioresponses
from paysafe.async_support import AsyncPaysafeClient
from paysafe.exceptions import ValidationError, PaysafeException


@pytest.mark.asyncio
async def test_async_authorize_missing_fields(async_client, sample_auth_payload):
    del sample_auth_payload["amount"]
    with pytest.raises(ValidationError):
        await async_client.authorize_card(sample_auth_payload)


@pytest.mark.asyncio
async def test_async_authorize_success(async_client, sample_auth_payload, sample_auth_response, merchant_id):
    url = f"https://api.test.paysafe.com/cardpayments/v1/accounts/{merchant_id}/auths"

    with aioresponses() as mocked:
        mocked.post(url, payload=sample_auth_response, status=200)
        result = await async_client.authorize_card(sample_auth_payload)

    assert result == sample_auth_response


@pytest.mark.asyncio
async def test_async_authorize_api_error(async_client, sample_auth_payload, merchant_id):
    url = f"https://api.test.paysafe.com/cardpayments/v1/accounts/{merchant_id}/auths"

    with aioresponses() as mocked:
        mocked.post(url, body="Declined", status=402)
        with pytest.raises(PaysafeException) as exc:
            await async_client.authorize_card(sample_auth_payload)
        assert "402" in str(exc.value)


@pytest.mark.asyncio
async def test_async_capture_success(async_client, merchant_id):
    auth_id = "auth_abc123"
    url = f"https://api.test.paysafe.com/cardpayments/v1/accounts/{merchant_id}/auths/{auth_id}/captures"

    with aioresponses() as mocked:
        mocked.post(url, payload={"id": "cap_001", "status": "COMPLETED"}, status=200)
        result = await async_client.capture_payment(auth_id, merchant_id)

    assert result["id"] == "cap_001"


@pytest.mark.asyncio
async def test_async_refund_success(async_client, merchant_id):
    settlement_id = "settle_789"
    url = f"https://api.test.paysafe.com/cardpayments/v1/accounts/{merchant_id}/settlements/{settlement_id}/refunds"

    with aioresponses() as mocked:
        mocked.post(url, payload={"id": "ref_001", "status": "COMPLETED"}, status=200)
        result = await async_client.refund_payment(settlement_id, merchant_id)

    assert result["id"] == "ref_001"


@pytest.mark.asyncio
async def test_async_context_manager(api_key, api_secret, sample_auth_payload, sample_auth_response, merchant_id):
    url = f"https://api.test.paysafe.com/cardpayments/v1/accounts/{merchant_id}/auths"

    with aioresponses() as mocked:
        mocked.post(url, payload=sample_auth_response, status=200)

        async with AsyncPaysafeClient(api_key, api_secret) as client:
            result = await client.authorize_card(sample_auth_payload)
            assert result == sample_auth_response
