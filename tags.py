import requests
from bs4 import BeautifulSoup


with open("sample.html",  "r") as f:
    html_doc = f.read()          # We will get the content of sample.html as a string

soup = BeautifulSoup(html_doc, "html.parser") # soup is a special object which is used by beautiful soup to fetch data from html doc


# print(soup.prettify())
# print(soup.title, type(soup.title))  # <title>Sample HTML page</title>,<class 'bs4.element.Tag'>          # To see the HTML document in readable format        # This is used to print the HTML document

# print(soup.title.string, type(soup.title.string))  # WebScraping <class 'bs4.element.NavigableString'>

# print(soup.div)    # This will return only 1st div
# print(soup.find_all("div")[1])  #[0] For 1st div

# for link in soup.find_all('a'):   # To find all links with href attribute
#     print(link['href'])
#     print(link.get_text().strip())  # Get text inside the tag without any HTML tags

s = soup.find(id="link3")     # Find first element by id=
# print(len(s), s)                                # There is one element with id=link3
# print(s.get_text())               # Get text from first occurrence (index 0)
print(s.get("href"))
