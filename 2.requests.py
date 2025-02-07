import requests
import random
import json
import time

# https://api.binance.com
# https://api-gcp.binance.com
# https://api1.binance.com
# https://api2.binance.com
# https://api3.binance.com
# https://api4.binance.com

api_options = ["", "-gcp", "1", "2", "3", "4"]

valoare = random.choice(api_options)

BASE_URL = f"https://api{valoare}.binance.com"

print(BASE_URL)

PATH = "/api/v3/avgPrice"

URL = BASE_URL + PATH
print(URL)

symbol = "ETHUSDT"
def call_api():
    response = requests.get(URL, params ={"symbol":symbol})
    print(response.status_code)
    print(response.content, type(response.content))

    #deserializare
    json_response = json.loads(response.content)
    print(json_response, type(json_response))

    price = json_response['price']
    print("price=", price)

    with open("ethereum.txt", "a", encoding="utf-8") as fwritter:
        fwritter.write(price)
        fwritter.write("\n")

if __name__ == "__main__":
    while True:
        call_api()
        doarme = random.randint(1,2)
        print("doarme...", doarme, "secunde")
        time.sleep(doarme)
