# Programming by Sh4d0wE4
# Herhangi bir websitenin kaynak kodunu dump edip, bir klasore kayıt eden python programi.
# A python program that dumps the source code of any website and saves it to a folder.

import requests
import os
import subprocess
import time

os.system("clear")

def main():
    print("DumpSourceC0de_V1")
    print("Programming by Sh4d0wE4")
    input()
    
    url = input("Lutfen verisini cekmek istediginiz sitenin\nURL'sini girin: ")
    request(url)
    print("Program basariyla calisti..")

def request(url):
    try:
        r = requests.get(url)
        statuscode = r.status_code

        if statuscode == 200:
            print("HTTP 200 OK")
            time.sleep(1)
            print("Lutfen biraz bekleyin..")
            time.sleep(2)
            print("\n")

            print("Veriler cekiliyor..")
            time.sleep(2)
            f = open("text.html", "w")
            f.write(str(r.text))
            f.close()
            print("Veriler basariyla yazdirildi..")
            time.sleep(1)
            print("Dosya aciliyor...")
            subprocess.run(['code', 'text.html'])
            time.sleep(2)
            print("Dosya basariyla acildi..")
            time.sleep(2)
            os.system("clear")
        
        if statuscode == 404:
            print("İnternet sitesi bulunamadi.")
        
        if statuscode == 403:
            print("İnternet sitesine erisim yetkiniz yok.")
        
        servererrors = [501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512]
        for server in servererrors:
            if statuscode == server:
                print("Sunucu hatasi !")
    
    except:
        print("Bir hata olustu!")

main()
