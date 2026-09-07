from paysafe.exceptions import (
    PaysafeException,
    AuthenticationError,
    ValidationError,
    PaymentError,
    APIConnectionError,
)


def test_exception_hierarchy():
    assert issubclass(AuthenticationError, PaysafeException)
    assert issubclass(ValidationError, PaysafeException)
    assert issubclass(PaymentError, PaysafeException)
    assert issubclass(APIConnectionError, PaysafeException)


def test_exception_messages():
    exc = ValidationError("Missing field")
    assert str(exc) == "Missing field"

    exc = APIConnectionError("Timeout")
    assert "Timeout" in str(exc)
