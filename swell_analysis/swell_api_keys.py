def get_eden_buoys():
    wave_height = "https://api.manly.hydraulics.works/api.php?"\
                  "format=csv&page=rawdatatable&id=1027%2C102"\
                  "6&startdate=null&enddate=null&username=public"\
                  "www&token=KzZQWmJFbWZzRGVXYWdVTVpYQUpFb3hhb0"\
                  "ttSmhMelFoKzRTTmR0U0lwL0lyVWRmUUdKTzlJRVVVNm1"\
                  "lMTR4dzFxLy90cExuS0NFUmVDb0I5VXUvRllqL3dRL0lE"\
                  ":bjE4end3SDBLQmNrWU55QncwblpzeGJabStyT21CbGhVM"\
                  "ktaUWo4Ym5FK0d6aTZiQ3J2TDNac2JBR0hZbHRKd3Q5SGF"\
                  "ONE1sMlVGdHVYRkp2QWl2TDExWjArNUs5NDVQakpybzRG"\
                  "dCtlYXdCT0t4MWxTV2d1YThaKzNPNzdoLytNaTA4Y3hHZHo"\
                  "rM0RBRC92VG9tZU9IK0R3blA3NVFKaFdnbWhoRi92UE5SdE"\
                  "1WQTVhQzdIKytGSm04WTVBUTdmS3RYZENvR2xtSUFMMDJjN3"\
                  "FmQytrRkRNQnZlcXNnbnROOFY%3D"

    wave_direction = "https://api.manly.hydraulics.works/api.php?"\
                     "format=csv&page=rawdatatable&id=1028&startda"\
                     "te=null&enddate=null&username=publicwww&token"\
                     "=KzZQWmJFbWZzRGVXYWdVTVpYQUpFb3hhb0ttSmhMelFoK"\
                     "zRTTmR0U0lwL0lyVWRmUUdKTzlJRVVVNm1lMTR4dzFxLy9"\
                     "0cExuS0NFUmVDb0I5VXUvRllqL3dRL0lEbjE4end3SDBLQm"\
                     "NrWU55QncwblpzeGJabStyT21CbGhVMktaUWo4Ym5FK0d6aT"\
                     "ZiQ3J2TDNac2JBR0hZbHRKd3Q5SGFONE1sMlVGdHVYRkp2QW"\
                     "l2TDExWjArNUs5NDVQakpybzRGdCtlYXdCT0t4MWxTV2d1YTh"\
                     "aKzNPNzdoLytNaTA4Y3hHZHorM0RBRC92VG9tZU9IK0R3blA3"\
                     "NVFKaFdnbWhoRi92UE5SdE1WQTVhQzdIKytGSm04WTVBUTdmS"\
                     "3RYZENvR2xtSUFMMDJjN3FmQytrRkRNQnZlcXNnbnROOFY%3D"

    wave_period = "https://api.manly.hydraulics.works/api.php?"\
                  "format=csv&page=rawdatatable&id=1029%2C1031&"\
                  "startdate=null&enddate=null&username=publicww"\
                  "w&token=KzZQWmJFbWZzRGVXYWdVTVpYQUpFb3hhb0ttSm"\
                  "hMelFoKzRTTmR0U0lwL0lyVWRmUUdKTzlJRVVVNm1lMTR4"\
                  "dzFxLy90cExuS0NFUmVDb0I5VXUvRllqL3dRL0lEbjE4en"\
                  "d3SDBLQmNrWU55QncwblpzeGJabStyT21CbGhVMktaUWo4"\
                  "Ym5FK0d6aTZiQ3J2TDNac2JBR0hZbHRKd3Q5SGFONE1sMl"\
                  "VGdHVYRkp2QWl2TDExWjArNUs5NDVQakpybzRGdCtlYXdCT0"\
                  "t4MWxTV2d1YThaKzNPNzdoLytNaTA4Y3hHZHorM0RBRC92VG"\
                  "9tZU9IK0R3blA3NVFKaFdnbWhoRi92UE5SdE1WQTVhQzdIKy"\
                  "tGSm04WTVBUTdmS3RYZENvR2xtSUFMMDJjN3FmQytrRkRNQn"\
                  "ZlcXNnbnROOFY%3D"

    return wave_height, wave_direction, wave_period


