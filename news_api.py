import requests

NEWS_API_KEY = '84a1069d41f84d8e895a044753b0f886'  

def get_news_headlines():
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    
    if response.status_code != 200:
        return "Sorry, couldn't fetch the news at the moment."

    data = response.json()
    articles = data.get('articles', [])
    
    if not articles:
        return "No news articles available right now."

    headlines = [f" {article['title']}" for article in articles[:5]]
    return "\n".join(headlines)

