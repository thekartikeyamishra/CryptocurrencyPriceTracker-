import requests

BASE_URL = "https://api.coingecko.com/api/v3"


def fetch_crypto_price(crypto_id):
    url = f"{BASE_URL}/simple/price?ids={crypto_id}&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if crypto_id in data:
            return {
                "Cryptocurrency": crypto_id.capitalize(),
                "Price (USD)": data[crypto_id]["usd"],
                "Market Cap (USD)": data[crypto_id]["usd_market_cap"],
                "24h Volume (USD)": data[crypto_id]["usd_24h_vol"],
            }
    return None
