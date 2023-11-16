from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from tkcalendar import *
import os
from colorama import init, Fore
select = False
select2 = False
ErrorWave = False
ErrorEvent = False
from tkinter import Tk, Button, Frame
import time
from tkinter import ttk
import tkinter as tk
import sys
import queue
import threading
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
textWave=""
simulationWaveRun = False
simulationEventRun = False
import cv2
import pyautogui
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.chrome.options import Options
init(autoreset=True)


while True:
        if ErrorWave == False:

                def simulationWave():
                        while True:
                                try:
                                        textWave = "Wave Simulation starts..."
                                        driver_path = Service("C:\webdrivers\chromedriver.exe")
                                        chromeOptions = Options()
                                        chromeOptions.headless = False

                                        browser = webdriver.Chrome(service=driver_path, options=chromeOptions)

                                        browser.get("https://tadas.afad.gov.tr/map")

                                        kaynak = browser.page_source
                                        soup = BeautifulSoup(kaynak, "html.parser")
                                        time.sleep(15)
                                        tr_number = 0
                                        data_waveNumber = 0
                                        data_waveCode = 0
                                        page = 1
                                        old_page = 1
                                        common_page = 0
                                        tıkla = browser.find_element(By.XPATH, "/html/body/app-root/div/app-login/div/div/div/div[1]/div/div[3]/div/button")
                                        tıkla.click()
                                        time.sleep(15)
                                        next_page = False


                                        while tr_number <= 10:

                                                time.sleep(15)
                                                tr_number = tr_number + 1
                                                common_page = 0
                                                browser.get("https://tadas.afad.gov.tr/list-waveform")
                                                time.sleep(10)

                                                range_input = browser.find_element(By.XPATH, "./html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div/div/div[1]/kendo-datepicker/span/kendo-dateinput/span/input")
                                                value = range_input.get_attribute('aria-valuenow')
                                                range_input.send_keys("01")
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys("00")
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys("00")
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(YEAR)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(MONTH)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(DAY)

                                                time.sleep(5)
                                                range_input = browser.find_element(By.XPATH, "./html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div/div/div[2]/kendo-datepicker/span/kendo-dateinput/span/input")
                                                value = range_input.get_attribute('aria-valuenow')
                                                range_input.send_keys("01")
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys("00")
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys("00")
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(YEAR2)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(MONTH2)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(DAY2)
                                                time.sleep(5)
                                                ara_button = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/button[1]")
                                                ara_button.click()
                                                time.sleep(15)

                                                if next_page is False:

                                                        while common_page < (page-1):

                                                                #time.sleep(10)
                                                                next_page = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/kendo-pager/kendo-pager-next-buttons/a[1]")
                                                                next_page.click()
                                                                time.sleep(2)
                                                                common_page = common_page + 1

                                                else:
                                                        while common_page < page:
                                                                next_page = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/kendo-pager/kendo-pager-next-buttons/a[1]")
                                                                next_page.click()
                                                                time.sleep(3)
                                                                common_page = common_page + 1
                                                                next_page = False
                                                        page = page + 1

                                                time.sleep(15)

                                                if tr_number == 1:
                                                        ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[1]/td[12]/button")
                                                        ham_veri.click()
                                                        time.sleep(40)

                                                        veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[7]/div/button[2]")
                                                        veri_süzgeçleme.click()
                                                        print("Ham veri süzgeçleniyor")
                                                        textWave = "Ham veri süzgeçleniyor"
                                                        time.sleep(40)

                                                        veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                                                        veriyi_işle.click()
                                                        print("Ham veriyi işleniyor")
                                                        textWave="Ham veriyi işleniyor"
                                                        time.sleep(40)

                                                        ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                                                        ham_veriyi_indir.click()
                                                        print("Ham veriyi indirme işlemi gerçekleştiriliyor")
                                                        textWave = "Ham veriyi indirme işlemi gerçekleştiriliyor"
                                                        time.sleep(20)
                                                        next_page = False

                                                elif tr_number == 2:
                                                        ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[2]/td[12]/button")
                                                        ham_veri.click()
                                                        time.sleep(40)

                                                        veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[7]/div/button[2]")
                                                        veri_süzgeçleme.click()
                                                        print("Ham veri süzgeçleniyor")
                                                        textWave = "Ham veri süzgeçleniyor"
                                                        time.sleep(40)

                                                        veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                                                        veriyi_işle.click()
                                                        print("Ham veriyi işleniyor")
                                                        textWave = "Ham veriyi işleniyor"
                                                        time.sleep(40)

                                                        ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                                                        ham_veriyi_indir.click()
                                                        print("Ham veriyi indirme işlemi gerçekleştiriliyor")
                                                        textWave = "Ham veriyi indirme işlemi gerçekleştiriliyor"
                                                        time.sleep(20)
                                                        next_page = False

                                                elif tr_number == 3:
                                                        ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[3]/td[12]/button")
                                                        ham_veri.click()
                                                        time.sleep(40)

                                                        veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[7]/div/button[2]")
                                                        veri_süzgeçleme.click()
                                                        print("Ham veri süzgeçleniyor")
                                                        textWave = "Ham veri süzgeçleniyor"
                                                        time.sleep(40)

                                                        veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                                                        veriyi_işle.click()
                                                        print("Ham veriyi işleniyor")
                                                        textWave = "Ham veriyi işleniyor"
                                                        time.sleep(40)

                                                        ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                                                        ham_veriyi_indir.click()
                                                        print("Ham veriyi indirme işlemi gerçekleştiriliyor")
                                                        textWave = "Ham veriyi indirme işlemi gerçekleştiriliyor"
                                                        time.sleep(20)
                                                        next_page = False

                                                elif tr_number == 4:
                                                        ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[4]/td[12]/button")
                                                        ham_veri.click()
                                                        time.sleep(40)

                                                        veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[7]/div/button[2]")
                                                        veri_süzgeçleme.click()
                                                        print("Ham veri süzgeçleniyor")
                                                        textWave = "Ham veri süzgeçleniyor"
                                                        time.sleep(40)

                                                        veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                                                        veriyi_işle.click()
                                                        print("Ham veriyi işleniyor")
                                                        textWave = "Ham veriyi işleniyor"
                                                        time.sleep(40)

                                                        ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                                                        ham_veriyi_indir.click()
                                                        print("Ham veriyi indirme işlemi gerçekleştiriliyor")
                                                        textWave = "Ham veriyi indirme işlemi gerçekleştiriliyor"
                                                        time.sleep(20)
                                                        next_page = False

                                                elif tr_number == 5:
                                                        ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[5]/td[12]/button")
                                                        ham_veri.click()
                                                        time.sleep(40)

                                                        veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[7]/div/button[2]")
                                                        veri_süzgeçleme.click()
                                                        print("Ham veri süzgeçleniyor")
                                                        textWave = "Ham veri süzgeçleniyor"
                                                        time.sleep(40)

                                                        veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                                                        veriyi_işle.click()
                                                        print("Ham veriyi işleniyor")
                                                        textWave = "Ham veriyi işleniyor"
                                                        time.sleep(40)

                                                        ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                                                        ham_veriyi_indir.click()
                                                        print("Ham veriyi indirme işlemi gerçekleştiriliyor")
                                                        textWave = "Ham veriyi indirme işlemi gerçekleştiriliyor"
                                                        time.sleep(20)
                                                        next_page = False

                                                elif tr_number == 6:
                                                        ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[6]/td[12]/button")
                                                        ham_veri.click()
                                                        time.sleep(40)

                                                        veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[7]/div/button[2]")
                                                        veri_süzgeçleme.click()
                                                        print("Ham veri süzgeçleniyor")
                                                        textWave = "Ham veri süzgeçleniyor"
                                                        time.sleep(40)

                                                        veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                                                        veriyi_işle.click()
                                                        print("Ham veriyi işleniyor")
                                                        textWave = "Ham veriyi işleniyor"
                                                        time.sleep(40)

                                                        ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                                                        ham_veriyi_indir.click()
                                                        print("Ham veriyi indirme işlemi gerçekleştiriliyor")
                                                        textWave = "Ham veriyi indirme işlemi gerçekleştiriliyor"
                                                        time.sleep(20)
                                                        next_page = False

                                                elif tr_number == 7:
                                                        ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[7]/td[12]/button")
                                                        ham_veri.click()
                                                        time.sleep(40)

                                                        veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[7]/div/button[2]")
                                                        veri_süzgeçleme.click()
                                                        print("Ham veri süzgeçleniyor")
                                                        textWave = "Ham veri süzgeçleniyor"
                                                        time.sleep(40)

                                                        veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                                                        veriyi_işle.click()
                                                        print("Ham veriyi işleniyor")
                                                        textWave = "Ham veriyi işleniyor"
                                                        time.sleep(40)

                                                        ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                                                        ham_veriyi_indir.click()
                                                        print("Ham veriyi indirme işlemi gerçekleştiriliyor")
                                                        textWave = "Ham veriyi indirme işlemi gerçekleştiriliyor"
                                                        time.sleep(20)
                                                        next_page = False

                                                elif tr_number == 8:
                                                        ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[8]/td[12]/button")
                                                        ham_veri.click()
                                                        time.sleep(40)

                                                        veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[7]/div/button[2]")
                                                        veri_süzgeçleme.click()
                                                        print("Ham veri süzgeçleniyor")
                                                        textWave = "Ham veri süzgeçleniyor"
                                                        time.sleep(40)

                                                        veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                                                        veriyi_işle.click()
                                                        print("Ham veriyi işleniyor")
                                                        textWave = "Ham veriyi işleniyor"
                                                        time.sleep(40)

                                                        ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                                                        ham_veriyi_indir.click()
                                                        print("Ham veriyi indirme işlemi gerçekleştiriliyor")
                                                        textWave = "Ham veriyi indirme işlemi gerçekleştiriliyor"
                                                        time.sleep(20)
                                                        next_page = False

                                                elif tr_number == 9:
                                                        ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[9]/td[12]/button")
                                                        ham_veri.click()
                                                        time.sleep(40)

                                                        veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[7]/div/button[2]")
                                                        veri_süzgeçleme.click()
                                                        print("Ham veri süzgeçleniyor")
                                                        textWave = "Ham veri süzgeçleniyor"
                                                        time.sleep(40)

                                                        veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                                                        veriyi_işle.click()
                                                        print("Ham veriyi işleniyor")
                                                        textWave = "Ham veriyi işleniyor"
                                                        time.sleep(40)

                                                        ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                                                        ham_veriyi_indir.click()
                                                        print("Ham veriyi indirme işlemi gerçekleştiriliyor")
                                                        textWave = "Ham veriyi indirme işlemi gerçekleştiriliyor"
                                                        time.sleep(20)
                                                        next_page = False

                                                else:
                                                        ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[10]/td[12]/button")
                                                        ham_veri.click()
                                                        time.sleep(40)

                                                        veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[7]/div/button[2]")
                                                        veri_süzgeçleme.click()
                                                        print("Ham veri süzgeçleniyor")
                                                        textWave = "Ham veri süzgeçleniyor"
                                                        time.sleep(40)

                                                        veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                                                        veriyi_işle.click()
                                                        print("Ham veriyi işleniyor")
                                                        textWave = "Ham veriyi işleniyor"
                                                        time.sleep(40)

                                                        ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                                                        ham_veriyi_indir.click()
                                                        print("Ham veriyi indirme işlemi gerçekleştiriliyor")
                                                        textWave = "Ham veriyi indirme işlemi gerçekleştiriliyor"
                                                        time.sleep(20)
                                                        tr_number = 0
                                                        next_page = True
                                                        print("Ham veri indirildi")

                                                def print_error_message(message):
                                                        print("\033[91mError: {}\033[0m".format(message))

                                except Exception as e:
                                        # Handle the error here
                                        print(f"An error occurred in Waveform simulation: {str(e)}")
                                        print(Fore.RED + "Hata Mesajı:", str(e))
                                        textWave = str(e)

                                finally:
                                        if browser:
                                                browser.quit()
        if ErrorEvent == False:
                def simulationEvent():
                        while True:
                                try:
                                        driver_path = "C:\webdrivers\chromedriver.exe"
                                        browser = webdriver.Chrome(driver_path)

                                        browser.get("https://tadas.afad.gov.tr/map")

                                        kaynak = browser.page_source
                                        soup = BeautifulSoup(kaynak, "html.parser")
                                        time.sleep(15)
                                        tr_number = 0
                                        data_EventNumber = 0
                                        data_EvenetCode = 0
                                        page = 1
                                        old_page = 1
                                        common_page = 0
                                        tıkla = browser.find_element(By.XPATH, "/html/body/app-root/div/app-login/div/div/div/div[1]/div/div[3]/div/button")
                                        tıkla.click()
                                        time.sleep(15)
                                        next_page = False


                                        while tr_number <= 10:

                                                tr_number = tr_number + 1
                                                common_page = 0
                                                browser.get("https://tadas.afad.gov.tr/list-event")
                                                time.sleep(15)

                                                range_input = browser.find_element(By.XPATH, "./html/body/app-root/div[2]/app-list-event/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div[1]/kendo-datepicker/span/kendo-dateinput/span/input")
                                                value = range_input.get_attribute('aria-valuenow')
                                                range_input.send_keys("01")
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys("00")
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys("00")
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(YEAR)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(MONTH)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(DAY)

                                                time.sleep(5)
                                                range_input = browser.find_element(By.XPATH, "./html/body/app-root/div[2]/app-list-event/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/kendo-datepicker/span/kendo-dateinput/span/input")
                                                value = range_input.get_attribute('aria-valuenow')
                                                range_input.send_keys("01")
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys("00")
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys("00")
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(YEAR2)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(MONTH2)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(Keys.ARROW_LEFT)
                                                range_input.send_keys(DAY2)

                                                ara_button = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-event/div/div/div/div/div/div/div[1]/div[3]/div/button[1]")
                                                ara_button.click()
                                                time.sleep(25)
                                                #time.sleep(10)

                                                if next_page is False:

                                                        while common_page < (page-1):

                                                                #time.sleep(10)
                                                                next_page = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-event/div/div/div/div/div/div/div[3]/div/kendo-grid/kendo-pager/kendo-pager-next-buttons/a[1]/span")
                                                                next_page.click()
                                                                #time.sleep(5)
                                                                common_page = common_page + 1

                                                else:
                                                        while common_page < page:
                                                                next_page = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-event/div/div/div/div/div/div/div[3]/div/kendo-grid/kendo-pager/kendo-pager-next-buttons/a[1]/span")
                                                                next_page.click()
                                                                #time.sleep(3)
                                                                common_page = common_page + 1
                                                                next_page = False
                                                        page = page + 1

                                                #time.sleep(15)

                                                if tr_number == 1:
                                                        veri_Detay = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-event/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[1]/td[11]/button")
                                                        time.sleep(7)
                                                        veri_Detay.click()
                                                        time.sleep(15)

                                                        records_tab = browser.find_element(By.XPATH, "//a[contains(text(), 'Kayıtlar')]")
                                                        actions = ActionChains(browser)
                                                        actions.move_to_element(records_tab).click().perform()
                                                        time.sleep(12)

                                                        tümünü_seç = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[1]/kendo-grid/div/div/div/table/thead/tr/th[1]/input")
                                                        time.sleep(10)
                                                        tümünü_seç.click()
                                                        time.sleep(15)

                                                        ivme_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[3]/div/form/div/div[5]/div/button")
                                                        time.sleep(10)
                                                        ivme_indir.click()
                                                        time.sleep(15)
                                                        next_page = False
                                                        data_EventNumber = data_EventNumber + 1
                                                        print("Downloaded Event data: ", data_EventNumber)

                                                elif tr_number == 2:
                                                        ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-event/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[2]/td[11]/button")
                                                        time.sleep(7)
                                                        ham_veri.click()
                                                        time.sleep(15)

                                                        records_tab = browser.find_element(By.XPATH, "//a[contains(@href, '#records')]")
                                                        time.sleep(10)
                                                        records_tab.click()
                                                        time.sleep(15)

                                                        tümünü_seç = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[1]/kendo-grid/div/div/div/table/thead/tr/th[1]/input")
                                                        time.sleep(10)
                                                        tümünü_seç.click()
                                                        time.sleep(15)

                                                        ivme_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[3]/div/form/div/div[5]/div/button")
                                                        time.sleep(10)
                                                        ivme_indir.click()
                                                        time.sleep(15)
                                                        next_page = False
                                                        data_EventNumber = data_EventNumber + 1
                                                        print("Downloaded Event data: ", data_EventNumber)

                                                elif tr_number == 3:
                                                        ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-event/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[3]/td[11]/button")
                                                        time.sleep(7)
                                                        ham_veri.click()
                                                        time.sleep(15)

                                                        records_tab = browser.find_element(By.XPATH, "//a[contains(@href, '#records')]")
                                                        time.sleep(10)
                                                        records_tab.click()
                                                        time.sleep(15)

                                                        tümünü_seç = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[1]/kendo-grid/div/div/div/table/thead/tr/th[1]/input")
                                                        time.sleep(10)
                                                        tümünü_seç.click()
                                                        time.sleep(15)

                                                        ivme_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[3]/div/form/div/div[5]/div/button")
                                                        time.sleep(10)
                                                        ivme_indir.click()
                                                        time.sleep(15)
                                                        next_page = False
                                                        data_EventNumber = data_EventNumber + 1
                                                        print("Downloaded Event data: ", data_EventNumber)

                                                elif tr_number == 4:
                                                        ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-event/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[4]/td[11]/button")
                                                        time.sleep(7)
                                                        ham_veri.click()
                                                        time.sleep(15)

                                                        records_tab = browser.find_element(By.XPATH, "//a[contains(@href, '#records')]")
                                                        time.sleep(10)
                                                        records_tab.click()
                                                        time.sleep(15)

                                                        tümünü_seç = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[1]/kendo-grid/div/div/div/table/thead/tr/th[1]/input")
                                                        time.sleep(10)
                                                        tümünü_seç.click()
                                                        time.sleep(15)

                                                        ivme_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[3]/div/form/div/div[5]/div/button")
                                                        time.sleep(10)
                                                        ivme_indir.click()
                                                        time.sleep(15)
                                                        next_page = False
                                                        data_EventNumber = data_EventNumber + 1
                                                        print("Downloaded Event data: ", data_EventNumber)

                                                elif tr_number == 5:
                                                        ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-event/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[5]/td[11]/button")
                                                        time.sleep(7)
                                                        ham_veri.click()
                                                        time.sleep(15)

                                                        records_tab = browser.find_element(By.XPATH, "//a[contains(@href, '#records')]")
                                                        time.sleep(10)
                                                        records_tab.click()
                                                        time.sleep(15)

                                                        tümünü_seç = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[1]/kendo-grid/div/div/div/table/thead/tr/th[1]/input")
                                                        time.sleep(10)
                                                        tümünü_seç.click()
                                                        time.sleep(15)

                                                        ivme_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[3]/div/form/div/div[5]/div/button")
                                                        time.sleep(10)
                                                        ivme_indir.click()
                                                        time.sleep(15)
                                                        next_page = False
                                                        data_EventNumber = data_EventNumber + 1
                                                        print("Downloaded Event data: ", data_EventNumber)

                                                elif tr_number == 6:
                                                        ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-event/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[6]/td[11]/button")
                                                        time.sleep(7)
                                                        ham_veri.click()
                                                        time.sleep(15)

                                                        records_tab = browser.find_element(By.XPATH, "//a[contains(@href, '#records')]")
                                                        time.sleep(10)
                                                        records_tab.click()
                                                        time.sleep(15)

                                                        tümünü_seç = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[1]/kendo-grid/div/div/div/table/thead/tr/th[1]/input")
                                                        time.sleep(10)
                                                        tümünü_seç.click()
                                                        time.sleep(15)

                                                        ivme_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[3]/div/form/div/div[5]/div/button")
                                                        time.sleep(10)
                                                        ivme_indir.click()
                                                        time.sleep(15)
                                                        next_page = False
                                                        data_EventNumber = data_EventNumber + 1
                                                        print("Downloaded Event data: ", data_EventNumber)

                                                elif tr_number == 7:
                                                        ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-event/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[7]/td[11]/button")
                                                        time.sleep(7)
                                                        ham_veri.click()
                                                        time.sleep(15)

                                                        records_tab = browser.find_element(By.XPATH, "//a[contains(@href, '#records')]")
                                                        time.sleep(10)
                                                        records_tab.click()
                                                        time.sleep(15)

                                                        tümünü_seç = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[1]/kendo-grid/div/div/div/table/thead/tr/th[1]/input")
                                                        time.sleep(10)
                                                        tümünü_seç.click()
                                                        time.sleep(15)

                                                        ivme_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[3]/div/form/div/div[5]/div/button")
                                                        time.sleep(10)
                                                        ivme_indir.click()
                                                        time.sleep(15)
                                                        next_page = False
                                                        data_EventNumber = data_EventNumber + 1
                                                        print("Downloaded Event data: ", data_EventNumber)

                                                elif tr_number == 8:
                                                        ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-event/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[8]/td[11]/button")
                                                        time.sleep(7)
                                                        ham_veri.click()
                                                        time.sleep(15)

                                                        records_tab = browser.find_element(By.XPATH, "//a[contains(@href, '#records')]")
                                                        time.sleep(10)
                                                        records_tab.click()
                                                        time.sleep(15)

                                                        tümünü_seç = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[1]/kendo-grid/div/div/div/table/thead/tr/th[1]/input")
                                                        time.sleep(10)
                                                        tümünü_seç.click()
                                                        time.sleep(15)

                                                        ivme_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[3]/div/form/div/div[5]/div/button")
                                                        time.sleep(10)
                                                        ivme_indir.click()
                                                        time.sleep(15)
                                                        next_page = False
                                                        data_EventNumber = data_EventNumber + 1
                                                        print("Downloaded Event data: ", data_EventNumber)

                                                elif tr_number == 9:
                                                        ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-event/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[9]/td[11]/button")
                                                        time.sleep(7)
                                                        ham_veri.click()
                                                        time.sleep(15)

                                                        records_tab = browser.find_element(By.XPATH, "//a[contains(@href, '#records')]")
                                                        time.sleep(10)
                                                        records_tab.click()
                                                        time.sleep(15)

                                                        tümünü_seç = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[1]/kendo-grid/div/div/div/table/thead/tr/th[1]/input")
                                                        time.sleep(10)
                                                        tümünü_seç.click()
                                                        time.sleep(15)

                                                        ivme_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[3]/div/form/div/div[5]/div/button")
                                                        time.sleep(10)
                                                        ivme_indir.click()
                                                        time.sleep(15)
                                                        next_page = False
                                                        data_EventNumber = data_EventNumber + 1
                                                        print("Downloaded Event data: ", data_EventNumber)

                                                else:
                                                        ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-event/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[10]/td[11]/button")
                                                        time.sleep(7)
                                                        ham_veri.click()
                                                        time.sleep(15)

                                                        records_tab = browser.find_element(By.XPATH, "//a[contains(@href, '#records')]")
                                                        time.sleep(10)
                                                        records_tab.click()
                                                        time.sleep(15)

                                                        tümünü_seç = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[1]/kendo-grid/div/div/div/table/thead/tr/th[1]/input")
                                                        time.sleep(10)
                                                        tümünü_seç.click()
                                                        time.sleep(15)

                                                        ivme_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-event-detail/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[3]/div/form/div/div[5]/div/button")
                                                        time.sleep(10)
                                                        ivme_indir.click()
                                                        time.sleep(15)
                                                        next_page = False
                                                        tr_number = 0
                                                        time.sleep(7)
                                                        next_page = True
                                                        data_EventNumber = data_EventNumber + 1
                                                        print("Downloaded Event data: ", data_EventNumber)

                                        break
                                except Exception as e:
                                        # Handle the error here
                                        print(f"An error occurred: {str(e)}")
                                        browser.quit()



                if ErrorEvent is False and ErrorWave is False:

                        root = Tk()
                        root.title('Download of Raw Data')
                        root.geometry('500x750')

                        status = False

                        cal = Calendar(root, selectmode="day", year=2018, month=12, day=1)
                        cal.pack(pady=20)
                        date_label = ttk.Label(root, text="")
                        date_label.pack()
                        selected_date = cal.selection_get().strftime("%Y-%m-%d")
                        date_label.config(text=f"Selected Date: {selected_date}")

                        YEAR = int(selected_date[:4])
                        MONTH = int(selected_date[5:7])
                        DAY = int(selected_date[-2:])


                        def print_selected_date(event=None):
                                global YEAR, MONTH, DAY  # indicate that you want to modify the global variables
                                selected_date = cal.selection_get().strftime("%Y-%m-%d")
                                date_label.config(text=f"Selected Date: {selected_date}")
                                YEAR = int(selected_date[:4])  # update the YEAR variable with the selected year
                                MONTH = int(selected_date[5:7])
                                DAY = int(selected_date[-2:])


                        print_button = ttk.Button(root, text="Print selected date", command=print_selected_date)
                        print_button.pack(pady=10)

                        if select is False:
                                date_label.config(text="No date selected")

                        cal2 = Calendar(root, selectmode="day")
                        cal2.pack(pady=20)
                        date_label2 = ttk.Label(root, text="")
                        date_label2.pack()
                        selected_date2 = cal2.selection_get().strftime("%Y-%m-%d")
                        date_label2.config(text=f"Selected Date: {selected_date}")

                        YEAR2 = int(selected_date2[:4])
                        MONTH2 = int(selected_date2[5:7])
                        DAY2 = int(selected_date2[-2:])


                        def print_selected_endDate(event=None):
                                global YEAR2, MONTH2, DAY2  # indicate that you want to modify the global variables
                                selected_date2 = cal2.selection_get().strftime("%Y-%m-%d")
                                date_label2.config(text=f"Selected Date: {selected_date2}")
                                YEAR2 = int(selected_date2[:4])  # update the YEAR variable with the selected year
                                MONTH2 = int(selected_date2[5:7])
                                DAY2 = int(selected_date2[-2:])


                        print_button2 = ttk.Button(root, text="Print selected date", command=print_selected_endDate)
                        print_button2.pack(pady=10)

                        if select2 is False:
                                date_label2.config(text="No date selected")

                        button_Waveforms = Button(root, text="Waveforms")
                        button_Waveforms_S = Button(root, text="STOP")
                        button_Events = Button(root, text="Events ")
                        button_Events_S = Button(root, text="STOP")

                        def startAppW():
                                global status
                                status = True
                                os.system("C:/Users/berke/PycharmProjects/AfadData/main.py")
                                exeWaveforms.config(text='STOP', command=stopAppW)
                                simulationWaveRun = True
                                terminate_gui()
                                if ErrorWave == False:
                                        simulationWave()
                                else:
                                        #sys.exit(1)
                                        simulationWave()


                        def stopAppW():
                                global status
                                status = False
                                exeWaveforms.config(text="Waveforms", command=startAppW)
                                simulationWave()
                                otomatik_tikla_W_Stop()
                                otomatik_tikla_W()

                        def startAppE():
                                global status
                                status = True
                                os.system("C:/Users/berke/PycharmProjects/AfadData/main.py")
                                exeEvents.config(text='STOP', command=stopAppE)
                                simulationEventRun = True
                                terminate_gui()
                                simulationEvent()


                                if ErrorEvent == False:
                                        simulationEvent()




                        def stopAppE():
                                global status
                                status = False
                                exeEvents.config(text="Events", command=startAppE)
                                simulationEvent()
                                otomatik_tikla_E_Stop()
                                otomatik_tikla_E()


                        global exeWaveforms
                        exeWaveforms = Button(root, text='Waveforms', command=startAppW, width=20, height=2)
                        exeWaveforms.pack(pady=40)

                        global exeEvents
                        exeEvents = Button(root, text='Events', command=startAppE, width=20, height=2)
                        exeEvents.pack()

                        def otomatik_tikla_E_Stop():
                                button_Events_S.configure(command=otomatik_tikla_E_Stop)
                        def otomatik_tikla_E():
                                button_Events.configure(command=otomatik_tikla_E)
                        def otomatik_tikla_W():
                                button_Waveforms.configure(command=otomatik_tikla_W)
                        def otomatik_tikla_W_Stop():
                                button_Waveforms_S.configure(command=otomatik_tikla_W_Stop)
                        def terminate_gui():

                                root.destroy()
                                print("Error: GUI has already been destroyed.")





                        class ConsoleGUI(tk.Tk):
                                def __init__(self):
                                        super().__init__()
                                        self.title("Console Output to GUI")
                                        self.geometry("400x300")

                                        self.text_area = tk.Text(self, wrap="word")
                                        self.text_area.pack(fill="both", expand=True)


                                        self.output_queue = queue.Queue()


                                        sys.stdout = self


                                        self.update_thread = threading.Thread(target=self.update_gui)
                                        self.update_thread.daemon = True
                                        self.update_thread.start()

                                def write(self, text):

                                        self.output_queue.put(text)

                                def update_gui(self):
                                        while True:

                                                if not self.output_queue.empty():
                                                        text = self.output_queue.get()

                                                        self.text_area.insert(tk.END, text)
                                                        self.text_area.see(tk.END)


                                                self.update()

                                                self.after(100)


                        def run_program():

                                print("Running program...")
                                if simulationWaveRun == True:
                                        simulationWave()
                                if simulationEventRun == True:
                                        simulationEvent()
                        if __name__ == "__main__":
                                gui = ConsoleGUI()


                                program_thread = threading.Thread(target=run_program)
                                program_thread.start()


                                gui.mainloop()
                                terminate_gui()

