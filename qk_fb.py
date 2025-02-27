# Màu sắc cho hiển thị
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
end = '\033[0m'


import os
import random
import string
import threading
import sys
import requests
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
import zipfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#get key
import threading
import base64
import os
import time
import re
import json
import random
import requests
import socket
import sys
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
# Kiểm tra và cài đặt thư viện cần thiết
try:
    from faker import Faker
    from requests import session
    from colorama import Fore, Style
    import pystyle
except ImportError:
    os.system("pip install faker requests colorama bs4 pystyle")
    os.system("pip3 install requests pysocks")
    print('__Vui Lòng Chạy Lại Tool__')
    sys.exit()
# URL của file zip cần tải
ZIP_URL = "https://storage.googleapis.com/chrome-for-testing-public/133.0.6943.98/win32/chromedriver-win32.zip"
ZIP_NAME = "chromedriver-win32.zip"
EXTRACT_FOLDER = "chromedriver-win32"
chromedriver_path = os.path.dirname(os.path.abspath(__file__))+"/chromedriver-win32/chromedriver.exe"
folder_path = os.path.dirname(os.path.abspath(__file__))

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


# Định nghĩa đường dẫn
download_path = os.path.abspath("downloads")  # Thư mục tải file
extract_path = os.path.abspath("rektCaptcha-reCaptcha-Solver")  # Tên thư mục gốc sau khi giải nén

# Kiểm tra nếu thư mục đã tồn tại, bỏ qua việc tải lại
if os.path.exists(extract_path):
    print("Extension đã được tải và giải nén trước đó. Bỏ qua bước tải xuống.")
else:
    # Nếu chưa tồn tại, thực hiện tải xuống
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Cấu hình Chrome để tải file tự động
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "safebrowsing.enabled": True
    })

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    mediafire_url = "https://www.mediafire.com/file/w84diay6w8dp3je/rektCaptcha-reCaptcha-Solver.zip/file"  # Thay bằng URL thực tế
    print("Mở Mediafire để tải file...")
    driver.get(mediafire_url)

    try:
        # Chờ nút tải xuống xuất hiện và nhấn vào
        download_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'download')]"))
        )
        download_button.click()
        print("Đã nhấn tải xuống!")

        # Chờ file tải xong (tùy theo tốc độ mạng)
        time.sleep(60)
    finally:
        driver.quit()

    # Tìm file vừa tải
    zip_file = None
    for file in os.listdir(download_path):
        if file.endswith("rektCaptcha-reCaptcha-Solver.zip"):
            zip_file = os.path.join(download_path, file)
            break

    if not zip_file:
        print("Lỗi: Không tìm thấy file ZIP đã tải!")
        exit()

    print("Tải xuống thành công:", zip_file)

    # Giải nén file ZIP
    os.makedirs(extract_path, exist_ok=True)

    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(os.path.abspath("."))  # Giải nén vào thư mục hiện tại
    
    os.remove(zip_file)  # Xóa file ZIP sau khi giải nén
    print("Giải nén thành công!")

#path


#slow send
def slow_typing_with_actionchains(driver, element, text):
    delay = random.uniform(0.1, 0.5)
    for char in text:
        element.send_keys(char)
        time.sleep(delay)


def print_tool_info():
    print(Fore.CYAN + Back.BLACK + "╔═══════════════════════════════════════════════╗")
    print(Fore.YELLOW + Style.BRIGHT + "║       THÔNG TIN CHỦ TOOL                      ║")
    print(Fore.GREEN + "║ Tên: " + Fore.YELLOW + "Quy Kedo" + "                                 ║")
    print(Fore.RED + "║ Group Zalo: " + Fore.YELLOW + "https://zalo.me/g/uaahwq871" + "       ║")
    print(Fore.CYAN + Back.BLACK + "╚═══════════════════════════════════════════════╝")




