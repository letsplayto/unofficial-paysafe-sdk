from paysafe import PaysafeClient
import os

client = PaysafeClient(os.getenv("PS_API_KEY"), os.getenv("PS_API_SECRET"), environment="TEST")

def test_payment():
    payload = {
        "merchantAccountId": "YOUR_MERCHANT_ID",
        "amount": 1000,
        "card": {
            "cardNum": "4111111111111111",
            "cvv": "123",
            "expiryMonth": 12,
            "expiryYear": 2025
        },
        "billingDetails": {
            "street": "123 Game Dev Blvd",
            "city": "Unityville",
            "country": "US"
        }
    }
    result = client.payments.authorize_card(payload)
    print("Payment Authorized:", result)

if __name__ == "__main__":
    test_payment()
