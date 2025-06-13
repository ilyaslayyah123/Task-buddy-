import requests
API_KEY = '018515b395f8c9b40dec46b1cc7b24f1'

def get_weather(query):
    
    city = extract_city(query)
    if not city:
        return "Sorry, I couldn't find the city in your request."
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data['cod'] != 200:
        return f"Error: {data.get('message', 'Could not fetch weather')}"

    temp = data['main']['temp']
    condition = data['weather'][0]['description'].capitalize()
    city_name = data['name']
    
    return f"Weather in {city_name}: {temp}°C, {condition}"

def extract_city(query):
    words = query.lower().split()
    for i in range(len(words)):
        if words[i] == "in" and i+1 < len(words):
            return words[i+1]
    return None

