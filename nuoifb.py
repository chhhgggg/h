import os
import random
import string
import threading
import sys
import requests
import shutil
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import hashlib
from colorama import init , Fore, Back , Style
from webdriver_manager.core.manager import DriverManager
import socket
from datetime import datetime
import json
import os
import requests
import zipfile

# URL của file zip cần tải
ZIP_URL = "https://storage.googleapis.com/chrome-for-testing-public/133.0.6943.98/win32/chromedriver-win32.zip"
ZIP_NAME = "chromedriver-win32.zip"
EXTRACT_FOLDER = "chromedriver-win32"

def download_and_extract_chromedriver():
    # Kiểm tra nếu thư mục đã tồn tại
    if os.path.exists(EXTRACT_FOLDER):
        print(f"Thư mục '{EXTRACT_FOLDER}' đã tồn tại, không cần tải lại.")
        return

    # Tải file zip về
    print(f"Đang tải {ZIP_URL}...")
    response = requests.get(ZIP_URL, stream=True)
    
    if response.status_code == 200:
        with open(ZIP_NAME, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Tải xuống {ZIP_NAME} thành công.")
    else:
        print("Tải xuống thất bại!")
        return

    # Giải nén file
    print(f"Đang giải nén {ZIP_NAME}...")
    with zipfile.ZipFile(ZIP_NAME, "r") as zip_ref:
        zip_ref.extractall(".")
    print(f"Giải nén hoàn tất vào thư mục '{EXTRACT_FOLDER}'.")

    # Xóa file ZIP sau khi giải nén
    os.remove(ZIP_NAME)
    print(f"Đã xóa file {ZIP_NAME}.")

# Gọi hàm trước khi sử dụng chromedriver
download_and_extract_chromedriver()
#path
chromedriver_path = os.path.dirname(os.path.abspath(__file__))+"/chromedriver-win32/chromedriver.exe"
folder_path = os.path.dirname(os.path.abspath(__file__))

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datanuoifb")



def print_tool_info():
    print(Fore.CYAN + Back.BLACK + "╔═══════════════════════════════════════════════╗")
    print(Fore.YELLOW + Style.BRIGHT + "║       THÔNG TIN CHỦ TOOL                      ║")
    print(Fore.GREEN + "║ Tên: " + Fore.YELLOW + "Quy Kedo" + " + Lê Mạnh                       ║")
    print(Fore.RED + "║ Group Zalo: " + Fore.YELLOW + "https://zalo.me/g/uaahwq871" + "       ║")
    print(Fore.CYAN + Back.BLACK + "╚═══════════════════════════════════════════════╝")


#slow send



def slow_typing_with_actionchains(driver, element, text):
    delay = random.uniform(0.1, 0.5)
    for char in text:
        element.send_keys(char)
        time.sleep(delay)


def print_with_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")



def check_ck(driver):
    link = driver.current_url
    if link == 'https://www.facebook.com/login':
        return False
    else:
        return True



def log_fb(folder_path,driver,name):
    driver.get('https://www.facebook.com/login')
    driver.refresh()
    checkacc = check_ck(driver)
    if checkacc:
        print(f'{name}: {Fore.GREEN}đăng nhập thành công cấu hình: {name}!{Style.RESET_ALL}')
    
    else:
        print('bạn phải đang nhập bằng tay ( lần sau có lẽ ko cần đăng nhập lại)')
        while True:
            link_now = driver.current_url
            if link_now != 'https://www.facebook.com/login':
                break
            time.sleep(1)
        if check_ck(driver):
            print(f'{name}: {Fore.GREEN}đăng nhập thành công!{Style.RESET_ALL}')
        else:
            print(f'{name}: {Fore.RED}đăng nhập không thành công, có thể do cookie die{Style.RESET_ALL}')


# def khoitao(dt_p , headlesss ,chromedriver_path, name,folder_path):
#     service = Service(chromedriver_path, log_path=os.devnull)
#     chrome_options = Options()
#     chrome_options.add_argument("--log-level=3")  # Chỉ hiển thị lỗi nghiêm trọng
#     chrome_options.add_argument("--silent")  # Giảm log từ trình duyệt
#     chrome_options.add_argument("--start-minimized")
#     chrome_options.add_argument("--disable-notifications")
#     chrome_options.add_argument("--disable-logging")
#     chrome_options.add_argument("--disable-infobars")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument(f"--user-data-dir={dt_p}")
#     chrome_options.add_argument(f"--profile-directory={name}")
#     chrome_options.add_argument("--force-device-scale-factor=0.45")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
#     if headlesss == 'y':
#         chrome_options.add_argument("--headless")
#     driver= webdriver.Chrome(service=service, options=chrome_options)
#     driver.set_window_size(700,1024 )
#     log_fb(folder_path,driver,name)
#     return driver

def check(dt_p , headlesss ,chromedriver_path, name,folder_path):
    service = Service(chromedriver_path, log_path=os.devnull)
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")  # Chỉ hiển thị lỗi nghiêm trọng
    chrome_options.add_argument("--silent")  # Giảm log từ trình duyệt
    chrome_options.add_argument("--start-minimized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument(f"--user-data-dir={dt_p}")
    chrome_options.add_argument(f"--profile-directory={name}")
    chrome_options.add_argument("--force-device-scale-factor=0.45")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    if headlesss == 'True':
        chrome_options.add_argument("--headless")
    driver= webdriver.Chrome(service=service, options=chrome_options)
    driver.set_window_size(700,1024 )
    log_fb(folder_path,driver,name)
    driver.close()
def khoitao1(dt_p, headlesss, chromedriver_path, name, folder_path, proxy=None,username=None,password=None):
    service = Service(chromedriver_path, log_path=os.devnull)
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--silent") 
    chrome_options.add_argument("--start-minimized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument(f"--user-data-dir={dt_p}")
    chrome_options.add_argument(f"--profile-directory={name}")
    chrome_options.add_argument("--force-device-scale-factor=0.45")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    # Thêm cấu hình proxy nếu có
    if proxy != '':

        if username and password:
            # Cấu hình proxy với xác thực
            proxy_auth = f"{username}:{password}@{proxy}"
            print(proxy_auth)
            chrome_options.add_argument(f'--proxy-server=http://{proxy_auth}')
        else:
            # Cấu hình proxy không cần xác thực
            proxy = f'http://{proxy}'
            print(proxy)
            chrome_options.add_argument(f'--proxy-server={proxy}')
    
    if headlesss == 'y':
        chrome_options.add_argument("--headless")
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_window_size(700, 1024)
    log_fb(folder_path, driver, name)
    return driver



def khoitao2(dt_p, headlesss, chromedriver_path, name, folder_path):
    service = Service(chromedriver_path, log_path=os.devnull)
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--silent") 
    chrome_options.add_argument("--start-minimized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument(f"--user-data-dir={dt_p}")
    chrome_options.add_argument(f"--profile-directory={name}")
    chrome_options.add_argument("--force-device-scale-factor=0.45")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    if headlesss == 'y':
        chrome_options.add_argument("--headless")
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_window_size(700, 1024)
    log_fb(folder_path, driver, name)
    return driver


os.makedirs(data_path, exist_ok=True)







def like(driver):
    time.sleep(4)
    try:
        like_texts = [
            'Like', 'Thích', 'Prefer', 'Aimer', 'Piace'
        ]

        like_buttons = []
        for text in like_texts:
            like_buttons += driver.find_elements(By.XPATH, f'//div[@aria-label="{text}"] | //button[contains(text(), "{text}")]')

        if not like_buttons:
            print("Không tìm thấy nút like nào phù hợp.")
            return False

        for btn in like_buttons:
            try:
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                time.sleep(1)
                btn.click()
                print("Đã like bài viết!")
                return True
            except Exception as click_error:
                print(f"Lỗi khi nhấn nút like: {click_error}")

        print("Không tìm thấy nút like nào phù hợp.")
        return False
    except Exception as e:
        print(f"Lỗi khi tìm nút like: {e}")
        return False




def upbai(driver):
    driver.get('https://www.facebook.com/')
    up = driver.find_element(By.XPATH, '//div[@class="xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe"]')
    up.click()
    time.sleep(random.uniform(1.5,2.5))
    url = 'https://official-joke-api.appspot.com/random_joke'
    time.sleep(1)
    reponse = requests.get(url)
    time.sleep(5)
    data = reponse.json()
    time.sleep(2)
    content = data["setup"]
    inputt= driver.find_elements(By.XPATH, '//p[@class="xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8"]')

    # inputt[-1].send_keys(content)
    slow_typing_with_actionchains(driver, inputt[-1],content)
    time.sleep(random.uniform(1.5,2.5))
    inputt[-1].send_keys(Keys.ENTER)
    dang = driver.find_elements(By.XPATH, '//div[@class="x9f619 x1n2onr6 x1ja2u2z x193iq5w xeuugli x6s0dn4 x78zum5 x2lah0s x1fbi1t2 xl8fo4v"]')
    dang[-1].click()
    # time.sleep(3)
    # dong = driver.find_element(By.XPATH, '//div[@class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xzolkzo x12go9s9 x1rnf11y xprq8jg x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x78zum5 xl56j7k xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 xc9qbxq x14qfxbe x1qhmfi1"]')
    # dong.click()
    time.sleep(3)
def autoscroll(driver):
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(0.2)
def autoreels(driver):

    for i in range(3):
        all_chuyen_reels = [
            '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div/div[3]/div/div/svg/g/g/path[1]',

        ]
        for chuyen_reels in all_chuyen_reels:
            try:
                phantu = driver.find_element(By.XPATH, chuyen_reels)
                phantu.click()
                time.sleep(1)
                break
            except Exception as e:
                pass
        
def likereel(driver):
    all_xpath_reels = [
        '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[1]/div',
        '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[1]/div/i',
        '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[1]/div/div'
    ]
    for xpath_reels in all_xpath_reels:
        try:
            like = driver.find_element(By.XPATH, xpath_reels)
            like.click()
            time.sleep(1)
            break
        except Exception as e:
            pass
def ad_friends(driver):
    driver.get('https://www.facebook.com/friends')
    time.sleep(2)
    all_add_friends = [
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div/div[2]/div[3]/div/div',
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[3]/div/div/div[1]'
    ]
    for i in range(random.randint(1, 3)):
        try:
            for add_friends in all_add_friends:
                try:
                    add = driver.find_element(By.XPATH, add_friends)
                    add.click()
                    time.sleep(1)
                    break
                except Exception as e:
                    pass
        except Exception as e:
            pass
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(1)
    all_add_fri = [
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div/div/div/div/div[4]/div',
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div/div/div/div/div[4]/div/div',
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div/div/div/div/div[4]/div/div/div[1]'

    ]
    all_del = [
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div/div/div/div/div[5]',
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div/div/div/div/div[5]/div',
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div/div/div/div/div[5]/div/div'

    ]
    for i in range(random.randint(3, 5)):
        phanloai = random.choices(['gỡ', 'thêm'], weights=[20, 80])[0]
        if phanloai == 'gỡ':
            try:
                for del_friends in all_del:
                    try:
                        del_friend = driver.find_element(By.XPATH, del_friends)
                        del_friend.click()
                        time.sleep(1)
                        break
                    except Exception as e:
                        pass
            except Exception as e:
                pass
        elif phanloai == 'thêm':
            try:
                for add_friends in all_add_friends:
                    try:
                        add = driver.find_element(By.XPATH, add_friends)
                        add.click()
                        time.sleep(1)
                        break
                    except Exception as e:
                        pass
            except Exception as e:
                pass
def share_post(driver):
    all_xpath_share = [
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div[4]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div/div/div[2]/div/div[3]/div',
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div[4]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div/div/div[2]/div/div[3]/div/div[1]',
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div[4]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div/div/div[2]/div/div[3]/div/div[1]/div[1]/i',
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div[4]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div/div/div[2]/div/div[3]/div/div[1]/div[2]',
        
    ]
    all_xpath_chiase = [
        '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/form/div/div/div[3]/div/div/div/div[1]/div/div',
        '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/form/div/div/div[3]/div/div/div/div[1]/div'
    ]
    for xpath_share in all_xpath_share:
        try:
            share = driver.find_element(By.XPATH, xpath_share)
            share.click()
            time.sleep(1)
            try:
                for chiase in all_xpath_chiase:
                    try:
                        chiase = driver.find_element(By.XPATH, chiase)
                        chiase.click()
                        time.sleep(1)
                        break
                    except Exception as e:
                        pass
            except Exception as e:
                pass
            break
        except Exception as e:
            pass


def autocomment(driver):
    list_tu = [
        'Chào',
        'Xin chào',
        'Nhào nhào',
        'Hi',
        'Dạo này ổn ko',
        'Chúc một ngày tốt lành',
        'Hê lô!',
        '🥰😘🥰',
        '😴😴😴',
        '🤩🤩🤩'
    ]
    all_xpath_comment = [
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div[4]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div/div/div[2]/div/div[2]/div',
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div[4]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div/div/div[2]/div/div[2]/div/div[1]',
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div[4]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]',

    ]
    tudcchon = random.choice(list_tu)
    for comnent in all_xpath_comment:
        try:
            fcomment = driver.find_element(By.XPATH, comnent)
            fcomment.click()
            time.sleep(1)
            o_cmt = driver.find_element(By.XPATH, '//div[@aria-label="Viết bình luận..."]')
            slow_typing_with_actionchains(driver,o_cmt, tudcchon)
            time.sleep(1)
            break
        except Exception as e:
            pass
def main(driver,name):
    
    #cau hinh
    xem_post = random.randint( 17,26)
    
    sau_post_like= random.randint( 10,15)
    tu_post_sang_video = random.randint( 24,35)
    tu_post_sang_reel = random.randint(30,50)
    sau_reel_like = random.randint( 10,15)
    sau_video_like = random.randint( 2,4)
    sau_post_comment= random.randint( 10,20)
    sau_video_upbai = random.randint( 10,20)
    sau_post_add_friend= random.randint( 50,60)
    sau_post_share = random.randint( 3,7)
    # print('='*30)
    # print(name)
    # print(xem_post)
    # print(sau_post_like)
    # print(tu_post_sang_video)
    # print(tu_post_sang_reel)
    # print(sau_reel_like)
    # print(sau_video_like)
    # print(sau_post_comment)
    # print(sau_video_upbai)
    # print(sau_post_add_friend)
    # print(sau_post_share)
    # print('='*30)

    da_like = 0
    da_comment = 0
    da_add_friend = 0
    da_share = 0
    da_upbai = 0

    vd_wted = 0 # da lam
    reel_wted = 0 #da lam
    video_wted = 0 #da lam
    video_comment = 0 #da lam
    video_upbai = 0 #da lam
    video_add_friend = 0 #da lam
    video_share = 0 #da lam
    driver.get('https://www.facebook.com')
    time.sleep(3)
    while True:
        for i in range(3):
            try:
                autoscroll(driver)
            except:
                pass
        vd_wted += 1
        reel_wted += 1
        video_wted += 1
        video_comment += 1
        video_upbai += 1
        video_add_friend += 1
        video_share += 1
        time.sleep(xem_post)
        if vd_wted > sau_post_like:
            for i in range(3):
                try:
                    like(driver)
                    d = 0
                except Exception as e:
                    autoscroll(driver)
            vd_wted = 0
            da_like += 1
            print(f'cấu hình {name} đã like :{da_like} bài')
            sau_post_like= random.randint( 10,15)
        if reel_wted > tu_post_sang_reel:
            nhiem_vu_reel = random.randint(2,4)
            driver.get('https://www.facebook.com/reel/')
            time.sleep(2)
            for _ in range(nhiem_vu_reel):
                for _ in range(sau_reel_like):
                    xem_reel = random.randint( 30,40)
                    time.sleep(xem_reel)
                    autoreels(driver)
                likereel(driver)
                time.sleep(1)
            
            driver.get('https://www.facebook.com')
            reel_wted = 0
            tu_post_sang_reel = random.randint(30,50)
            sau_reel_like = random.randint( 10,15)
        if video_wted > tu_post_sang_video:
            nhiem_vu_video = random.randint(2,4)
            driver.get('https://www.facebook.com/watch/?ref=tab')
            time.sleep(2)
            for _ in range(nhiem_vu_video):                
                for _ in range(sau_video_like):
                    xemvideo = random.randint( 80,120)
                    time.sleep(xemvideo)
                    autoscroll(driver)
                like(driver)
                time.sleep(1)
            driver.get('https://www.facebook.com')
            video_wted = 0
            tu_post_sang_video = random.randint( 24,35)
            sau_video_like = random.randint( 2,4)
        if video_comment > sau_post_comment:
            autocomment(driver)
            video_comment = 0
            driver.get('https://www.facebook.com')
            da_comment += 1
            print(f'cấu hình {name} đã comment :{da_comment} bài')
            sau_post_comment= random.randint( 10,20)
        if video_upbai > sau_video_upbai:
            upbai(driver)
            video_upbai = 0
            driver.get('https://www.facebook.com')
            da_upbai += 1
            print(f'cấu hình {name} đã đăng bài viết : {da_upbai} lần')
            sau_video_upbai = random.randint( 10,20)
        if video_add_friend > sau_post_add_friend:
            ad_friends(driver)
            video_add_friend = 0
            driver.get('https://www.facebook.com')
            print(f'cấu hình {name} thực hiện thêm bài bè : {da_add_friend}')
            sau_post_add_friend= random.randint( 50,60)
        if video_share > sau_post_share:
            share_post(driver)
            video_share = 0
            da_share += 1
            print(f'cấu hình {name} thực hiện chia sẻ {da_share} bài')
            sau_post_share = random.randint( 3,7)

def nuoi_da_luong(dt_p,headlesss,chromedriver_path,name,folder_path):
    driver = khoitao2(dt_p,headlesss,chromedriver_path,name,folder_path)
    main(driver,name)
    # upbai(driver)
os.system('cls' if os.name == 'nt' else 'clear')
menu = """
\033[1;36m===================================\033[0m
\033[1;32mCHƯƠNG TRÌNH QUẢN LÝ TOOL NUÔI FB\033[0m
\033[1;36m===================================\033[0m
\033[1;33m[1]\033[0m Kiểm tra trạng thái hoạt động của tài khoản FB
\033[1;33m[2]\033[0m Thêm cấu hình
\033[1;33m[3]\033[0m Xóa cấu hình
\033[1;33m[4]\033[0m Nuôi tất cả tài khoản
\033[1;31m[exit]\033[0m Thoát chương trình
\033[1;36m===================================\033[0m
"""

os.system('cls' if os.name == 'nt' else 'clear')
print_tool_info()
headlesss = input("bạn có muốn chạy tài khoản headless(ẩn) không?(y/n): ").strip().lower()
time.sleep(2.5)
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print_tool_info()
    print(menu)
    folders = [f for f in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, f))]
    if len(folders) == 0:
        print("Không tìm thấy tài khoản nào, cần thêm cấu hình")

    else:
        print('các cấu hình hiện tại:')
        for i in range(len(folders)):
            print(f"[{i}] {folders[i]}")
    choice = input("Nhập lựa chọn của bạn , exit để thoát: ")
    
    if choice == "1":
        rt = "\n>> Kiểm tra trạng thái tài khoản...\n"
        print(rt)
        profile = len(folders)
        
        def check_at_tk():
            threadsss = []
            for i in range(profile):
                profile_path = os.path.join(data_path, f'Facebook{i}')
                os.makedirs(profile_path, exist_ok=True)

                # check(profile_path,headlesss,chromedriver_path, f'Facebook{i}',folder_path)
                thread = threading.Thread(target=check, args=(profile_path,headlesss,chromedriver_path, f'Facebook{i}',folder_path))
                thread.start()
                threadsss.append(thread)
            for i in threadsss:
                i.join()
        check_at_tk()
        time.sleep(5)
        
    elif choice == "2":
        rt = "\n>> Thêm cấu hình...\n"
        print(rt)
        time.sleep(1)
        them_cau_hinh = input("Nhập số lượng cấu hình bạn có : ")
        for i in range(int(them_cau_hinh)):
            
            user_proxy = None
            pass_proxy = None
            proxy = None
            muon_them_proxy = input("bạn có muốn thêm proxy cho tài khoản này ko(y/n): ")
            if muon_them_proxy == "y":
                loai_proxy = input("Nhập loại proxy , nếu proxy có user:pass nhập 1, ko thì nhập 2: ")
                if loai_proxy == "1":
                    user_proxy = input("Nhập user proxy: ")
                    pass_proxy = input("Nhập pass proxy: ")
                    proxy = input("nhập proxy(dạng ip:port): ")
                else:
                    proxy = input("nhập proxy(dạng ip:port): ")
            else:
                proxy = ""
            profile_path = os.path.join(data_path, f'Facebook{i}')
            os.makedirs(profile_path, exist_ok=True)
            khoitao1(profile_path,headlesss,chromedriver_path, f'Facebook{i}',folder_path,proxy,user_proxy,pass_proxy)
            print(folders)
    elif choice == "3":
        rt = "\n>> Xóa cấu hình...\n"
        print(rt)
        time.sleep(1)
        folders = [f for f in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, f))]
        for i in range(len(folders)):
            print(f"[{i}] {folders[i]}")
        while True:
            tk_del = input("Nhập cấu hình muốn xóa, ấn exit để quay lại menu: ")
            if tk_del == "exit":
                break
            elif int(tk_del) > len(folders)-1:
                print("Cấu hình không hợp lệ ")
            else:
                cau_hinh_xoa = data_path + "\\" + folders[int(tk_del)]
                shutil.rmtree(cau_hinh_xoa)
                print(f"Đã xoá cấu hình thành công cấu hình : {folders[int(tk_del)]}")
    elif choice == "4":
        rt = "\n>> Nuôi tất cả tài khoản...\n"
        # driver = khoitao('C:\\Users\\TechZoo\\Downloads\\TDS\\datanuoifb\\Facebook0',headlesss,chromedriver_path,f'Facebook0',folder_path)
        # upbai(driver)
        print(rt)
        folders = [f for f in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, f))]
        if len(folders) == 0:
            print("Không tìm thấy tài khoản nào, cần thêm cấu hình")

        else:
            print('các cấu hình hiện tại:')
            threadingg = []
            for i in range(len(folders)):
                dataa_path = data_path+f'/Facebook{i}'
                threaD = threading.Thread(target=nuoi_da_luong, args=(dataa_path, headlesss, chromedriver_path, f'Facebook{i}', folder_path))
                threaD.start()
                threadingg.append(threaD)
            for i in threadingg:
                i.join()
    elif choice == "exit":
        rt = "\n>> Thoát chương trình!\n"
        print(rt)
        sys.exit()
    else:
        rt = "\n>> Lựa chọn không hợp lệ! Vui lòng nhập lại.\n"
        print(rt)
        time.sleep(2)
