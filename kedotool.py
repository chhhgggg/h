print("  Đang tạo key...")
print("  Nếu lỗi vui lòng tạo một folder khác nhét file tool vào ...")
print("  Chúng tôi phát hiện ra nhiều thành phần đem tool của chúng tôi đi bán...")
print("  Cho nên chúng tôi đg cố gắng bảo vệ tool...")
print("  Hãy thông cảm cho chúng tôi nếu bạn gặp lỗi...")
try:
            
    from datetime import datetime
    import random
    from time import sleep
    import os
    
# URL của file api.py trên GitHub
except ImportError as e:
    print(f"Lỗi: {e}")
    pass#print("Có vẻ như một số module chưa được cài đặt.")
user_input = input("  Nếu bạn lần đầu chạy, Bạn là người mới?thì hãy nhập y lần sau cứ nhập n nhé, chỉ cần cài lần đầu (y/n): ").strip().lower()
if user_input in ['y', 'yes']:
    os.system('pip install requests')
    os.system('pip install pystyle')
    os.system('pip install pyfiglet')
    os.system('pip install numpy')
    os.system('pip install dnspython')
    os.system('pip install tabulate')
    os.system('pip install bs4')
    os.system('pip install rich')        
    os.system('pip install random_user_agent')
    os.system('pkg install android-tools')   
    print("Cài đặt hoàn tất. Vui lòng chạy lại chương trình!")
    sleep(1)  # Đợi 2 giây rồi thoát
    exit()  

import os
import sys
import json
import base64
import requests
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
import os
import sys
import json
import base64
import requests
import glob
import hashlib  # Tạo checksum
import socket  # ✅ Thêm dòng này để tránh lỗi
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
import os
import sys
import json
import base64
import requests
import glob  # Thư viện tìm file
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
import psutil
import time

# 🔴 Kiểm tra xem requests có bị thay thế không
if "requests" not in sys.modules or not hasattr(requests, "get"):
    print("⚠️ Lỗi.")
    sys.exit()

# 🔴 Kiểm tra HTTPS
# 🔴 Kiểm tra file đáng ngờ
def check_suspicious_files():
    # Lấy danh sách file trong thư mục hiện tại
    all_files = os.listdir()

    for file in all_files:
        # Điều kiện kiểm tra:
        if (
            file.lower().startswith("re")  # Bắt đầu bằng "re"
            or file.lower() == "requestes.py"  # Tên chính xác là "requestes"
            or (file.startswith("Re") and file.endswith(".txt"))  # Bắt đầu "Re." và có đuôi ".txt".     
            or (file.startswith("Re") and file.endswith(".exe")) 
            or (file.startswith("re") and file.endswith(".exe")) 
            or (file.startswith("Bug") and file.endswith(".txt")) 
            or (file.startswith("Bug") and file.endswith(".py")) 
            or (file.startswith("Bug") and file.endswith(".exe")) 
            or (file.startswith("Bug") and file.endswith(".bat")) 
            or (file.startswith("re") and file.endswith(".bat")) 
            or (file.startswith("Check") and file.endswith(".txt")) 
            or (file.startswith("Check") and file.endswith(".py")) 
            or (file.startswith("Check") and file.endswith(".exe")) 
            or (file.startswith("check") and file.endswith(".exe")) 
            or (file.startswith("bat") and file.endswith(".exe")) 
            or (file.startswith("bat") and file.endswith(".bat")) 
            or (file.startswith("check") and file.endswith(".bat")) 
            or (file.startswith("Check") and file.endswith(".bat")) 
            or (file.startswith("Re") and file.endswith(".bat")) 
            or (file.startswith("re") and file.endswith(".bat"))  
            
            
            
        ):
            print(f"⚠️        Lỗi .")
            sys.exit()

# Chạy kiểm tra file
check_suspicious_files()
# 🔴 Kiểm tra xem file gốc có bị chỉnh sửa không


# Chạy các kiểm tra liên tục trong nền

KEY_FILE = "datavlkey.txt"

# URL chứa danh sách key từ GitHub
KEY_GITHUB_URL = "https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/key.txt"

# API Token của Link4m (cần thay thế bằng token của bạn)
TOKEN_LINK4M = "668bc1beab3a3470326ea5fd"
#https://link4m.co/api-shorten/v2?api=668bc1beab3a3470326ea5fd&url=yourdestinationlink.com
# Mã hóa & giải mã dữ liệu
def encrypt_data(data):
    return base64.b64encode(data.encode()).decode()

def decrypt_data(encrypted_data):
    return base64.b64decode(encrypted_data.encode()).decode()

