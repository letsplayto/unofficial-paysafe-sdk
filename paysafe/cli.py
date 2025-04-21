import argparse
import json
from . import PaysafeClient

def main():
    parser = argparse.ArgumentParser(description="Paysafe CLI Tool")
    parser.add_argument("--key", required=True, help="API Key")
    parser.add_argument("--secret", required=True, help="API Secret")
    parser.add_argument("--merchant", required=True, help="Merchant Account ID")
    parser.add_argument("--amount", type=int, required=True, help="Payment amount in cents")

    args = parser.parse_args()

    client = PaysafeClient(args.key, args.secret)
    payload = {
        "merchantAccountId": args.merchant,
        "amount": args.amount,
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

    try:
        response = client.payments.authorize_card(payload)
        print("✅ Authorized:", json.dumps(response, indent=2))
    except Exception as e:
        print("❌ Error:", str(e))

if __name__ == "__main__":
    main()
