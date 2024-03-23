import requests
from bs4 import BeautifulSoup


with open("sample.html",  "r") as f:
    html_doc = f.read()          # We will get the content of sample.html as a string

soup = BeautifulSoup(html_doc, "html5lib")  # soup is a special object which is used by beautiful soup to fetch data from html doc


# print(soup.prettify())
# print(soup.title, type(soup.title))  # <title>Sample HTML page</title>,<class 'bs4.element.Tag'>          # To see the HTML document in readable format        # This is used to print the HTML document

# print(soup.title.string, type(soup.title.string))  # WebScraping <class 'bs4.element.NavigableString'>

# print(soup.div)    # This will return only 1st div
# print(soup.find_all("div")[1])  #[0] For 1st div

# for link in soup.find_all('a'):   # To find all links with href attribute
#     print(link['href'])
#     print(link.get_text().strip())  # Get text inside the tag without any HTML tags

# s = soup.find(id="link3")     # Find first element by id=
# # print(len(s), s)            # There is one element with id=link3
# # print(s.get_text())         # Get text from first occurrence (index 0)
# print(s.get("href"))

# print(soup.select("div.italic"))  # Select elements based on class name and tag name together o/p--> [<div class="italic">Italic 1</div>, <div class="italic">Italic 2</div>, <div class="italic">Italic 3</div>, <div class="italic">Italic 4</div>]
# print(soup.select("span#italic"))  # Using CSS selector o/p--> [<span id="italic">Italic with ID</span>]
# print(soup.span.get("class")) # return the list of the class

# for tg in soup.select("div.italic"):
#     print(tg)

# print(soup.find(id="italic"))  #  It returns None if not found else it returns the element

# for child in soup.find(class_="container").children:
#     print(child)
    
    
# for parent in soup.find(class_="box").parents:
#     print(parent)
    
# cont = soup.find(class_="container")
# cont.name="span"              #Changes div name to span
# cont["class"]="myClass"       #Changes class container to 'myClass'
# cont.string = "I'm a String"  #Changes conent inside  div to "Im a String"
# print(cont)

# To set new Tags

# ulTag = soup.new_tag("ul")
# liTag = soup.new_tag("li", {"style":"color:red;"})
# liTag.string = "Home"
# ulTag.append(liTag)                      # Append liTag into ulTag


# liTag = soup.new_tag("li")
# liTag.string = "About Us"               # Set string value
# ulTag.append(liTag)                      # Append another liTag into ulTag


# soup.html.body.insert(0,ulTag)          # Insert ulTag at beginning of body

# with open("modified.html", "w") as f:
#     f.write(str(soup))

cont = soup.find(class_="container")
print(cont.has_attr("id"))           # Returns True or False whether tag has attribute or not