import requests
from twilio.rest import Client
MY_API_KEY="909a809ea1f131fcf181772cd28c2c09"
own_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
Account_ID ="ACf7cc2d6a0d388b716fd090b203c1a4dd"
Token ="ea9b614ec30de199d495817f246009c3"




weather_params ={
    "lat":-33.865143,
"lon":151.209900,
"appid":MY_API_KEY,
"exclude":"current,minutely,daily"
}
will_rain = False
response = requests.get(own_endpoint,params=weather_params)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True

if will_rain==True:

    client = Client(Account_ID, Token)

    message = client.messages \
        .create(
        body="Hey Abhi,it is going to rain today,Please take  an umbrella with you",
        from_='+13608031091',
        to='+61433969361'
    )

    print(message.status)

