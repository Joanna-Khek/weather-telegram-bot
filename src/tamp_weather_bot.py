from api import Data
import pandas as pd
import telegram
import os


url = "https://api.data.gov.sg/v1/environment/2-hour-weather-forecast"
api = Data(url)

forecasts = api.get_forecasts()
timestamp = api.get_timestamp()
valid_period_start = api.get_start_period()
valid_period_end = api.get_end_period()


TAMP_API_KEY = os.environ['TAMP_API_KEY']
TAMP_CHAT_ID = os.environ['TAMP_CHAT_ID']


def send_message():
    date = f'*{pd.to_datetime(timestamp).date()}*'
    start_time = pd.to_datetime(valid_period_start).strftime('%I:%M %p')
    end_time = pd.to_datetime(valid_period_end).strftime('%I:%M %p')
    time_period = f'*{start_time} 到 {end_time}*'

    if (status == "Light Showers" or status == "Showers"):
        image_path = open("../images/light_shower.png", "rb")
        msg = date + "\n" + time_period + "\n" + '会下雨' + "\n" + f' {status}'
        bot.send_photo(chat_id=TAMP_CHAT_ID, photo=image_path, caption=msg, parse_mode=telegram.ParseMode.MARKDOWN)
    elif status == 'Thundery Showers':
        image_path = open("../images/thundery_shower.png", "rb")
        msg = date + "\n" + time_period + "\n" + '会下大雨' + "\n" + f' {status}'
        bot.send_photo(chat_id=TAMP_CHAT_ID, photo=image_path, caption=msg, parse_mode=telegram.ParseMode.MARKDOWN)
    elif status == "Light Rain":
        image_path = open("../images/light_rain.png", "rb")
        msg = date + "\n" + time_period + "\n" + '会下小雨' + "\n" + f' {status}'
        bot.send_photo(chat_id=TAMP_CHAT_ID, photo=image_path, caption=msg, parse_mode=telegram.ParseMode.MARKDOWN)

# filter
forecasts_subset = forecasts.query("area == 'Tampines'")
status = forecasts_subset.forecast.values[0]
print(status)

bot = telegram.Bot(token=TAMP_API_KEY)
send_message()