def print_with_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def print_notice():
    print("\033[1;34m" + "="*50)
    print("\033[1;32m🔹 Nếu sau 30s không thấy tool thực hiện chức năng gì, thử \033[1;33mCtrl + C\033[1;32m.")
    print("🔹 Nếu vẫn không được, hãy chạy lại tool.")
    print("-" * 50)
    print("🔹 Nếu không thành công nhiều job liên tiếp, có thể Facebook đã thay đổi phần tử.")
    print("   🔸 Khi đó, hãy thoát tool và kiểm tra lại.")
    print("-" * 50)
    print("🔹 Khi nhận job mà cửa sổ Facebook bị tắt, đó là \033[1;36mCHUYỆN BÌNH THƯỜNG\033[1;32m, không phải lỗi.")
    print("="*50 + "\033[0m")










KEY_FILE = "keytoolkd.txt"  # File lưu key
TOKEN_LINK4M = "668bc1beab3a3470326ea5fd"  # API Token của bạn
# Tạo hoặc đọc khóa mã hóa bằng base64
secret_key = base64.urlsafe_b64encode(os.urandom(32))

# Mã hóa và giải mã dữ liệu bằng base64
def encrypt_data(data):
    return base64.b64encode(data.encode()).decode()

def decrypt_data(encrypted_data):
    return base64.b64decode(encrypted_data.encode()).decode()

# Lấy địa chỉ IP của thiết bị
def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        return response.json()['ip']
    except requests.ConnectionError:
        print("\033[1;91mKhông thể lấy địa chỉ IP! Kiểm tra kết nối mạng.")
        sys.exit()

# Lấy key mặc định từ GitHub
def get_default_key_from_github():
    url = "https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/keyy.txt"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text.strip()
    except requests.ConnectionError:
        pass
    return None

# Rút gọn URL bằng Link4m
def get_shortened_link_link4m(url):
    """Rút gọn URL bằng Link4m"""
    try:
        api_url = f"https://link4m.co/api-shorten/v2?api={TOKEN_LINK4M}&url={url}"
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success":
                return data.get("shortenedUrl")
            else:
                print(f"\033[1;91mLỗi từ Link4m: {data.get('message')}")
        else:
            print("\033[1;91mLỗi kết nối đến Link4m!")
    except requests.ConnectionError:
        print("\033[1;91mLỗi khi kết nối đến Link4m! Kiểm tra mạng.")
    return None

# Tạo key từ địa chỉ IP
def generate_key_and_url(ip_address):
    ngay = int(datetime.now().day)
    key1 = str(ngay * 27 + 27)
    ip_numbers = ''.join(filter(str.isdigit, ip_address))
    key = f'QuyKeDo{key1}{ip_numbers}'
    expiration_date = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    url = f'https://mlevip.blogspot.com/2025/02/mlevip.html?ma={key}'
    return url, key, expiration_date

# Lưu key vào file `keytool.txt`
def save_key(key, expiration_date):
    data = {"key": key, "expiration_date": expiration_date.isoformat()}
    encrypted_data = encrypt_data(json.dumps(data))
    with open(KEY_FILE, "w") as file:
        file.write(encrypted_data)

# Đọc key đã lưu trong file và kiểm tra hạn sử dụng
def load_saved_key():
    if not os.path.exists(KEY_FILE):
        return None

    try:
        with open(KEY_FILE, "r") as file:
            encrypted_data = file.read()
            data = json.loads(decrypt_data(encrypted_data))

            expiration_date = datetime.fromisoformat(data["expiration_date"])
            if expiration_date > datetime.now():
                return data["key"]  # Key còn hạn, trả về key
            else:
                print("\033[1;91mKey đã hết hạn! Vui lòng nhập key mới.")
                return None
    except (json.JSONDecodeError, KeyError):
        return None

