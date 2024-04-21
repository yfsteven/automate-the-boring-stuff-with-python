#! python3

import requests, bs4
from twilio.rest import Client

url = 'https://forecast.weather.gov/MapClick.php?lat=40.6414317&lon=-74.0133144'
res = requests.get(url)
res.raise_for_status()

accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken  = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+1'
myCellPhone = '+1'


weatherSoup = bs4.BeautifulSoup(res.text, 'html.parser')

elem = weatherSoup.select('div.row-odd:nth-child(1) > div:nth-child(2)')

if 'showers' in elem[0].getText()):
    message = twilioCli.messages.create(body='Possibility of Rain. Bring an umbrella', from_=myTwilioNumber, to=myCellPhone)
