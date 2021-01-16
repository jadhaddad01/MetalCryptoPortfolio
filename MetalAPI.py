import http.client
import json
import config

conn = http.client.HTTPSConnection("live-metal-prices.p.rapidapi.com")

headers = {
    'x-rapidapi-key': config.APIKey,
    'x-rapidapi-host': "live-metal-prices.p.rapidapi.com"
    }

conn.request("GET", "/v1/latest/XAU,XAG,PA,PL,GBP,/EUR/ounce", headers=headers)

res = conn.getresponse()
data = res.read()
response = json.loads(data.decode("utf-8"))

def getSuccess():
    return response["success"]

def getValidationMessage():
    return response["validationMessage"]

def getBaseCurrency():
    return response["baseCurrency"]

def getUnit():
    return response["unit"]

def getRates():
    return response["rates"]

print(response)