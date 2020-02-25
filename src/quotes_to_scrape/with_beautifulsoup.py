import requests
from bs4 import BeautifulSoup

def quotes_scraper(base_url):
    url = base_url
    while True:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        
        all_quotes = soup.find_all('div', class_='quote')

        for quote in all_quotes:
            quote_text = quote.find('span', class_='text').text
            
            author_soup = quote.find('small', class_='author')
            author_name = author_soup.text
            author_url = author_soup.find_next_sibling('a').get('href')
            print(
                f"{quote_text}\n" +
                f"{author_name}\n" +
                f"{author_url}\n"
            )


        next_page = soup.find('li', class_="next")
        if next_page is None:
            break
        next_page_url =  next_page.find("a").get("href")
        url = f"{base_url}{next_page_url}"


def main_scraper():
    base_url = "http://quotes.toscrape.com"
    quotes_scraper(base_url)
