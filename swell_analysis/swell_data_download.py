import requests
from bs4 import BeautifulSoup
import os


def download_image(image_url, path):
    """Download image from web to a path given"""
    image_path = path
    img_data = requests.get(image_url).content
    with open(image_path, 'wb') as handler:
        handler.write(img_data)


def download_histories():
    """Download swell history in the form of
    wave height, period, and direction using BOM API urls
    """
    wave_height_url = "https://api.manly.hydraulics.works/api.php?"\
                      "format=csv&page=rawdatatable&id=999%2C998&"\
                      "startdate=null&enddate=null&username=publicwww&token"\
                      "=KzZQWmJFbWZzRGVXYWdVTVpYQUpFb3hhb0ttSmhM"\
                      "elFoKzRTTmR0U0lw"\
                      "L0lyVWRmUUdKTzlJRVVVNm1lMTR4dz"\
                      "FxLy90cExuS0NFUmVDb0I5VXUv"\
                      "RllqL3dRL0lEbjE4end3SDBLQmNrWU55"\
                      "QncwblpzeGJabStyT21CbGhV"\
                      "MktaUWo4Ym5FK0d6aTZiQ3J2TDNac"\
                      "2JBR0hZbHRKd3Q5SGFONE1sMlVG"\
                      "dHVYRkp2QWl2TDExWjArNUs5NDVQakpybz"\
                      "RGdCtlYXdCT0t4MWxTV2d1YT"\
                      "haKzNPNzdoLytNaTA4Y3hHZHorM0RBRC92V"\
                      "G9tZU9IK0R3blA3NVFKaFdnbW"\
                      "hoRi92UE5SdE1WQTVhQzdIKytG"\
                      "Sm04WTVBUTdmS3RYZENvR2xtSUFMMDJjN3F"\
                      "mQytrRkRNQnZlcXNnbnROOFY%3D"

    wave_direction_url = "https://api.manly.hydraulics.works/api.php?"\
                         "format=csv&page=rawdatatable&id=1000&startdate="\
                         "null&enddate=null&username=publicwww&token"\
                         "=KzZQWmJFbWZzRGVXYWdVTVpYQUpFb3hhb0ttSmhMelFoKzR"\
                         "TTmR0U0lwL0lyVWRmUUdKTzlJRVVVNm1lMTR4dzFxLy90cExuS0"\
                         "NFUmVDb0I5VXUvRllqL3dRL0lEbjE4end3SDBLQmNrWU55Qncw"\
                         "blpzeGJabStyT21CbGhVMktaUWo4Ym5FK0d6aTZiQ3J2TDNac2J"\
                         "BR0hZbHRKd3Q5SGFONE1sMlVGdHVYRkp2QWl"\
                         "2TDExWjArNUs5NDVQ"\
                         "akpybzRGdCtlYXdCT0t4MWxTV2d1YThaKzNPNz"\
                         "doLytNaTA4Y3hHZH"\
                         "orM0RBRC92VG9tZU9IK0R3blA3NVFKaFdnbWh"\
                         "oRi92UE5SdE1WQTVhQzdI"\
                         "KytGSm04WTVBUTdmS3RYZENvR2xtSUFMMDJjN3FmQ"\
                         "ytrRkRNQnZlcXNnbnROOFY%3D"

    wave_period_url = "https://api.manly.hydraulics.works/api.php?"\
                      "format=csv&page=rawdatatable&id=1001%2C1003&startdate="\
                      "null&enddate=null&username=publicwww&token=KzZQWmJFbWZ"\
                      "zRGVXYWdVTVpYQUpFb3hhb0ttSmhMelFoKzRTT"\
                      "mR0U0lwL0lyVWRmUUd"\
                      "KTzlJRVVVNm1lMTR4dzFxLy90cExu"\
                      "S0NFUmVDb0I5VXUvRllqL3dRL0lEbj"\
                      "E4end3SDBLQmNrWU55QncwblpzeGJab"\
                      "StyT21CbGhVMktaUWo4Ym5FK0d6aT"\
                      "ZiQ3J2TDNac2JBR0hZbHRKd3Q5SGFONE1"\
                      "sMlVGdHVYRkp2QWl2TDExWjArNU"\
                      "s5NDVQakpybzRGdCtlYXdCT0t4MWxTV2d"\
                      "1YThaKzNPNzdoLytNaTA4Y3hHZH"\
                      "orM0RBRC92VG9tZU9IK0R3blA3NVFKaFdnb"\
                      "WhoRi92UE5SdE1WQTVhQzdIKyt"\
                      "GSm04WTVBUTdmS3RYZENvR2xtSUFMMDJj"\
                      "N3FmQytrRkRNQnZlcXNnbnROOFY%3D"

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


# def download_swell_rose():
#     """Download latest swell rose from BOM"""
#     content = requests.get(url="https://mhl.nsw.gov.au/Station-BATBOW")
#     soup = BeautifulSoup(content.text, 'html.parser')
#     swell_map_url = soup.select(".order-lg-2 .img-fluid")[0]['src']
#     path = os.path.join("swell_analysis", "images", "swell_rose.png")
#     download_image(swell_map_url, path)


def swell_data_main():
    download_histories()
    # download_swell_rose()


if __name__ == '__main__':
    swell_data_main()
