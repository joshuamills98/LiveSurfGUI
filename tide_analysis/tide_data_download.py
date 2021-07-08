from tide_analysis.tide_api_keys import get_bateman_tide
import requests
import os
from datetime import datetime, timedelta


def download_histories(location="Batemans Bay"):
    """Download tide history from MHL"""
    start_date = datetime.strftime(
        datetime.today() - timedelta(days=1),
        "%Y-%m-%d")
    end_date = datetime.strftime(
            datetime.today() + timedelta(days=1),
            "%Y-%m-%d")

    if location == "Batemans Bay":
        tide_url = get_bateman_tide(start_date, end_date)

    response = requests.get(tide_url)
    with open(os.path.join("tide_analysis",
                           "tide_data",
                           "tide_height.csv"), 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    download_histories()
