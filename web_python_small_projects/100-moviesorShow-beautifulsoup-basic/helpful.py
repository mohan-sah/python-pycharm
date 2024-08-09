from bs4 import BeautifulSoup

with open(file = "website.html", mode="r", encoding="utf8") as file:
    content = file.read()
    # print(content)

soup = BeautifulSoup(content , "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
## it gives first occurrence
# print(soup.p)
# print(soup.a)
# print(soup.h1)
## it gives all occurrence
all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    # print(tag.get_text())
    # print(tag.get("href"))
    pass

# heading =  soup.find_all(name = "h1", id = "name")
# print(heading)

section_heading = soup.find(name = "h3", class_ = "heading")
# print(section_heading.getText())
# print(section_heading.get("class"))

## selecting by css
company_url = soup.select_one(selector="p a")
by_id_heading= soup.select_one(selector="#book")
print(company_url, by_id_heading)

