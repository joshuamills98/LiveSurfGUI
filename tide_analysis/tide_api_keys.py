def get_bateman_tide(start_date, end_date):

    tide_url = "https://api.manly.hydraulics.works/api.php?" \
               "format=csv&page=rawdatatable&id=2371%2C97044" \
               "042%2C106491042&startdate=" \
               + start_date + "+10%3A00%3A00&enddate=" \
               + end_date + "+10%3A00%3A00&username=publicwww&token="\
               "KzZQWmJFbWZzRGVXYWdVTVpYQUpFb3hhb0ttSmh"\
               "MelFoKzRTTmR0U0lwL0lyVWRmUUdKTzlJRVVVNm1l"\
               "MTR4dzFxLy90cExuS0NFUmVDb0I5VXUvRllqL3dRL0lE"\
               "bjE4end3SDBLQmNrWU55QncwblpzeGJabStyT21CbGhV"\
               "MktaUWo4Ym5FK0d6aTZiQ3J2TDNac2JBR0hZbHRKd3Q5S"\
               "GFONE1sMlVGdHVYRkp2QWl2TDExWjArNUs5NDVQakpyb"\
               "zRGdCtlYXdCT0t4MWxTV2d1YThaKzNPNzdoLytNaTA4Y3"\
               "hHZHorM0RBRC92VG9tZU9IK0R3blA3NVFKaFdnbWhoRi"\
               "92UE5SdE1WQTVhQzdIKytGSm04WTVBUTdmS3RYZENvR2xt"\
               "SUFMMDJjN3FmQytrRkRNQnZlcXNnbnROOFY%3D"

    return tide_url
