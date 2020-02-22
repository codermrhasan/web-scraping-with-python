from selenium import webdriver

def scraper():
    url = 'https://www.python.org/events/python-events/'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url)

    events = driver.find_elements_by_xpath('//ul[contains(@class, "list-recent-events")]/li')

    print(
        f"\n        Upcoming Python Events        \n" +
        '+++++++++++++++++++++++++++++++++++++\n'
    )
    i=1
    for event in events:
        event_details = dict()
        event_details['name'] = event.find_element_by_xpath('h3[@class="event-title"]/a').text
        event_details['time'] = event.find_element_by_xpath('p/time').text
        event_details['location'] = event.find_element_by_xpath('p/span[@class="event-location"]').text

        print(
            f"______________Event {i}______________\n"
            f"Event Name: {event_details['name']}\n" +
            f"Event Time: {event_details['time']}\n" +
            f"Event Location: {event_details['location']}\n"
        )
        i += 1
    
    driver.close()

