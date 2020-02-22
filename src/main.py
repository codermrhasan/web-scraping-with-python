print(
    f"#######################################\n"+
    f"# Welcome To Web Scraping With Python #\n"+
    f"#######################################\n"
)

while(True):
    print(
        f"Please choose a scraping app to use it\n" +
        f"Enter 0 to exit\n"
    )
    print(
        f"\n               App Lists               \n" +
        f"***************************************\n" +
        f"1. Upcoming Events of Python"
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
    


print(
    f'\nThanks for using our Apps\n' +
    f"Have a good day"
)