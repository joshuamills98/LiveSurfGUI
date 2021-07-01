import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import os
import re
from datetime import datetime, timedelta


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


def clean_wind_table(df):
    """Strip out all white space and wrong characters and return df"""
    df = df.iloc[1:, :]

    # Remove "Yesterday" and "Today" from date column
    df.iloc[:, 0] = df.iloc[:, 0].apply(
        lambda x: re.sub('([a-z]|[A-Z])+', '', x).strip())  

    # Remove "/" symbol, select knots and replace '-' values with 0 kts
    df.loc[:, 'Wind(km/h)/(kt)'] = df.loc[:, 'Wind(km/h)/(kt)']\
        .apply(lambda x: re.sub('\d+\s+\/\s+', '',
                                x.replace('-', '0')).strip())

    df.loc[:, 'Gust(km/h)/(kt)'] = df.loc[:, 'Gust(km/h)/(kt)'] \
        .apply(lambda x: re.sub('\d+\s+\/\s+', '',
                                x.replace('-', '0')).strip())

    # Replace '-' with westerly winds (this needs to be verified)
    df.loc[:, 'WindDir.'] = df.loc[:, 'WindDir.'] \
        .apply(lambda x: x.replace('-', 'W'))
    return df


def download_wind_table(source):
    opener = AppURLopener()

    with opener.open(source) as raw_data:
        return raw_data.read()


def convert_to_datetime(df, date_of_usage, format="%H:%M"):
    """Return df with a datetime index

    Keyword arguments:
    df -- dataframe extracted from ozforecasts
    date_of_usage -- current date of extraction to calibrate data
    format -- format of existing datetie labels
    """
    year = date_of_usage.year
    month = date_of_usage.month
    day = date_of_usage.day
    latest_date = datetime.\
        strptime(df.iloc[0, 0], format).\
        replace(year=year,
                month=month,
                day=day)
    print(latest_date)
    num_time_steps = df.shape[0]
    date_range = [latest_date - timedelta(minutes=10*x) for x in
                  range(num_time_steps)]
    df['date'] = date_range
    df.set_index(['date'], inplace=True)
    print(df.index[-1])
    return df


def parse_wind_data(html_text):
    """Parse the html representing the wind forecast and reutrn a dataframe"""
    soup = BeautifulSoup(html_text, 'html.parser')

    # Locate table
    table_body = soup.find(
        'table',
        attrs={"style": "margin-left: auto; margin-right: auto;"}) \
        .find('table', attrs={'class': 'ozf'})

    # Extract tabular data from each row using relevant tags
    data = []
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all(['th', 'td'])
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Get rid of empty values

    # Get the date at which data is being called on the webpage
    date_of_usage = datetime.strptime(
        soup.find('h2').text.replace(
            'Observations for 24 hours up to ', ''),
        "%Y-%m-%d %H:%M")

    # Clean and process dataframe
    df = pd.DataFrame(data, columns=data[0])
    df = clean_wind_table(df)
    df = convert_to_datetime(df, date_of_usage)

    # Get name of weather station for metadata
    station_text = soup.find('td',
                             attrs={'style': 'text-align: center;'}).text
    station_name = re.findall(r"\s+(.+) Weather Station",
                              station_text)[0].replace(' ', '_')
    return station_name, df


def wind_data_main(source):
    """Download, parse, clean and process wind data from given source"""
    source_html = download_wind_table(source)
    station_name, df = parse_wind_data(source_html)
    path = os.path.join("wind_analysis",
                        "wind_data",
                        station_name + "_Wind_Data.csv")
    df.to_csv(path)


if __name__ == '__main__':
    source = "https://ozforecast.com.au/cgi-bin/"\
             "weatherstation.cgi?station=95937"
    wind_data_main(source)
