import requests

LLAMA_API_KEY = "tgp_v1_Gzm5z5KOVxCyQvllttXRoIrFgfUuNPQJhjAqK90Ow2I"
SERP_API_KEY = "2ca8eacc1f20c5eca0884833217f00b9443eaf4b3dd1a88d900cb6b9ee05331e"

keywords = ["latest", "today", "news", "recent", "update", "new model", "new version"]
def get_ai_response(query):
    query_lower= query.lower()
    if any(keyword in query_lower for keyword in keywords):
        return get_latest_tech_news(query)
    try:
        url = "https://api.together.xyz/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {LLAMA_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "mistralai/Mistral-7B-Instruct-v0.1",
            "messages": [
                {"role": "user", "content": query}
            ],
            "temperature": 0.7
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        reply = response.json()["choices"][0]["message"]["content"]
        return reply

    except requests.exceptions.RequestException as e:
        return f" API Request Error: {e}"
    except Exception as e:
        return f" Unexpected Error: {e}"

def get_latest_tech_news(query):
    try:
        url = f"https://serpapi.com/search.json?q={query}&api_key={SERP_API_KEY}&tbm=nws"
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        articles = data.get("news_results", [])
        if not articles:
            return "No news found."
        return "\n".join([f"{a['title']} - {a['link']}" for a in articles[:3]])
    except Exception as e:
        return f"Error fetching news: {e}"