import requests

def hacker_news_api_integration():
    url = "https://hacker-news.firebaseio.com/v0"

    top_stories = requests.get(f"{url}/topstories.json").json()
    
    print(
        "######################################\n"+
        "###### Hacker News API Fetching ######\n" +
        "######################################\n"
    )
    for story_id in top_stories:
        print(f"Fetching... {url}/item/{story_id}.json")
        r = requests.get(f"{url}/item/{story_id}.json")
        story_details = r.json()

        print(story_details)
        
