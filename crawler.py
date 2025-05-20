import requests

def crawler():
    response = requests.get("https://www.scrapingcourse.com/ecommerce/")
    response.raise_for_status()
    print(response.text)

#execute the crawler
crawler()