# Chương trình chính để lấy key
def main():
    ip_address = get_ip_address()
    saved_key = load_saved_key()

    if saved_key:
        print("\033[1;92mKey hợp lệ! Mời bạn dùng tool.")
        time.sleep(2)
        return

    default_key = get_default_key_from_github()
    url, key_link4m, expiration_date = generate_key_and_url(ip_address)

    with ThreadPoolExecutor(max_workers=2) as executor:
        link4m_future = executor.submit(get_shortened_link_link4m, url)
        link_key_link4m = link4m_future.result()

        print("\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;32mNhập Key Để Dùng Tool")

        if link_key_link4m:
            print(f"\033[1;35mVượt link để lấy key Link4m: \033[1;36m{link_key_link4m}")

        while True:
            try:
                keynhap = input("\033[1;33mNhập Key: \033[1;32m").strip()
                if keynhap in [key_link4m, default_key]:
                    print("\033[1;92mKey đúng! Mời bạn dùng tool.")
                    save_key(keynhap, expiration_date)
                    time.sleep(2)
                    return
                else:
                    print("\033[1;91mKey sai! Vui lòng nhập lại.")
            except KeyboardInterrupt:
                print("\n\033[1;91mThoát tool!")
                sys.exit()

if __name__ == '__main__':
    main()



os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


#chrome option
chrome_options = Options()
chrome_options.add_argument("--log-level=3")  # Chỉ hiển thị lỗi nghiêm trọng
chrome_options.add_argument("--silent")  # Giảm log từ trình duyệt
chrome_options.add_argument("--start-minimized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--force-device-scale-factor=0.45")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")



service = Service(chromedriver_path, log_path=os.devnull)  # Ẩn log từ ChromeDriver
# Khởi tạo trình duyệt
print(Fore.CYAN + "══════════════════════════════════════")
print(Fore.YELLOW + Style.BRIGHT + " ▄█▀  CHỌN KÍCH CỠ CHROMEDRIVER  ▀█▄")
print(Fore.CYAN + "══════════════════════════════════════")
print(Fore.GREEN + "▶ [1] -  1366 x 768(to nhất)")
print(Fore.BLUE + "▶ [2] -  1280 x 720")
print(Fore.MAGENTA + "▶ [3] -  960 x 540")
print(Fore.CYAN + "══════════════════════════════════════")
loai = [[1366,768],[1280,720],[960,540]]
while True:
    user = input('bạn có muốn chọn kích cỡ (1-3): ')
    if user in ['1', '2', '3']:
        c,d = loai[int(user)-1]
        break
    else:
        continue


# headless_mode = input("Bạn có muốn chạy chế độ headless ở chrome facebook? (y/n): ").strip().lower()


driver = webdriver.Chrome(service=service, options=chrome_options)
driver.set_window_size(d, c)

chrome_options = Options()
chrome_options.add_argument("--log-level=3")  # Chỉ hiển thị lỗi nghiêm trọng
chrome_options.add_argument("--silent")  # Giảm log từ trình duyệt
chrome_options.add_argument("--start-minimized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--force-device-scale-factor=0.45")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# if headless_mode == 'y':
#     chrome_options.add_argument("--headless")
driver2 = webdriver.Chrome(service=service, options=chrome_options)
driver2.set_window_size(d, c)
check = 'settingfb.txt' in os.listdir(folder_path)
if check:
    user = input('bạn có muốn dùng lại setting cũ không? (Y/N): ')
    if user in ['y', 'Y']:
        f= open('settingfb.txt')
        lj_min,lj_max,wj_min,wj_max = map(int, f.read().split())
    else:
        check = False
        

if check == False:
    fi = open('settingfb.txt','w')
    #user = input('delay load jobs min:')
    lj_min = int(input('sau mỗi nhiệm vụ thì delay bao nhiêu giây (min):'))
    lj_max = int(input('sau mỗi nhiệm vụ thì delay bao nhiêu giây (max):'))
    wj_min = int(input('delay thực hiện nhiệm vụ (min) :'))
    wj_max = int(input('delay thực hiện nhiệm vụ (max):'))

    print(lj_min,lj_max,wj_min,wj_max, file= fi)
    fi.close()
    time.sleep(random.uniform(3,5))

def check_ck():
    link = driver2.current_url
    if link == 'https://www.facebook.com/login':
        return False
    else:
        return True



