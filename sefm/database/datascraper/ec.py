import pandas as pd
import datetime
from dateutil import rrule
from datetime import datetime, timedelta
import os
from retrying import retry
import math


def getCompleteWeatherTimeSeriesEC(df_stations, output_path, timeframe):
    """

    :param df_stations:
    :param output_path:
    :param timeframe:
    """
    stationID = df_stations['Station ID']
    if timeframe == 1:
        start_date = df_stations['HLY First Year']
        end_date = df_stations['HLY Last Year']
    elif timeframe == 2:
        start_date = df_stations['DLY First Year']
        end_date = df_stations['DLY Last Year']
    if not (math.isnan(start_date) or (math.isnan(end_date))):
        start_date = datetime.strptime(str(int(start_date)), '%Y')
        end_date = datetime.strptime(str(int(end_date)), '%Y')

        frames = []
        for dt in rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date):
            df = getHourlyDataEC(stationID, dt.year, dt.month, timeframe)
            frames.append(df)

        weather_data = pd.concat(frames)
        weather_data['Date/Time'] = pd.to_datetime(weather_data['Date/Time'])

        if timeframe == 1:
            weather_data['Temp (°C)'] = pd.to_numeric(weather_data['Temp (°C)'])
        elif timeframe == 2:
            weather_data['Max Temp (°C)'] = pd.to_numeric(weather_data['Max Temp (°C)'])
            weather_data['Min Temp (°C)'] = pd.to_numeric(weather_data['Min Temp (°C)'])
            weather_data['Mean Temp (°C)'] = pd.to_numeric(weather_data['Mean Temp (°C)'])

        weather_data.set_index('Date/Time', inplace=True)
        name = df_stations['Climate ID']

        start = weather_data.index[0].strftime('%Y%m%d')
        end = weather_data.index[-1].strftime('%Y%m%d')
        complete_name = 'meteo_' + start + '_' + name + '_' + end + '.csv'
        weather_data.to_csv(os.path.join(output_path, complete_name))


@retry(wait_random_min=2000, wait_random_max=3000, stop_max_attempt_number=10)
def getHourlyDataEC(stationID, year, month, timeframe):
    # Call Environment Canada API
    # Returns a dataframe of data
    base_url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?"
    query_url = "format=csv&stationID={}&Year={}&Month={}&timeframe={}".format(stationID, year, month, timeframe)
    api_endpoint = base_url + query_url
    return pd.read_csv(api_endpoint, skiprows=0)