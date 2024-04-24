from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
from selenium.webdriver.remote.remote_connection import LOGGER as seleniumLogger
from urllib3.connectionpool import log as urlliblogger
import requests  
import pandas as pd
import sys
from termcolor import colored

def Tektektek():

    def authSm(c):
        user = ["user1", "user2", "user3", "user4", "user5", "user6", "user7", "user8"]
        passwd = ["passwd1", "passwd2", "passwd3", "passwd4", "passwd5", "passwd6", "passwd7", "passwd8"]#password dan user asli sudah tidak ditampakkan lagi
        devSupermicro = pd.read_csv('devSupermicro1.csv')
        lholho = devSupermicro.iloc[c].to_string(index=False)
        nama = lholho.split('\n')
        naaa = nama[0]
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--log-level=3')
        options.add_argument('--disable-javascript')
        options.add_argument('--disable-notifications')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-gpu')
        options.set_capability('javascript.enabled', False)
        options.add_argument('--disable-plugins')
        options.add_argument("--disable-infobars")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_driver = '/chromedriver_win32'
        driver = webdriver.Chrome(chrome_driver, options=options)
        driver.set_window_position(100, 100)
        print("\n")
        driver.get(enum)
        time.sleep(1)
        ai = 0
        for cred1, cred2 in zip(user,passwd):
            ai += 1
            print(colored(f"Tes Auth ke {ai}","cyan"))
            print("Target: ",naaa)
            print("IP    : ",nakniknuk)
                
            lapo = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/input[1]')#titik injek1
            lapo.send_keys(cred1)
            
            lapo = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/input[2]')#titik injek2
            lapo.send_keys(cred2)
            maeng = driver.current_url
            lapo = driver.find_element(By.XPATH,'//*[@id="login_word"]')
            lapo.click()
            time.sleep(3)
            anjay = driver.current_url
            time.sleep(3)
            if anjay != maeng and sc.status_code == 200:
                driver.switch_to.alert.dismiss()
                driver.quit()
                print(colored(f"Auth menggunakan akun {cred1} sukses\n", "green"))
            elif anjay == maeng and sc.status_code == 200:
                print(colored(f"Auth menggunakan akun {cred1} gagal\n", "red"))
            elif anjay == maeng and sc.status_code != 200:
                print(colored(f"Silahkan cek koneksi terlebih dahulu\n", "red"))
            else:
                print(colored(f"Auth menggunakan akun {cred1} gagal\n", "red"))
                
    seleniumLogger.setLevel(logging.ERROR)
    urlliblogger.setLevel(logging.ERROR)
    if len(sys.argv) < 2:
        print("Penggunaan: bulkauthtester.py run")
    elif str(sys.argv[1]) == "run":
        i=0
        c=0
        ipSupermicro = pd.read_csv('ipSupermicro1.csv')#Siapkan list ip yang ingin dites formnya
        ipS = ipSupermicro.shape[0]
        for tektek in range(ipS):
            i +=1
            alamat = ipSupermicro.iloc[i]['target']
            if pd.notnull(alamat):
                tektek = alamat.split(',')
                for url in tektek:
                    url = url.strip()
                    url2 = "http://" + url
                    url3 = url + ":80"
                    nakniknuk = url
                    c+=1
                    try:
                        sc = requests.get(url2)
                        if sc.status_code == 200 :
                            enum = url2
                            authSm(c)
                        else:
                            cek2 = url3
                            sc = requests.get(cek2)
                            if sc.status_code == 200 :
                                enum = url3
                                authSm(c)
                    except requests.exceptions.ConnectionError:
                        print(f"\n{nakniknuk}")
                        print(colored("IP tidak bisa di kunjungi bosqiuu :V\n","red"))
                    continue
    else:
        print("Inputan tidak jelas, program auto close")
Tektektek()