def log_fb(folder_path):
    driver2.get('https://www.facebook.com/login')
    driver2.refresh()
    check = 'accfb.json' in os.listdir(folder_path)
    if check:
        us = input('bạn có muốn dùng lại cookie Facebook cũ không?(y/n): ')
        if us.lower() == 'y':
        
            f = open('accfb.json','r')
            cookies = json.load(f)
            for i in cookies:
                driver2.add_cookie({"name": i, "value": cookies[i]})
            time.sleep(1)
            driver2.refresh()
            time.sleep(5)
            if check_ck():
                print_with_color('đăng nhập thanh công!',"32")
            else:
                print_with_color('đăng nhập khỏ thành công, có thể do cookie die',"31")
                check = False
        else:
            check = False
    if check== False:
        driver2.get('https://www.facebook.com/login')
        driver2.refresh()
        while True:
            cookies = input("Cookies FB: ")
            ck = {}
            for cookie in cookies.split(';'):
                try:
                    name, value = cookie.split('=')
                    name = name.strip()
                    value = value.strip()
                    ck[name] = value
                except ValueError:
                    pass
            for i in ck:
                driver2.add_cookie({"name": i, "value": ck[i]})
            time.sleep(1)
            driver2.refresh()
            time.sleep(2)
            if check_ck():
                print_with_color('đăng nhập thanh công!',"32")
                with open('accfb.json','w') as f:
                    json.dump(ck,f)
                break
            else:
                print_with_color('đăng nhập khỏ thành công, có thể do cookie die',"31")

def bao_loi():
    time.sleep(random.uniform(3,5))
    try:
        err_report = driver.find_element(By.XPATH, '//img[@src="../../assets/images/icons-new/error.svg"]')
    except Exception as e:
        err_report = driver.find_element(By.XPATH, '//img[@src="/assets/images/icons-new/error.svg"]')
    err_report.click()
    time.sleep(random.uniform(2.5,3.5))
    # Tạo đối tượng ActionChains
    actions = ActionChains(driver)

    # Cuộn trang xuống
    actions.move_to_element(driver.find_element(By.TAG_NAME, 'body')).send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(random.uniform(3,5))
    button_submit = driver.find_element(By.XPATH, '//button[@class="btn btn-primary btn-sm form-control mt-3"]')
    button_submit.click()
    
    time.sleep(random.uniform(2.5,3.5))
    ok = driver.find_element(By.XPATH, '//button[@type="button" and @class="swal2-confirm swal2-styled"]')
    ok.click()
    
    time.sleep(random.uniform(2.5,3.5))




def like():
    time.sleep(4)

    def lk():
        try:
            # Kiểm tra nếu có nhiều nút "Thích", chọn cái cuối cùng
            like_buttons = WebDriverWait(driver2, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, '//span[@data-ad-rendering-role="thích_button"]'))
            )
            if like_buttons:
                driver2.execute_script("arguments[0].click();", like_buttons[-1])
                return True
        except:
            pass
        
        # Các phương pháp khác để tìm nút "Thích"
        like_xpaths = [
            '//*[contains(text(), "Thích")]',  # Tiếng Việt
            '//*[contains(text(), "Like")]',  # Tiếng Anh
            '//*[@aria-label="Thích"]',
            '//*[@aria-label="Like"]',
            '//div[contains(@class, "x1i10hfl")]'  # Một class phổ biến trên Facebook
        ]

        for xpath in like_xpaths:
            try:
                like_button = WebDriverWait(driver2, 5).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
                driver2.execute_script("arguments[0].click();", like_button)
                return True
            except:
                pass

        return False

    # Thử like bài viết
    if lk():
        return
    else:
        time.sleep(3)

        # Nếu không tìm thấy nút "Thích", thử scroll xuống để tìm
        try:
            for _ in range(4):
                driver2.execute_script("window.scrollBy(0, 200);")
                time.sleep(0.2)
                if lk():
                    return
        except:
            pass
def likereel():
    time.sleep(random.uniform(1.5,2.5))
    try:
        actions = ActionChains(driver2)
        actions.move_by_offset(682,820).click().perform()
        return
    except Exception as e:
        pass
    
