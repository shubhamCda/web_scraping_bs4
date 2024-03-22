import requests
import json

proxies = {
    "http": "http://103.168.44.105:3127",  # replace with your proxy ip and port
    "https": "https://103.168.44.105:3127",
}

r = requests.get("https://www.indiatoday.in/", proxies=proxies)
print(r.json())