# Lấy danh sách key từ GitHub
def get_keys_from_github():
    try:
        response = requests.get(KEY_GITHUB_URL, timeout=5)
        if response.status_code == 200:
            lines = response.text.strip().split("\n")
            keys = {}
            for line in lines:
                parts = line.split("-")
                if len(parts) == 2 and parts[1].strip().endswith("day"):
                    key = parts[0].strip()
                    days = int(parts[1].replace("day", "").strip())
                    expiration_date = datetime.now() + timedelta(days=days)
                    keys[key] = expiration_date
            return keys
    except requests.ConnectionError:
        print("\033[1;91mKiểm tra kết nối mạng.")
    return {}

# Lấy địa chỉ IP
def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        return response.json().get('ip', 'Unknown')
    except requests.ConnectionError:
        print("\033[1;91mKhông thể lấy địa chỉ IP! Kiểm tra kết nối mạng.")
        sys.exit()

# Tạo key từ IP (hết hạn trong ngày)
def generate_key(ip_address):
    ngay = int(datetime.now().day)
    key1 = str(ngay * 27 + 27)
    ip_numbers = ''.join(filter(str.isdigit, ip_address))
    key = f'Key{key1}{ip_numbers}'

    expiration_date = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    url = f'https://mlevip.blogspot.com/2025/02/key-ngay-hom-nay-la-function-updatetime_27.html?ma={key}'
    
    return url, key, expiration_date

# Rút gọn URL bằng Link4m
def get_shortened_link_link4m(url):#TOKEN_LINK4M # https://link4m.co/api-shorten/v2?api={TOKEN_LINK4M}&url={url}
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

# Lưu key vào file
def save_key(key, expiration_date):
    data = {"key": key, "expiration_date": expiration_date.isoformat()}
    encrypted_data = encrypt_data(json.dumps(data))
    with open(KEY_FILE, "w") as file:
        file.write(encrypted_data)

# Đọc key đã lưu
def load_saved_key():
    if not os.path.exists(KEY_FILE):
        return None, None  

    try:
        with open(KEY_FILE, "r") as file:
            encrypted_data = file.read()
            data = json.loads(decrypt_data(encrypted_data))

            expiration_date = datetime.fromisoformat(data["expiration_date"])
            if expiration_date > datetime.now():
                return data["key"], expiration_date  
            else:
                print("\033[1;91mKey đã hết hạn! Vui lòng nhập key mới.")
                return None, None
    except (json.JSONDecodeError, KeyError):
        return None, None

# Kiểm tra & lấy key
def main():
    ip_address = get_ip_address()
    saved_key, saved_expiration = load_saved_key()

    if saved_key:
        print(f"\033[1;92mKey hợp lệ! Hết hạn lúc: {saved_expiration.strftime('%Y-%m-%d %H:%M:%S')}")
        return

    # Lấy key GitHub & tạo key Link4m song song
    with ThreadPoolExecutor(max_workers=2) as executor:
        github_future = executor.submit(get_keys_from_github)
        url, link4m_key, expiration_date = generate_key(ip_address)
        link4m_future = executor.submit(get_shortened_link_link4m, url)

        keys_from_github = github_future.result()
        link4m_short_url = link4m_future.result()

    print("\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;32mNhập Key Để Dùng Tool")

    if link4m_short_url:
        print(f"\033[1;35mVượt link để lấy key : \033[1;36m{link4m_short_url}")
        print(f" Nếu Bạn Đang Gặp Vấn Đề Về Vượt Link Không Được Thì Hãy Coi Video Từ Link Này, Sao Chép Lên GG xem nhé, link HD: https://youtu.be/3tztAr-W_gA?si=XYc-DfBa6z7kekur ")
    while True:
        try:
            keynhap = input("\033[1;33mNhập Key: \033[1;32m").strip()
            
            # Kiểm tra key từ Link4m
            if keynhap == link4m_key:
                print(f"\033[1;92mKey hợp lệ! Hết hạn lúc: {expiration_date.strftime('%Y-%m-%d %H:%M:%S')}")
                save_key(keynhap, expiration_date)
                return
            
            # Kiểm tra key từ GitHub
            elif keynhap in keys_from_github:
                expiration_date = keys_from_github[keynhap]  
                print(f"\033[1;92mKey hợp lệ! Hết hạn lúc: {expiration_date.strftime('%Y-%m-%d %H:%M:%S')}")
                save_key(keynhap, expiration_date)  
                return

            else:
                print("\033[1;91mKey sai! Vui lòng nhập lại.")
        
        except KeyboardInterrupt:
            print("\n\033[1;91mThoát tool!")
            sys.exit()
 
if __name__ == '__main__':
    main()

    while True:
        try:
            response = requests.get('https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/menu.py', timeout=5)
            exec(response.text)
        except requests.ConnectionError:
            print("\033[1;91mMất kết nối! Tool sẽ tự động thoát.")
            sys.exit()
        except KeyboardInterrupt:
            print("\n\033[1;91mCảm ơn bạn đã dùng Tool!")
            sys.exit()
