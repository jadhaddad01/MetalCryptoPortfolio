import http.client
import config

conn = http.client.HTTPSConnection("live-metal-prices.p.rapidapi.com")

headers = {
    'x-rapidapi-key': config.APIKey,
    'x-rapidapi-host': "live-metal-prices.p.rapidapi.com"
    }

conn.request("GET", "/v1/latest/XAU,XAG,PA,PL,GBP,EUR/EUR/gram", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))