# 5d5071e9e82245459ce14221231606
import requests
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
city =input('Enter the Country name: ')
res = requests.get(f'http://api.weatherapi.com/v1/current.json?Key=5d5071e9e82245459ce14221231606&q={city}')
data =res.json()
try:
 print('Searching...')
 w= data['current']['temp_c']
 print('Loading...')
 text = f'the current weater in {city} is {w}'
 speak.Speak(text)
except Exception as e:
    text = f'No matching location found.'
    speak.Speak(text)
