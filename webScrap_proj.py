import requests
from bs4 import BeautifulSoup
import pandas as pd


data = {"title": [], "price": []}

url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&param=178819&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.type%255B%255D%3DSmartphones&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNhbXN1bmcgc21hcnRwaG9uZXMiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&wid=26.productCard.PMU_V2_19"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())


# div_clss = soup.find_all(class_=["Brand-name"])
div_clss = soup.select("div._4rR01T")

for sp in div_clss:
    # print(sp.string)
    data["title"].append(sp.string)

# spans = soup.find_all("span", {"class": "pro-price"})
spans = soup.select("div._30jeq3._1_WHN1")
for sp in spans:
    # print(sp.get_text())
    data["price"].append(sp.string)

df = pd.DataFrame.from_dict(data).to_csv('shoppersstop.csv', index=False)
