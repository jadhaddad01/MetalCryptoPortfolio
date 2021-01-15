import http.client
import config

conn = http.client.HTTPSConnection("coingecko.p.rapidapi.com")

headers = {
    'x-rapidapi-key': config.APIKey,
    'x-rapidapi-host': "coingecko.p.rapidapi.com"
    }

conn.request("GET", "/simple/price?ids=bitcoin%2Cethereum&vs_currencies=CAD%2CEUR%2CUSD&include_last_updated_at=true&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))