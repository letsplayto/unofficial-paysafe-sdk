import pytest
import responses
from paysafe.utils import make_request
from paysafe.exceptions import PaysafeException, APIConnectionError


@responses.activate
def test_make_request_success():
    responses.add(
        responses.POST,
        "https://api.test.paysafe.com/test",
        json={"status": "ok"},
        status=200,
    )
    result = make_request("POST", "https://api.test.paysafe.com/test", json={"foo": "bar"})
    assert result == {"status": "ok"}


@responses.activate
def test_make_request_api_error():
    responses.add(
        responses.POST,
        "https://api.test.paysafe.com/test",
        body="Invalid request",
        status=400,
    )
    with pytest.raises(PaysafeException) as exc:
        make_request("POST", "https://api.test.paysafe.com/test")
    assert "400" in str(exc.value)
    assert "Invalid request" in str(exc.value)


@responses.activate
def test_make_request_connection_error():
    with pytest.raises(APIConnectionError):
        make_request("GET", "http://localhost:9999/does-not-exist", timeout=1)
