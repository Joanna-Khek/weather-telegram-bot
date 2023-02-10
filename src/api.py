import pandas as pd
import requests


class Data:
    def __init__(self, url):
        self.resp = requests.get(url).json()
    
    def get_status(self):
        return self.resp

    def get_forecasts(self):
        df = []
        for item in self.resp['items'][0]['forecasts']:
            data = {'area': item['area'],
                    'forecast': item['forecast']
                    }
            df.append(data)
        return pd.DataFrame(df)


    def get_timestamp(self):
         timestamp = self.resp['items'][0]['update_timestamp']
         return timestamp

    def get_start_period(self):
        valid_period_start = self.resp['items'][0]['valid_period']['start']
        return valid_period_start

    def get_end_period(self):
        valid_period_end = self.resp['items'][0]['valid_period']['end']
        return valid_period_end

        