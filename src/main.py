

while(True):
    print(
        "\n#######################################\n"+
        "# Welcome To Web Scraping With Python #\n"+
        "#######################################\n"
    )
    print(
        "Please choose a scraping app to use it\n" +
        "Enter 0 to exit\n"
    )
    print(
        "               App Lists               \n" +
        "***************************************\n" +
        "1. Upcoming Events of Python\n" +
        "2. Hacker News\n" +
        "3. Hacker News API Fetching\n" +
        "4. Quotes Scraping"

    )
    

    app_option = int(input())
    if app_option == 0:
        break
    
    elif app_option == 1:
        print(
            'Choose which tools do you want to use this app\n'+
            '1. Beautifulsoup  2. Selenium'
        )
        tool_option = int(input())
        if tool_option == 1:
            from upcoming_python_events.with_beautifulsoup import scraper
            scraper()
        elif tool_option == 2:
            from upcoming_python_events.with_selenium import scraper
            scraper()

    elif app_option == 2:
        from hacker_news.with_beautifulsoup import hacker_news_scraper
        print("Scraping Data...")
        hacker_news_scraper()
    
    elif app_option == 3:
        from hacker_news_api.with_beautifulsoup import hacker_news_api_integration
        hacker_news_api_integration()

    elif app_option == 4:
        from quotes_to_scrape.with_beautifulsoup import main_scraper
        main_scraper()

print(
    f'\nThanks for using our Apps\n' +
    f"Have a good day"
)