from api import Data
import pandas as pd
import telegram
import os
from io import BytesIO
from PIL import Image

url = "https://api.data.gov.sg/v1/environment/2-hour-weather-forecast"
api = Data(url)

forecasts = api.get_forecasts()
timestamp = api.get_timestamp()
valid_period_start = api.get_start_period()
valid_period_end = api.get_end_period()


API_KEY = os.environ['API_KEY']
CHAT_ID = os.environ['CHAT_ID']


def send_message():
    if status == "Light Showers":
        image_path = open("../images/light_shower.png", "rb")
        msg = time_period + "\n" + '会下雨' + "\n" + f' {status}'
        bot.send_photo(chat_id=CHAT_ID, photo=image_path, caption=msg, parse_mode=telegram.ParseMode.MARKDOWN)
    elif status == 'Thundery Showers':
        image_path = open("../images/thundery_shower.png", "rb")
        msg = time_period + "\n" + '会下大雨' + "\n" + f' {status}'
        bot.send_photo(chat_id=CHAT_ID, photo=image_path, caption=msg, parse_mode=telegram.ParseMode.MARKDOWN)

# filter
forecasts_subset = forecasts.query("area == 'Bukit Panjang'")
status = forecasts_subset.forecast.values[0]
print(status)

date = f'*{pd.to_datetime(timestamp).date()}*'
start_time = pd.to_datetime(valid_period_start).strftime('%I:%M %p')
end_time = pd.to_datetime(valid_period_end).strftime('%I:%M %p')
time_period = f'*{start_time} 到 {end_time}*'
msg = time_period + "\n" + '会下雨' + "\n" + f' {status}'
bot = telegram.Bot(token=API_KEY)
send_message()



