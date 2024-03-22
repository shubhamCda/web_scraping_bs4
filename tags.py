import requests
from bs4 import BeautifulSoup


with open("sample.html",  "r") as f:
    html_doc = f.read()          # We will get the content of sample.html as a string

soup = BeautifulSoup(html_doc, "html.parser") # soup is a special object which is used by beautiful soup to fetch data from html doc
# print(soup.prettify())
print(soup.title, type(soup.title))                   # <title>Sample HTML page</title>,          # To see the HTML document in readable format        # This is used to print the HTML document
# print(soup.title.string, type(soup.title.string))       # <class 'bs4.element.NavigableString'>
