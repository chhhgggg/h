import os
import requests
import sys
import time
import json
import base64
from datetime import datetime

# File lưu key
KEY_FILE = "datavlkey.txt"

# Hàm giải mã dữ liệu
def decrypt_data(encrypted_data):
    return base64.b64decode(encrypted_data.encode()).decode()

# Kiểm tra key đã lưu
def check_saved_key():
    if not os.path.exists(KEY_FILE):
        return False, "Không tìm thấy key đã lưu!"

    try:
        with open(KEY_FILE, "r") as file:
            encrypted_data = file.read()
            data = json.loads(decrypt_data(encrypted_data))

            key = data.get("key", "")
            expiration_date = datetime.fromisoformat(data["expiration_date"])

            if expiration_date > datetime.now():
                days_left = (expiration_date - datetime.now()).days
                return True, f"Key hợp lệ! Hết hạn: {expiration_date.strftime('%Y-%m-%d %H:%M:%S')} ({days_left} ngày nữa)", key, days_left
            else:
                return False, "Key đã hết hạn!", "", 0
    except:
        return False, "Lỗi khi đọc file key!", "", 0

# Kiểm tra key
is_valid, message, key, days_left = check_saved_key()
print(message)
if not is_valid:
    print("\nYêu cầu nhập key mới!")
    exit()

# Hiển thị banner
def banner():
    banner_text = f'''
    ----------------------------------------
    Chào mừng bạn đến với Tool
    ----------------------------------------
    Chúc bạn một ngày vui vẻ và nhiều may mắn!
    Mèo con chúc bạn code không lỗi!
    ----------------------------------------
    Key của bạn: {key}
    Thời hạn còn lại: {days_left} ngày
    ----------------------------------------
    Admin support tool Zalo: 0367742346
    Chat support: https://zalo.me/g/uaahwq871
    Web VPN giá rẻ & ID Apple free: timgiare.top
    ----------------------------------------
    CopyRight: © KEDO@TOOL
    '''
    print(banner_text)

# Hiển thị menu tool
print("----------------------------------------")
print("Tool Auto Golike")
print("----------------------------------------")
print("[1] Tool Auto TikTok ADB auto follow, tim...")
print("[1.1] Tool Tiktok Không Auto Click[Mobile]")
print("[1.2] Tool Auto Facebook[Vip-PC]")
print("[1.3] Tool Auto Instagram[PC cần giả lập-Mobile]")
print("[1.4] Tool Auto LinkedIn[PC cần giả lập-Mobile]")
print("[1.5] Tool Auto X[PC cần giả lập-Mobile]")
print("[1.6] Tool Auto Threads[PC cần giả lập-Mobile]")
print("[1.7] Tool Auto Facebook 100% auto Giải Captcha New Update Thử Nghiệm[PC]")
print("[1.8] Tool Auto Youtube[Giả lập-Mobile]")

print("----------------------------------------")
print("Tool Auto Hustmedia")
print("----------------------------------------")
print("[7] Tool Auto Facebook, Instagram[All Thiết Bị]")

print("----------------------------------------")
print("Tool Trao Đổi Sub")
print("----------------------------------------")
print("[2] Tool TDS TikTok ADB auto follow, tim...")
print("[2.1] Tool Auto Facebook[PC]")
print("[2.2] Tool Auto Facebook[PC+Mobile](die)")
print("[2.3] Tool Auto Instagram[PC+Mobile](die)")

print("----------------------------------------")
print("Tool Tương Tác Chéo")
print("----------------------------------------")
print("[3] Tool TTC Facebook[Mobile+PC]")
print("[3.1] Tool TTC Facebook[PC Untiblock,Vip]")

print("----------------------------------------")
print("Tool Nuôi Facebook VIP")
print("----------------------------------------")
print("[4] Tool Nuôi Facebook[PC]")

print("----------------------------------------")
print("Tool Tiện ích")
print("----------------------------------------")
print("[5] Tool reg profile Facebook [PC+Mobile]")
print("[5.1] Tool Chuyển Quản Trị Profile Facebook [PC+Mobile](die)")
print("[5.2] Tool Unlock follow Tiktok Selenium [PC]")
print("[5.3] Tool reg Facebook Novery[PC+Mobile]")
print("[5.4] Tool reg Facebook Full100% Cần Proxy Xịn[PC+Mobile]")

print("----------------------------------------")
print("Tool Airdrop Auto")
print("----------------------------------------")
print("[6] Tool Midas noproxy[All thiết bị]")
print("[6.1] Tool Midas proxy[All thiết bị]")

chon = str(input('Nhập số: '))

# Kiểm tra lựa chọn và thực thi script từ URL
script_urls = {
    '1': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/glttadb.py',
    '1.1': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/gltt.py',
    '1.2': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/glfb.py',
    '1.3': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/gljg.py',
    '1.4': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/gllink.py',
    '1.5': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/glx.py',
    '1.6': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/threads.py',
    '1.7': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/qk_fb.py',
    '1.8': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/glytb.py',
    '2': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/tdsttadb.py',
    '2.1': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/tdsunti.py',
    '2.2': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/tdsfb.py',
    '2.3': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/igtds.py',
    '3': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/ttcfb.py',
    '3.1': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/ttcfbunti.py',
    '4': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/nuoifb.py',
    '5': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/regprofile.py',
    '5.2': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/unfollow.py',
    '5.3': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/regfbb.py',
    '5.4': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/regcloneauto.py',
    '6': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/midas.py',
    '6.1': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/midas_proxy.py',
    '7': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/menuhust.py'
}

if chon in script_urls:
    exec(requests.get(script_urls[chon]).text)
else:
    print("Sai lựa chọn!")
    exit()
