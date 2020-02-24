import re
import requests
from bs4 import BeautifulSoup

def hacker_news_scraper():
    url = 'https://news.ycombinator.com/news'
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'lxml')

    # going to save all data as a dictionary in news_list List
    news_list = []

    for item in soup.find_all('tr', class_='athing'):
        if item.find('a', class_='storylink') is None:
            continue
        
        # going to save all scraped data of a single news in a dictionary news_details
        news_details = dict()

        # getting news title and link 
        title = item.find('a', class_='storylink')
        link = title.get('href')
        news_details['title'] = title.text
        news_details['link'] = link
        
        # getting all other things
        next_item = item.find_next_sibling('tr')
        points = next_item.find('span', class_='score')
        comments = next_item.find('a', string=re.compile("^(\\d+\\s)comment(s?)"))
        news_details['points'] = points.text if points else '0 points'
        news_details['comments'] = comments.text.replace('\xa0', ' ') if comments else '0 comments'

        # saving data in list
        news_list.append(news_details)


    # Printing the scraped data
    print(
        "#################################" +
        "########## Hacker News ##########" +
        "#################################"

    )
    i = 1
    for news in news_list:
        print(
            f"_____________News {i}______________\n" +
            f"Title: {news['title']}\n" +
            f"Link: {news['link']}\n" +
            f"Points: {news['points']}\n" +
            f"Comments: {news['comments']}\n"
        )
        i+=1
