import requests
import os
from swell_analysis.swell_api_keys import *
from bs4 import BeautifulSoup

def download_image(image_url, path):
    """Download image from web to a path given"""
    image_path = path
    img_data = requests.get(image_url).content
    with open(image_path, 'wb') as handler:
        handler.write(img_data)


def download_histories(location="Batemans Bay"):
    """Download swell history in the form of
    wave height, period, and direction using MHL API urls
    """
    if location == "Batemans Bay":
        wave_height_url, wave_direction_url, wave_period_url \
            = get_bateman_buoys()
    if location == "Eden":
        wave_height_url, wave_direction_url, wave_period_url \
            = get_eden_buoys()
    if location == "Port Kembla":
        wave_height_url, wave_direction_url, wave_period_url \
            = get_kembla_buoys()
    if location == "Sydney":
        wave_height_url, wave_direction_url, wave_period_url \
            = get_sydney_buoys()
    # Get and save wave data files
    response = requests.get(wave_height_url)
    with open(os.path.join("swell_analysis",
                           "swell_data",
                           "swell_height.csv"), 'wb') as f:
        f.write(response.content)

    response = requests.get(wave_direction_url)
    with open(os.path.join("swell_analysis",
                           "swell_data",
                           "swell_direction.csv"), 'wb') as f:
        f.write(response.content)

    response = requests.get(wave_period_url)
    with open(os.path.join("swell_analysis",
                           "swell_data",
                           "swell_period.csv"), 'wb') as f:
        f.write(response.content)


def download_swell_rose():
    """Download latest swell rose from BOM"""
    try:
        content = requests.get(url="https://mhl.nsw.gov.au/Station-BATBOW")
        soup = BeautifulSoup(content.text, 'html.parser')
        swell_map_url = soup.select(".order-lg-2 .img-fluid")[0]['src']
        path = os.path.join("swell_analysis", "images", "swell_rose.png")
        download_image(swell_map_url, path)
    except:
        print("Unable to download image")

def swell_data_main(location):
    download_histories(location)
    # download_swell_rose()


if __name__ == '__main__':
    # swell_data_main()
    download_swell_rose()