def likepage():
    time.sleep(random.uniform(2.5,3.5))
    try:
        likepage = driver2.find_element(By.XPATH, "//*[contains(text(), 'Thích')]")
        likepage.click()
    except Exception as e:
        pass


def log_in_gl(folder_path):
    driver.get('https://app.golike.net/home')
    check = 'tt_gl.txt' in os.listdir(folder_path)
    if check:
        us = input('bạn có muốn dùng lại tài khoản Golike không?(y/n): ')
        if us.lower() == 'y':
            if len(open('tt_gl.txt', 'r').read().split()) != 2:
                print('thông tin bị sai ')
                check = False
            else:
                email , password = open('tt_gl.txt', 'r').read().split()
        else:
            check = False
    if check == False:
        email = input('nhập tên tài khoản golike: ')
        password = input('nhập mật khảu tài khoản golike: ')
        with open('tt_gl.txt', 'w') as f:
            f.write(f"{email} {password}")
    time.sleep(random.uniform(2,3))
    offer_email = driver.find_element(By.XPATH, '//input[@type="text"]')
    slow_typing_with_actionchains(driver, offer_email, email)
    time.sleep(random.uniform(2,3))
    offer_password = driver.find_element(By.XPATH, '//input[@type="password"]')
    slow_typing_with_actionchains(driver, offer_password, password)
    time.sleep(random.uniform(2,3))
    offer_password.send_keys(Keys.ENTER)
    time.sleep(random.uniform(3,5))
    try:
        ktr = driver.find_element(By.XPATH, '//h2[@class="swal2-title" and @id="swal2-title"]')
        ktr = ktr.text
        if ktr == 'Lỗi':
            print('có lỗi xảy ra với tài khoản của bạn, có thể do sai tên tài khoản hoặc mật khẩu')
            with open('tt_gl.txt', 'w') as f:
                f.write(f"")
        else:
            print('đăng nhập thanh công!')
    except Exception as e:
        pass

    





def path_job():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_tool_info()
    time.sleep(2)
    try:
        da_hieu = driver.find_element(By.XPATH, '//*[contains(text(), "Đã hiểu")]')
        da_hieu.click()
        time.sleep(random.uniform(3,5))
    except Exception as e:
        pass
    # driver.get('https://www.golike.net/home')
    time.sleep(random.uniform(2.5,3.5))
    cho_duyet = driver.find_element(By.XPATH, '//div[@class="card shadow-400 bg-gradient-3 h-100 hand"]')
    cho_duyet.click()
    time.sleep(random.uniform(2.5,3.5))
    fb_j = driver.find_element(By.XPATH, '//i[@class="fab fa-facebook-f b200"]')
    fb_j.click()
    time.sleep(random.uniform(1.5,2.5))
    list_job = driver.find_element(By.XPATH, '//i[@class="material-icons"]')
    list_job.click()
    time.sleep(random.uniform(2.5,3.5))
    reacc = input('đổi sang acc bạn thực hiện nhiệm vụ và enter: ')



