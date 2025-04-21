class PaysafeException(Exception):
    pass

class AuthenticationError(PaysafeException):
    pass

class ValidationError(PaysafeException):
    pass

class PaymentError(PaysafeException):
    pass

class APIConnectionError(PaysafeException):
    pass
