import requests

url = "https://api.wazirx.com/api/v2/tickers" #API 
response = (requests.get(url).json()) #API Response

#Takes in the coin symbol as the parameter
def price(coin): 
    return response[coin.lower() + "inr"]["last"]

print(price("DOGE"))
