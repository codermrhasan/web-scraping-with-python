import requests
from bs4 import BeautifulSoup

def scraper():
    
    url = 'https://www.python.org/events/python-events/'
    # download the page
    try:
        req = requests.get(url)
    except:
        print('Something went wrong. Make Sure you have provided a valid url')
        return
    
    if req.status_code != 200:
        print("make sure you are making a valid get request")
        return

    # parse the html
    soup = BeautifulSoup(req.text, 'lxml')

    # getting list of all events
    events = soup.find('ul', {'class':'list-recent-events'}).findAll('li')

    # formatting data
    print(
        f"\n        Upcoming Python Events        \n" +
        '+++++++++++++++++++++++++++++++++++++\n'
    )
    i = 1
    for event in events:
        event_details = dict()
        event_details['name'] = event.find('h3').find('a').text
        event_details['time'] = event.find('time').text
        event_details['location'] = event.find('span', {'class': 'event-location'}).text

        print(
            f"______________Event {i}______________\n"
            f"Event Name: {event_details['name']}\n" +
            f"Event Time: {event_details['time']}\n" +
            f"Event Location: {event_details['location']}\n"
        )
        i += 1