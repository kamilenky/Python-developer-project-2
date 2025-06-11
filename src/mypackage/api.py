# 5.API section
# tato cast prekonvertuje sumu na vratenie na inu menu pomocou API
# nie je dokoncena
# chcem prepojit vystup {refund_amount:.2f} z calculations.py a amount_in_currency

import requests


def get_exchange_rate(base="EUR", target="CZK"):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{base}"
        response = requests.get(url)
        data = response.json()
        return data["rates"].get(target)
    except Exception as e:
        print("Chyba - API")
        return None



# # Usage
# rate = get_exchange_rate("EUR", "CZK")
# amount_in_currency = 1 * rate
# print(f"Refund in CZK: {amount_in_currency:.2f}")