def get_bateman_buoys():

    wave_height = "https://api.manly.hydraulics.works/api.php?"\
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

    wave_direction = "https://api.manly.hydraulics.works/api.php?"\
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

    wave_period = "https://api.manly.hydraulics.works/api.php?"\
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
    return wave_height, wave_direction, wave_period


def get_kembla_buoys():

    wave_height = "https://api.manly.hydraulics.works/api.php?"\
                  "format=csv&page=rawdatatable&id=1034%2C1033&"\
                  "startdate=null&enddate=null&username=publicwww"\
                  "&token=KzZQWmJFbWZzRGVXYWdVTVpYQUpFb3hhb0ttSmh"\
                  "MelFoKzRTTmR0U0lwL0lyVWRmUUdKTzlJRVVVNm1lMTR4dz"\
                  "FxLy90cExuS0NFUmVDb0I5VXUvRllqL3dRL0lEbjE4end3S"\
                  "DBLQmNrWU55QncwblpzeGJabStyT21CbGhVMktaUWo4Ym5FK"\
                  "0d6aTZiQ3J2TDNac2JBR0hZbHRKd3Q5SGFONE1sMlVGdHVYR"\
                  "kp2QWl2TDExWjArNUs5NDVQakpybzRGdCtlYXdCT0t4MWxTV"\
                  "2d1YThaKzNPNzdoLytNaTA4Y3hHZHorM0RBRC92VG9tZU9IK0R3"\
                  "blA3NVFKaFdnbWhoRi92UE5SdE1WQTVhQzdIKytGSm04WTVBUTd"\
                  "mS3RYZENvR2xtSUFMMDJjN3FmQytrRkRNQnZlcXNnbnROOFY%3D"

    wave_direction = "https://api.manly.hydraulics.works/api.php?"\
                     "format=csv&page=rawdatatable&id=1035&startdat"\
                     "e=null&enddate=null&username=publicwww&token=Kz"\
                     "ZQWmJFbWZzRGVXYWdVTVpYQUpFb3hhb0ttSmhMelFoKzRTT"\
                     "mR0U0lwL0lyVWRmUUdKTzlJRVVVNm1lMTR4dzFxLy90cExuS"\
                     "0NFUmVDb0I5VXUvRllqL3dRL0lEbjE4end3SDBLQmNrWU55Q"\
                     "ncwblpzeGJabStyT21CbGhVMktaUWo4Ym5FK0d6aTZiQ3J2TD"\
                     "Nac2JBR0hZbHRKd3Q5SGFONE1sMlVGdHVYRkp2QWl2TDExWjA"\
                     "rNUs5NDVQakpybzRGdCtlYXdCT0t4MWxTV2d1YThaKzNPNzdo"\
                     "LytNaTA4Y3hHZHorM0RBRC92VG9tZU9IK0R3blA3NVFKaFdnb"\
                     "WhoRi92UE5SdE1WQTVhQzdIKytGSm04WTVBUTdmS3RYZENvR2"\
                     "xtSUFMMDJjN3FmQytrRkRNQnZlcXNnbnROOFY%3D"

    wave_period = "https://api.manly.hydraulics.works/api.php?"\
                  "format=csv&page=rawdatatable&id=1036%2C1038"\
                  "&startdate=null&enddate=null&username=public"\
                  "www&token=KzZQWmJFbWZzRGVXYWdVTVpYQUpFb3hhb0t"\
                  "tSmhMelFoKzRTTmR0U0lwL0lyVWRmUUdKTzlJRVVVNm1lM"\
                  "TR4dzFxLy90cExuS0NFUmVDb0I5VXUvRllqL3dRL0lEbjE4"\
                  "end3SDBLQmNrWU55QncwblpzeGJabStyT21CbGhVMktaUWo4Y"\
                  "m5FK0d6aTZiQ3J2TDNac2JBR0hZbHRKd3Q5SGFONE1sMlVGdHV"\
                  "YRkp2QWl2TDExWjArNUs5NDVQakpybzRGdCtlYXdCT0t4MWx"\
                  "TV2d1YThaKzNPNzdoLytNaTA4Y3hHZHorM0RBRC92VG9tZU9"\
                  "IK0R3blA3NVFKaFdnbWhoRi92UE5SdE1WQTVhQzdIKytGSm04"\
                  "WTVBUTdmS3RYZENvR2xtSUFMMDJjN3FmQytrRkRNQnZlcXNnb"\
                  "nROOFY%3D"

    return wave_height, wave_direction, wave_period


