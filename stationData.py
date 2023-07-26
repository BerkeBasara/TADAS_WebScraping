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
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
textWave=""
simulationWaveRun = False
simulationEventRun = False
init(autoreset=True)
next_page = False
tr_number=0
while True:
        try:



                textWave = "Wave Simulation starts..."
                driver_path = "C:\webdrivers\chromedriver.exe"
                browser = webdriver.Chrome(driver_path)

                browser.get("https://tadas.afad.gov.tr/map")

                kaynak = browser.page_source
                soup = BeautifulSoup(kaynak, "html.parser")
                time.sleep(15)

                tıkla = browser.find_element(By.XPATH, "./html/body/app-root/div/app-login/div/div/div/div[1]/div/div[3]/div/button")  #Burada guest e tıklandı
                tıkla.click()
                time.sleep(10)
                data_waveNumber = 0
                data_waveCode = 0
                tr_number = 0
                page = 1
                old_page = 1
                common_page = 0
                next_page = False

                while tr_number <= 10:
                        tr_number = tr_number + 1
                        common_page = 0
                        browser.get("https://tadas.afad.gov.tr/list-station")
                        time.sleep(15)

                        if next_page is False:

                            while common_page < (page - 1):
                                # time.sleep(10)
                                next_page = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/kendo-pager/kendo-pager-next-buttons/a[1]/span")
                                next_page.click()
                                time.sleep(5)
                                common_page = common_page + 1

                        else:
                            while common_page < page:
                                next_page = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/kendo-pager/kendo-pager-next-buttons/a[1]/span")
                                next_page.click()
                                # time.sleep(3)
                                common_page = common_page + 1
                                next_page = False
                            page = page + 1

                        time.sleep(30)

                        if tr_number == 1:

                            station = browser.find_element(By.XPATH, "./html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/div[2]/ul/li[2]/a")  # Burada station e tıklandı
                            station.click()
                            time.sleep(15)

                            station_search = browser.find_element(By.XPATH, "/html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/div[2]/ul/li[2]/ul/li/a")  # Burada station/search e tıklandı
                            station_search.click()
                            time.sleep(15)

                            search_ = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[1]/div[3]/div/button[1]")  # search işlemi gerçekleştirildi
                            search_.click()
                            time.sleep(15)

                            Vs30_button = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/div/div/table/thead/tr/th[8]/a")
                            Vs30_button.click()
                            Vs30_button.click()
                            time.sleep(15)

                            station_detail = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[1]/td[12]/button")
                            station_detail.click()
                            time.sleep(15)
                            kod_element = browser.find_element(By.TAG_NAME, "h3")
                            kod_numarasi = kod_element.text.split(":")[1].strip()

                            h3_element = browser.find_element(By.TAG_NAME, "h3")
                            text = h3_element.text

                            jeofizik_data = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[7]/a")
                            jeofizik_data.click()
                            time.sleep(10)
                            next_page = False
                            if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item")) == 0:
                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()

                                if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.pdf']")) == 0:
                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)
                                else:
                                    pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute("href")
                                    browser.get(pdf_link)
                                    time.sleep(15)
                                    pdf_url = browser.current_url
                                    file_name = f'TK.{kod_numarasi}.pdf'
                                    file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                    response = requests.get(pdf_url)
                                    with open(file_path, 'wb') as file:
                                        file.write(response.content)


                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)
                            else:


                                zip_elements = browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.zip']")


                                for zip_element in zip_elements:
                                    zip_link = zip_element.get_attribute("href")
                                    zip_element.click()
                                    time.sleep(15)
                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()
                                time.sleep(15)

                                pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute("href")
                                browser.get(pdf_link)
                                time.sleep(15)
                                pdf_url = browser.current_url
                                file_name = f'TK.{kod_numarasi}.pdf'
                                file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                response = requests.get(pdf_url)
                                with open(file_path, 'wb') as file:
                                    file.write(response.content)

                                browser.get("https://tadas.afad.gov.tr/list-station")
                                time.sleep(15)

                        elif tr_number == 2:

                            station = browser.find_element(By.XPATH, "./html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/div[2]/ul/li[2]/a")  # Burada station e tıklandı
                            station.click()
                            time.sleep(15)

                            station_search = browser.find_element(By.XPATH, "/html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/div[2]/ul/li[2]/ul/li/a")  # Burada station/search e tıklandı
                            station_search.click()
                            time.sleep(15)

                            search_ = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[1]/div[3]/div/button[1]")  # search işlemi gerçekleştirildi
                            search_.click()
                            time.sleep(15)

                            Vs30_button = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/div/div/table/thead/tr/th[8]/a")
                            Vs30_button.click()
                            Vs30_button.click()
                            time.sleep(15)

                            station_detail = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[2]/td[12]/button")
                            station_detail.click()
                            time.sleep(15)
                            kod_element = browser.find_element(By.TAG_NAME, "h3")
                            kod_numarasi = kod_element.text.split(":")[1].strip()
                            h3_element = browser.find_element(By.TAG_NAME, "h3")
                            text = h3_element.text

                            jeofizik_data = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[7]/a")
                            jeofizik_data.click()
                            time.sleep(15)
                            next_page = False

                            if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item")) == 0:
                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()

                                if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.pdf']")) == 0:
                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)
                                else:
                                    pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute("href")
                                    browser.get(pdf_link)
                                    time.sleep(15)
                                    pdf_url = browser.current_url
                                    file_name = f'TK.{kod_numarasi}.pdf'
                                    file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                    response = requests.get(pdf_url)
                                    with open(file_path, 'wb') as file:
                                        file.write(response.content)

                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)

                            else:


                                zip_elements = browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.zip']")


                                for zip_element in zip_elements:
                                    zip_link = zip_element.get_attribute("href")
                                    zip_element.click()
                                    time.sleep(15)
                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()
                                time.sleep(15)

                                pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute("href")
                                browser.get(pdf_link)
                                time.sleep(15)
                                pdf_url = browser.current_url
                                file_name = f'TK.{kod_numarasi}.pdf'
                                file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                response = requests.get(pdf_url)
                                with open(file_path, 'wb') as file:
                                    file.write(response.content)

                                browser.get("https://tadas.afad.gov.tr/list-station")
                                time.sleep(15)
                        elif tr_number == 3:

                            station = browser.find_element(By.XPATH, "./html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/div[2]/ul/li[2]/a")  # Burada station e tıklandı
                            station.click()
                            time.sleep(15)

                            station_search = browser.find_element(By.XPATH, "/html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/div[2]/ul/li[2]/ul/li/a")  # Burada station/search e tıklandı
                            station_search.click()
                            time.sleep(15)

                            search_ = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[1]/div[3]/div/button[1]")  # search işlemi gerçekleştirildi
                            search_.click()
                            time.sleep(15)

                            Vs30_button = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/div/div/table/thead/tr/th[8]/a")
                            Vs30_button.click()
                            Vs30_button.click()
                            time.sleep(15)

                            station_detail = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[3]/td[12]/button")
                            station_detail.click()
                            time.sleep(15)
                            kod_element = browser.find_element(By.TAG_NAME, "h3")
                            kod_numarasi = kod_element.text.split(":")[1].strip()
                            h3_element = browser.find_element(By.TAG_NAME, "h3")
                            text = h3_element.text

                            jeofizik_data = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[7]/a")
                            jeofizik_data.click()
                            time.sleep(15)
                            next_page = False

                            if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item")) == 0:
                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()

                                if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.pdf']")) == 0:
                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)
                                else:
                                    pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute("href")
                                    browser.get(pdf_link)
                                    time.sleep(15)
                                    pdf_url = browser.current_url
                                    file_name = f'TK.{kod_numarasi}.pdf'
                                    file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                    response = requests.get(pdf_url)
                                    with open(file_path, 'wb') as file:
                                        file.write(response.content)

                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)

                            else:


                                zip_elements = browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.zip']")


                                for zip_element in zip_elements:
                                    zip_link = zip_element.get_attribute("href")
                                    zip_element.click()

                                    time.sleep(15)
                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()
                                time.sleep(15)

                                pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute("href")
                                browser.get(pdf_link)
                                time.sleep(10)
                                pdf_url = browser.current_url
                                file_name = f'TK.{kod_numarasi}.pdf'
                                file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                response = requests.get(pdf_url)
                                with open(file_path, 'wb') as file:
                                    file.write(response.content)

                                browser.get("https://tadas.afad.gov.tr/list-station")
                                time.sleep(15)
                        elif tr_number == 4:

                            station = browser.find_element(By.XPATH, "./html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/div[2]/ul/li[2]/a")  # Burada station e tıklandı
                            station.click()
                            time.sleep(15)

                            station_search = browser.find_element(By.XPATH, "/html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/div[2]/ul/li[2]/ul/li/a")  # Burada station/search e tıklandı
                            station_search.click()
                            time.sleep(15)

                            search_ = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[1]/div[3]/div/button[1]")  # search işlemi gerçekleştirildi
                            search_.click()
                            time.sleep(15)

                            Vs30_button = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/div/div/table/thead/tr/th[8]/a")
                            Vs30_button.click()
                            Vs30_button.click()
                            time.sleep(15)

                            station_detail = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[4]/td[12]/button")
                            station_detail.click()
                            time.sleep(15)
                            h3_element = browser.find_element(By.TAG_NAME, "h3")
                            text = h3_element.text
                            kod_element = browser.find_element(By.TAG_NAME, "h3")
                            kod_numarasi = kod_element.text.split(":")[1].strip()
                            jeofizik_data = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[7]/a")
                            jeofizik_data.click()
                            time.sleep(15)
                            next_page = False

                            if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item")) == 0:
                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()

                                if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.pdf']")) == 0:
                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)
                                else:
                                    pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute("href")
                                    browser.get(pdf_link)
                                    time.sleep(15)
                                    pdf_url = browser.current_url
                                    file_name = f'TK.{kod_numarasi}.pdf'
                                    file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                    response = requests.get(pdf_url)
                                    with open(file_path, 'wb') as file:
                                        file.write(response.content)

                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)

                            else:


                                zip_elements = browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.zip']")


                                for zip_element in zip_elements:
                                    zip_link = zip_element.get_attribute("href")
                                    zip_element.click()

                                    time.sleep(15)
                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()
                                time.sleep(15)

                                pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute("href")
                                browser.get(pdf_link)
                                time.sleep(15)
                                pdf_url = browser.current_url
                                file_name = f'TK.{kod_numarasi}.pdf'
                                file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                response = requests.get(pdf_url)
                                with open(file_path, 'wb') as file:
                                    file.write(response.content)

                                browser.get("https://tadas.afad.gov.tr/list-station")
                                time.sleep(15)
                        elif tr_number == 5:

                            station = browser.find_element(By.XPATH, "./html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/div[2]/ul/li[2]/a")  # Burada station e tıklandı
                            station.click()
                            time.sleep(15)

                            station_search = browser.find_element(By.XPATH, "/html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/div[2]/ul/li[2]/ul/li/a")  # Burada station/search e tıklandı
                            station_search.click()
                            time.sleep(15)

                            search_ = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[1]/div[3]/div/button[1]")  # search işlemi gerçekleştirildi
                            search_.click()
                            time.sleep(15)

                            Vs30_button = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/div/div/table/thead/tr/th[8]/a")
                            Vs30_button.click()
                            Vs30_button.click()
                            time.sleep(15)

                            station_detail = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[5]/td[12]/button")
                            station_detail.click()
                            time.sleep(15)
                            kod_element = browser.find_element(By.TAG_NAME, "h3")
                            kod_numarasi = kod_element.text.split(":")[1].strip()

                            h3_element = browser.find_element(By.TAG_NAME, "h3")
                            text = h3_element.text

                            jeofizik_data = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[7]/a")
                            jeofizik_data.click()
                            time.sleep(15)
                            next_page = False

                            if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item")) == 0:
                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()

                                if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.pdf']")) == 0:
                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)
                                else:
                                    pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute("href")
                                    browser.get(pdf_link)
                                    time.sleep(15)
                                    pdf_url = browser.current_url
                                    file_name = f'TK.{kod_numarasi}.pdf'
                                    file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                    response = requests.get(pdf_url)
                                    with open(file_path, 'wb') as file:
                                        file.write(response.content)

                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)

                            else:


                                zip_elements = browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.zip']")


                                for zip_element in zip_elements:
                                    zip_link = zip_element.get_attribute("href")
                                    zip_element.click()

                                    time.sleep(15)
                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()
                                time.sleep(15)

                                pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute("href")
                                browser.get(pdf_link)
                                time.sleep(15)
                                pdf_url = browser.current_url
                                file_name = f'TK.{kod_numarasi}.pdf'
                                file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                response = requests.get(pdf_url)
                                with open(file_path, 'wb') as file:
                                    file.write(response.content)

                                browser.get("https://tadas.afad.gov.tr/list-station")
                                time.sleep(15)
                        elif tr_number == 6:

                            station = browser.find_element(By.XPATH, "./html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/div[2]/ul/li[2]/a")  # Burada station e tıklandı
                            station.click()
                            time.sleep(15)

                            station_search = browser.find_element(By.XPATH, "/html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/div[2]/ul/li[2]/ul/li/a")  # Burada station/search e tıklandı
                            station_search.click()
                            time.sleep(15)

                            search_ = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[1]/div[3]/div/button[1]")  # search işlemi gerçekleştirildi
                            search_.click()
                            time.sleep(15)

                            Vs30_button = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/div/div/table/thead/tr/th[8]/a")
                            Vs30_button.click()
                            Vs30_button.click()
                            time.sleep(15)

                            station_detail = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[6]/td[12]/button")
                            station_detail.click()
                            time.sleep(15)
                            kod_element = browser.find_element(By.TAG_NAME, "h3")
                            kod_numarasi = kod_element.text.split(":")[1].strip()
                            h3_element = browser.find_element(By.TAG_NAME, "h3")
                            text = h3_element.text

                            jeofizik_data = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[7]/a")
                            jeofizik_data.click()
                            time.sleep(15)
                            next_page = False

                            if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item")) == 0:
                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()

                                if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.pdf']")) == 0:
                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)
                                else:
                                    pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute("href")
                                    browser.get(pdf_link)
                                    time.sleep(15)
                                    pdf_url = browser.current_url
                                    file_name = f'TK.{kod_numarasi}.pdf'
                                    file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                    response = requests.get(pdf_url)
                                    with open(file_path, 'wb') as file:
                                        file.write(response.content)

                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)

                            else:


                                zip_elements = browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.zip']")


                                for zip_element in zip_elements:
                                    zip_link = zip_element.get_attribute("href")
                                    zip_element.click()

                                    time.sleep(15)
                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()
                                time.sleep(15)

                                pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute("href")
                                browser.get(pdf_link)
                                time.sleep(15)
                                pdf_url = browser.current_url
                                file_name = f'TK.{kod_numarasi}.pdf'
                                file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                response = requests.get(pdf_url)
                                with open(file_path, 'wb') as file:
                                    file.write(response.content)

                                browser.get("https://tadas.afad.gov.tr/list-station")
                                time.sleep(15)
                        elif tr_number == 7:

                            station = browser.find_element(By.XPATH, "./html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/div[2]/ul/li[2]/a")  # Burada station e tıklandı
                            station.click()
                            time.sleep(15)

                            station_search = browser.find_element(By.XPATH, "/html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/div[2]/ul/li[2]/ul/li/a")  # Burada station/search e tıklandı
                            station_search.click()
                            time.sleep(15)

                            search_ = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[1]/div[3]/div/button[1]")  # search işlemi gerçekleştirildi
                            search_.click()
                            time.sleep(15)

                            Vs30_button = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/div/div/table/thead/tr/th[8]/a")
                            Vs30_button.click()
                            Vs30_button.click()
                            time.sleep(15)

                            station_detail = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[7]/td[12]/button")
                            station_detail.click()
                            time.sleep(15)
                            kod_element = browser.find_element(By.TAG_NAME, "h3")
                            kod_numarasi = kod_element.text.split(":")[1].strip()
                            h3_element = browser.find_element(By.TAG_NAME, "h3")
                            text = h3_element.text

                            jeofizik_data = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[7]/a")
                            jeofizik_data.click()
                            time.sleep(15)
                            next_page = False

                            if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item")) == 0:
                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()

                                if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.pdf']")) == 0:
                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)
                                else:
                                    pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute("href")
                                    browser.get(pdf_link)
                                    time.sleep(15)
                                    pdf_url = browser.current_url
                                    file_name = f'TK.{kod_numarasi}.pdf'
                                    file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                    response = requests.get(pdf_url)
                                    with open(file_path, 'wb') as file:
                                        file.write(response.content)

                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)

                            else:


                                zip_elements = browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.zip']")


                                for zip_element in zip_elements:
                                    zip_link = zip_element.get_attribute("href")
                                    zip_element.click()

                                    time.sleep(15)
                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()
                                time.sleep(15)

                                pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute("href")
                                browser.get(pdf_link)
                                time.sleep(15)
                                pdf_url = browser.current_url
                                file_name = f'TK.{kod_numarasi}.pdf'
                                file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                response = requests.get(pdf_url)
                                with open(file_path, 'wb') as file:
                                    file.write(response.content)

                                browser.get("https://tadas.afad.gov.tr/list-station")
                                time.sleep(15)
                        elif tr_number == 8:

                            station = browser.find_element(By.XPATH, "./html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/div[2]/ul/li[2]/a")  # Burada station e tıklandı
                            station.click()
                            time.sleep(15)

                            station_search = browser.find_element(By.XPATH, "/html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/div[2]/ul/li[2]/ul/li/a")  # Burada station/search e tıklandı
                            station_search.click()
                            time.sleep(15)

                            search_ = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[1]/div[3]/div/button[1]")  # search işlemi gerçekleştirildi
                            search_.click()
                            time.sleep(15)

                            Vs30_button = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/div/div/table/thead/tr/th[8]/a")
                            Vs30_button.click()
                            Vs30_button.click()
                            time.sleep(15)

                            station_detail = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[8]/td[12]/button")
                            station_detail.click()
                            time.sleep(15)
                            kod_element = browser.find_element(By.TAG_NAME, "h3")
                            kod_numarasi = kod_element.text.split(":")[1].strip()
                            h3_element = browser.find_element(By.TAG_NAME, "h3")
                            text = h3_element.text

                            jeofizik_data = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[7]/a")
                            jeofizik_data.click()
                            time.sleep(15)
                            next_page = False

                            if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item")) == 0:
                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()

                                if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.pdf']")) == 0:
                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)
                                else:
                                    pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute("href")
                                    browser.get(pdf_link)
                                    time.sleep(15)
                                    pdf_url = browser.current_url
                                    file_name = f'TK.{kod_numarasi}.pdf'
                                    file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                    response = requests.get(pdf_url)
                                    with open(file_path, 'wb') as file:
                                        file.write(response.content)

                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)

                            else:


                                zip_elements = browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.zip']")


                                for zip_element in zip_elements:
                                    zip_link = zip_element.get_attribute("href")
                                    zip_element.click()

                                    time.sleep(15)
                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()
                                time.sleep(15)

                                pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute("href")
                                browser.get(pdf_link)
                                time.sleep(15)
                                pdf_url = browser.current_url
                                file_name = f'TK.{kod_numarasi}.pdf'
                                file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                response = requests.get(pdf_url)
                                with open(file_path, 'wb') as file:
                                    file.write(response.content)

                                browser.get("https://tadas.afad.gov.tr/list-station")
                                time.sleep(15)
                        elif tr_number == 9:

                            station = browser.find_element(By.XPATH, "./html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/sdiv[2]/ul/li[2]/a")  # Burada station e tıklandı
                            station.click()
                            time.sleep(15)

                            station_search = browser.find_element(By.XPATH, "/html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/div[2]/ul/li[2]/ul/li/a")  # Burada station/search e tıklandı
                            station_search.click()
                            time.sleep(15)

                            search_ = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[1]/div[3]/div/button[1]")  # search işlemi gerçekleştirildi
                            search_.click()
                            time.sleep(15)

                            Vs30_button = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/div/div/table/thead/tr/th[8]/a")
                            Vs30_button.click()
                            Vs30_button.click()
                            time.sleep(15)

                            station_detail = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[9]/td[12]/button")
                            station_detail.click()
                            time.sleep(15)
                            kod_element = browser.find_element(By.TAG_NAME, "h3")
                            kod_numarasi = kod_element.text.split(":")[1].strip()
                            h3_element = browser.find_element(By.TAG_NAME, "h3")
                            text = h3_element.text

                            jeofizik_data = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[7]/a")
                            jeofizik_data.click()
                            time.sleep(15)
                            next_page = False

                            if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item")) == 0:
                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()

                                if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.pdf']")) == 0:
                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)
                                else:
                                    pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute("href")
                                    browser.get(pdf_link)
                                    time.sleep(15)
                                    pdf_url = browser.current_url
                                    file_name = f'TK.{kod_numarasi}.pdf'
                                    file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                    response = requests.get(pdf_url)
                                    with open(file_path, 'wb') as file:
                                        file.write(response.content)

                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)

                            else:


                                zip_elements = browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.zip']")


                                for zip_element in zip_elements:
                                    zip_link = zip_element.get_attribute("href")
                                    zip_element.click()

                                    time.sleep(15)
                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()
                                time.sleep(15)

                                pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute("href")
                                browser.get(pdf_link)
                                time.sleep(15)
                                pdf_url = browser.current_url
                                file_name = f'TK.{kod_numarasi}.pdf'
                                file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                response = requests.get(pdf_url)
                                with open(file_path, 'wb') as file:
                                    file.write(response.content)

                                browser.get("https://tadas.afad.gov.tr/list-station")
                                time.sleep(15)

                        else:

                            station = browser.find_element(By.XPATH, "./html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/div[2]/ul/li[2]/a")  # Burada station e tıklandı
                            station.click()
                            time.sleep(15)

                            station_search = browser.find_element(By.XPATH, "/html/body/app-root/div[1]/app-navbar/nav/div[2]/div/div/div[2]/ul/li[2]/ul/li/a")  # Burada station/search e tıklandı
                            station_search.click()
                            time.sleep(15)

                            search_ = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[1]/div[3]/div/button[1]")  # search işlemi gerçekleştirildi
                            search_.click()
                            time.sleep(15)

                            Vs30_button = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/div/div/table/thead/tr/th[8]/a")
                            Vs30_button.click()
                            Vs30_button.click()
                            time.sleep(15)

                            station_detail = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-station/div/div/div/div/div/div/div[3]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[10]/td[12]/button")
                            station_detail.click()
                            time.sleep(15)
                            kod_element = browser.find_element(By.TAG_NAME, "h3")
                            kod_numarasi = kod_element.text.split(":")[1].strip()

                            h3_element = browser.find_element(By.TAG_NAME, "h3")
                            text = h3_element.text

                            jeofizik_data = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[7]/a")
                            jeofizik_data.click()
                            time.sleep(15)
                            next_page = True
                            tr_number = 0
                            if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item")) == 0:
                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()

                                if len(browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.pdf']")) == 0:

                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)
                                else:
                                    pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute("href")
                                    browser.get(pdf_link)
                                    time.sleep(15)
                                    pdf_url = browser.current_url
                                    file_name = f'TK.{kod_numarasi}.pdf'
                                    file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                    response = requests.get(pdf_url)
                                    with open(file_path, 'wb') as file:
                                        file.write(response.content)

                                    browser.get("https://tadas.afad.gov.tr/list-station")
                                    time.sleep(15)

                            else:


                                zip_elements = browser.find_elements(By.CSS_SELECTOR, "div.panel-body li.list-group-item a[href$='.zip']")


                                for zip_element in zip_elements:
                                    zip_link = zip_element.get_attribute("href")
                                    zip_element.click()

                                    time.sleep(15)

                                doküman_station = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-station-detail/div/div/div/div/div/div[2]/div/div/ul/li[6]/a")
                                doküman_station.click()
                                time.sleep(15)

                                pdf_link = browser.find_element(By.XPATH, "//a[contains(text(), 'raporu.pdf')]").get_attribute(
                                    "href")
                                browser.get(pdf_link)
                                time.sleep(15)
                                pdf_url = browser.current_url
                                file_name = f'TK.{kod_numarasi}.pdf'
                                file_path = 'C:/Users/berke/OneDrive - Kadir Has University/Masaüstü/' + file_name
                                response = requests.get(pdf_url)
                                with open(file_path, 'wb') as file:
                                    file.write(response.content)

                                browser.get("https://tadas.afad.gov.tr/list-station")
                                time.sleep(15)
                break
        except Exception as e:

            print(f"An error occurred: {str(e)}")
            browser.quit()