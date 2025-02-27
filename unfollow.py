from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pathlib import Path
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import platform
import time
from colorama import Fore, Style, init
import tkinter as tk
current_dir = Path(__file__).parent
base_profile_path = current_dir / "Profile_tool"
os_name = platform.system()
if os_name == "Windows":
    chromedriver_path = current_dir / "chromedriver.exe"
elif os_name == "Darwin":
    chromedriver_path = current_dir / "chromedriver"
drivers = []

def setup():
    global driver
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--disable-infobars")
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    drivers.append(driver)
    driver.get("https://www.tiktok.com")
    input("Nhấn Enter để tiến hành unfolow")

        
def reload():
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[3]/h3/div[1]/span'))).click()

def unfollow():
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[1]/div/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[2]/div/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[3]/div/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[4]/div/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[5]/div/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[6]/div/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[7]/div/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[8]/div/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[9]/div/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[10]/div/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[11]/div/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[12]/div/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[13]/div/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[14]/div/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[15]/div/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[16]/div/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[17]/div/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[18]/div/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[19]/div/div/div/div/button'))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[20]/div/div/div/div/button'))).click()
    time.sleep(1)
        

setup()
WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[3]/div[1]/div[9]/a/button/div/div[2]'))).click()
while True:
    try:
        reload()
        unfollow()
        driver.refresh()
    except NoSuchElementException:
        print("unfl thành công")
        driver.quit()
        