def get_sydney_buoys():

    wave_height = "https://api.manly.hydraulics.works/api.php?format=csv&page=rawdatatable&id=992%2C991&startdate=null&enddate=null&username=publicwww&token=KzZQWmJFbWZzRGVXYWdVTVpYQUpFb3hhb0ttSmhMelFoKzRTTmR0U0lwL0lyVWRmUUdKTzlJRVVVNm1lMTR4dzFxLy90cExuS0NFUmVDb0I5VXUvRllqL3dRL0lEbjE4end3SDBLQmNrWU55QncwblpzeGJabStyT21CbGhVMktaUWo4Ym5FK0d6aTZiQ3J2TDNac2JBR0hZbHRKd3Q5SGFONE1sMlVGdHVYRkp2QWl2TDExWjArNUs5NDVQakpybzRGdCtlYXdCT0t4MWxTV2d1YThaKzNPNzdoLytNaTA4Y3hHZHorM0RBRC92VG9tZU9IK0R3blA3NVFKaFdnbWhoRi92UE5SdE1WQTVhQzdIKytGSm04WTVBUTdmS3RYZENvR2xtSUFMMDJjN3FmQytrRkRNQnZlcXNnbnROOFY%3D"

    wave_direction = "https://api.manly.hydraulics.works/api.php?format=csv&page=rawdatatable&id=993&startdate=null&enddate=null&username=publicwww&token=KzZQWmJFbWZzRGVXYWdVTVpYQUpFb3hhb0ttSmhMelFoKzRTTmR0U0lwL0lyVWRmUUdKTzlJRVVVNm1lMTR4dzFxLy90cExuS0NFUmVDb0I5VXUvRllqL3dRL0lEbjE4end3SDBLQmNrWU55QncwblpzeGJabStyT21CbGhVMktaUWo4Ym5FK0d6aTZiQ3J2TDNac2JBR0hZbHRKd3Q5SGFONE1sMlVGdHVYRkp2QWl2TDExWjArNUs5NDVQakpybzRGdCtlYXdCT0t4MWxTV2d1YThaKzNPNzdoLytNaTA4Y3hHZHorM0RBRC92VG9tZU9IK0R3blA3NVFKaFdnbWhoRi92UE5SdE1WQTVhQzdIKytGSm04WTVBUTdmS3RYZENvR2xtSUFMMDJjN3FmQytrRkRNQnZlcXNnbnROOFY%3D"

    wave_period = "https://api.manly.hydraulics.works/api.php?format=csv&page=rawdatatable&id=994%2C996&startdate=null&enddate=null&username=publicwww&token=KzZQWmJFbWZzRGVXYWdVTVpYQUpFb3hhb0ttSmhMelFoKzRTTmR0U0lwL0lyVWRmUUdKTzlJRVVVNm1lMTR4dzFxLy90cExuS0NFUmVDb0I5VXUvRllqL3dRL0lEbjE4end3SDBLQmNrWU55QncwblpzeGJabStyT21CbGhVMktaUWo4Ym5FK0d6aTZiQ3J2TDNac2JBR0hZbHRKd3Q5SGFONE1sMlVGdHVYRkp2QWl2TDExWjArNUs5NDVQakpybzRGdCtlYXdCT0t4MWxTV2d1YThaKzNPNzdoLytNaTA4Y3hHZHorM0RBRC92VG9tZU9IK0R3blA3NVFKaFdnbWhoRi92UE5SdE1WQTVhQzdIKytGSm04WTVBUTdmS3RYZENvR2xtSUFMMDJjN3FmQytrRkRNQnZlcXNnbnROOFY%3D"

    return wave_height, wave_direction, wave_period
