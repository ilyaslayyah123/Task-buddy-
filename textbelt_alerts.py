import requests

def send_textbelt_sms(message, phone='+923286371091'):
    response = requests.post('https://textbelt.com/text', {
        'phone': phone,  
        'message': message,
        'key': 'textbelt'  
    })

    result = response.json()
    if result.get('success'):
        print("SMS sent successfully!")
    else:
        print("SMS failed:", result.get('error'))


