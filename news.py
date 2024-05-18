from newsplease import NewsPlease # for scraping web content
import requests
import json

file = open('keys.json')
keys = json.load(file)

# endpoint
URL = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + keys['news']
r = requests.get(URL)
data = r.json()

# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# array w/ all urls to articles from search results
def get_search_results(obj):
    urls = []
    for item in data:
        if item == "articles":
            articles = data.get("articles")
            for article in articles:
                for attribute in article:
                    if attribute == "url":
                        urls.append(article[attribute])
    return urls

# get source name of article based on site url
def get_source_name(url: str) -> str:
    source_name = ""
    for item in data:
        if item == "articles":
            articles = data.get("articles")
            for article in articles:
                for attribute in article:
                    if attribute == "url":
                        if article[attribute] == url:
                            for x in article["source"]:
                                if x == "name":
                                    source_name = article["source"][x]
    print(source_name)
    return source_name

# get source id of article based on site url
def get_source_id(url: str) -> str:
    source_id = ""
    for item in data:
        if item == "articles":
            articles = data.get("articles")
            for article in articles:
                for attribute in article:
                    if attribute == "url":
                        if article[attribute] == url:
                            for x in article["source"]:
                                if x == "id":
                                    source_id = article["source"][x]
    return source_id

# get author based on site url
def get_author(url: str) -> str:
    author = ""
    for item in data:
        if item == "articles":
            articles = data.get("articles")
            for article in articles:
                for attribute in article:
                    if attribute == "url":
                        if article[attribute] == url:
                            author = article["author"]
    return author

# get unformatted content of article (truncated to 200 chars) based on site url
def get_content(url: str) -> str:
    article = NewsPlease.from_url(url)
    content = article.maintext
    for item in data:
        if item == "articles":
            articles = data.get("articles")
            for article in articles:
                for attribute in article:
                    if attribute == "url":
                        if article[attribute] == url:
                            return content
    return "No content was found."

# get date based on site url
def get_date(url: str) -> str:
    date = ""
    for item in data:
        if item == "articles":
            articles = data.get("articles")
            for article in articles:
                for attribute in article:
                    if attribute == "url":
                        if article[attribute] == url:
                            date = article["publishedAt"]
    return date


# get title of article based on site url
def get_title(url: str) -> str:
    title = ""
    for item in data:
        if item == "articles":
            articles = data.get("articles")
            for article in articles:
                for attribute in article:
                    if attribute == "url":
                        if article[attribute] == url:
                            title = article["title"]
    return title

# get description of article based on site url
def get_description(url: str) -> str:
    description = ""
    for item in data:
        if item == "articles":
            articles = data.get("articles")
            for article in articles:
                for attribute in article:
                    if attribute == "url":
                        if article[attribute] == url:
                            description = article["description"]
    return description

# testing getter functions
# get_author("https://www.nbcnews.com/politics/congress/house-passes-bill-rebuking-biden-pausing-weapons-israel-rcna152681")
# get_date("https://www.nbcnews.com/politics/congress/house-passes-bill-rebuking-biden-pausing-weapons-israel-rcna152681")
# get_content("https://www.nbcnews.com/politics/congress/house-passes-bill-rebuking-biden-pausing-weapons-israel-rcna152681")
# get_source_name("https://www.nbcnews.com/politics/congress/house-passes-bill-rebuking-biden-pausing-weapons-israel-rcna152681")