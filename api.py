import requests

def get_exchange_rate(base="EUR", target="USD"):
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    response = requests.get(url)
    data = response.json()
    return data["rates"].get(target)

# Usage
rate = get_exchange_rate("EUR", "USD")
amount_in_usd = 1000 * rate
print(f"Refund in USD: {amount_in_usd:.2f}")
