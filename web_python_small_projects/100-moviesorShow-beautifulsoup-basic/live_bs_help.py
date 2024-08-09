from bs4 import BeautifulSoup
import requests

def link(uri, label=None):
    if label is None:
        label = uri
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup =  BeautifulSoup(yc_web_page,"html.parser")
# print(soup.title)

articles = soup.find_all(name="a", class_ ="storylink")
article_text = []
article_link = []
all_upvotes = []
for article in articles:
    article_text.append(article.getText())
    article_link.append(article.get("href"))

all_upvotes =  [score.getText().split(" ")[0] for score in soup.find_all(name="span", class_ = "score")]

order = [ [text,link,upvote] for text,link,upvote in zip(article_text,article_link,all_upvotes)]

## getting most liked article
for article in order:
    if article[2] == max(all_upvotes):
        print(f"This is the most rated article on Ycombinator with {article[2]} upvotes titled '{article[0]}' : {article[1]}.")
# Print the hyperlink using ANSI escape codes (for compatible terminals)

