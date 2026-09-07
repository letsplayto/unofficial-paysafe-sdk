## 💳 unofficial-paysafe-sdk

[![Tests](https://github.com/letsplayto/unofficial-paysafe-sdk/actions/workflows/tests.yml/badge.svg)](https://github.com/letsplayto/unofficial-paysafe-sdk/actions/workflows/tests.yml)

This is the **first unofficial Python SDK** for the [Paysafe REST API](https://developer.paysafe.com/). It provides a clean, Pythonic interface to authorize, capture, and refund card payments — with full support for **sync**, **async**, and **command-line** usage.

Built to help developers integrate Paysafe into:
- Games (Unity, Unreal, etc.)
- Web platforms
- Python apps and services
- Scripts and automation tools

---

### 🚀 Features

- 🔐 Secure authentication with Base64-encoded API keys
- 💳 Full card flow: authorize, capture, and refund
- ⏱️ Async client (for game engines, bots, async web apps)
- 💻 CLI tool for quick testing and automation
- 🧪 Comprehensive unit tests + GitHub Actions CI
- ✅ MIT Licensed and easy to extend

---

### 📦 Installation

```bash
pip install -e .
# or with dev dependencies
pip install -e ".[dev]"
```

### Quick Start (Sync)

```python
from paysafe import PaysafeClient

client = PaysafeClient("your_api_key", "your_api_secret", environment="TEST")

payload = {
    "merchantAccountId": "your_merchant_id",
    "amount": 1000,  # in cents
    "card": {
        "cardNum": "4111111111111111",
        "cvv": "123",
        "expiryMonth": 12,
        "expiryYear": 2027
    },
    "billingDetails": {
        "street": "123 Main St",
        "city": "City",
        "country": "US"
    }
}

response = client.payments.authorize_card(payload)
print(response)
```

### Async Usage

```python
from paysafe import AsyncPaysafeClient

async with AsyncPaysafeClient("your_api_key", "your_api_secret") as client:
    response = await client.authorize_card(payload)
```

### CLI

```bash
paysafe --key YOUR_KEY --secret YOUR_SECRET --merchant YOUR_MERCHANT_ID --amount 1000
```

---

### 📦 Why this exists

Paysafe currently provides official SDKs for Java, C#, and JavaScript — but none for Python.  
This SDK bridges that gap and enables any Python developer to start building with Paysafe *immediately*.

> ⚠️ This SDK is **community-maintained** and is **not affiliated with or endorsed by Paysafe**. Use at your own discretion and always test thoroughly in sandbox mode.