def get_jobs_fb(us, lj_min, lj_max, wj_min, wj_max):
    """
    Chạy các công việc Facebook nhưng luôn kiểm tra Captcha.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print_tool_info()
    time.sleep(4)
    
    job_thanh_cong = 0
    tien = 0

    for i in range(us):
        try:
            # Kiểm tra Captcha trước khi làm nhiệm vụ
            

            current_time = time.strftime("%Hh- %Mm - %Ss")
            job_offer = driver.find_element(By.XPATH, '//i[@class="material-icons font-light font-18"]')
            job_offer.click()
            time.sleep(random.uniform(1.5, 2.5))

            job = driver.find_element(By.XPATH, '//span[@class="font-18 font-bold b200 block-text"]')
            jobs_type = job.text
            num_cash = driver.find_element(By.XPATH, '//span[@class="hold-prices"]')
            num_cash = int(num_cash.text)

            wh_offer = driver.find_element(By.XPATH, '//img[@src="/assets/images/icons-new/chrome.svg"]')
            wh_offer.click()

            # Kiểm tra Captcha trước khi chuyển tab

            try:
                driver.switch_to.window(driver.window_handles[1])
                link = driver.current_url
                driver.close()
                driver2.get(link)
                driver.switch_to.window(driver.window_handles[0])

                time.sleep(random.uniform(1.5, 2.5))
                driver2.refresh()

                # Kiểm tra Captcha trước khi thực hiện nhiệm vụ

                def demgiay(wj_min, wj_max, jdl, current_time, job_thanh_cong, num_cash, tien):
                    wj = random.randint(wj_min, wj_max)
                    for i in range(wj, -1, -1):
                        print(f"\r{Fore.GREEN}[{jdl}]{Style.RESET_ALL}|{Fore.YELLOW}🔥Quykedo🔥|{Fore.GREEN}Delay:{i}s{Style.RESET_ALL}|", end='', flush=True)
                        time.sleep(1)

                if jobs_type == 'TĂNG LIKE CHO FANPAGE':
                    likepage()
                    demgiay(wj_min, wj_max, i, current_time, job_thanh_cong, num_cash, tien)
                    time.sleep(1)
                elif jobs_type == 'TĂNG LƯỢT THEO DÕI':
                    bao_loi()
                    print(f'\r{Fore.GREEN}-->Đã Hủy Jobs [{i}]{Style.RESET_ALL}')
                    continue
                else:
                    link = driver.current_url
                    if 'reel' in link:
                        likereel()
                        demgiay(wj_min, wj_max, i, current_time, job_thanh_cong, num_cash, tien)
                        time.sleep(1)
                    else:
                        like()
                        demgiay(wj_min, wj_max, i, current_time, job_thanh_cong, num_cash, tien)

                  # Kiểm tra Captcha trước khi hoàn thành job

                time.sleep(2)
                try:
                    hoan_thanh = driver.find_element(By.XPATH, '//img[@src="/assets/images/icons-new/success.svg"]')
                    hoan_thanh.click()
                    time.sleep(random.uniform(3.5, 4.5))

                    ok = driver.find_element(By.XPATH, '//button[@type="button" and @class="swal2-confirm swal2-styled"]')
                    ok.click()

                    tien += num_cash
                    job_thanh_cong += 1

                    print(f"\r{Fore.GREEN}[{i}]{Style.RESET_ALL}|{Fore.YELLOW}🔥Quykedo🔥|{Fore.LIGHTGREEN_EX}Time:{current_time}{Style.RESET_ALL}|{Fore.GREEN}Delay:{0}s{Style.RESET_ALL}|{Fore.LIGHTYELLOW_EX}Job thành công:{job_thanh_cong}{Style.RESET_ALL}|{Fore.MAGENTA}{num_cash}đ{Style.RESET_ALL}|{Fore.CYAN}Tổng: {tien}đ{Style.RESET_ALL}| ", end='', flush=True)

                except:
                    print('Không thấy nút hoàn thành hiện!')
            
            except Exception as e:
                print('Có lỗi xảy ra:', e)
                
            # Kiểm tra Captcha sau khi nhấn "Hoàn thành"
            
            try:
                ok = driver.find_element(By.XPATH, '//button[@type="button" and @class="swal2-confirm swal2-styled"]')
                ok.click()
            except:
                pass

            print()
            time.sleep(random.uniform(lj_min, lj_max))

        except Exception as e:
            bao_loi()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_tool_info()
    log_fb(folder_path)
    time.sleep(2)
    log_in_gl(folder_path)
    while True:
        try:
            us= int(input('bạn có cần giải captcha ko , nếu có thì giải xong nhập số jobs muốn làm: '))
            break
        except ValueError:
            print(f"{Fore.RED}/!\{Style.RESET_ALL}{Fore.YELLOW} Vui lòng nhập số nguyên {Style.RESET_ALL}{Fore.RED}/!\{Style.RESET_ALL}")
    time.sleep(2)
    path_job()
    time.sleep(2)
    
    get_jobs_fb(us,lj_min,lj_max,wj_min,wj_max)

if __name__ == "__main__":
    main()
