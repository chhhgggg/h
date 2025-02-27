import os
import requests 
import sys
import time
from tabulate import tabulate
from pystyle import Write
from tabulate import tabulate
from pystyle import Colorate, Colors
from datetime import datetime
from colorama import Fore, Style, init
import sys
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from pystyle import*
from time import sleep

print('__Các thư viện đã được kiểm tra và cài đặt (nếu cần)__')
os.system('cls' if os.name == 'nt' else 'clear')
#Color
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
purple = "\033[35m"
hong = "\033[1;95m"
#Đánh Dấu Bản Quyền
HĐ_tool = trang + " " + trang + "[" + do + "+_+" + trang + "] " + trang + "=> "
mquang = trang + " " + trang + "[" + do + "÷_+" + trang + "] " + trang + "=> "
thanh = trang + "-------------------------------------------------------------------------"
import os
import requests
import sys
if "requests" not in sys.modules or not hasattr(requests, "get"):
    print("⚠️ Cảnh báo: requests đã bị thay thế! Cút")
    exit()

# Test
import os
import json
import base64
import time
import requests
from datetime import datetime
from colorama import Fore, Style, init
from pystyle import Center, Colorate, Colors

# Khởi tạo màu sắc
init(autoreset=True)

# File lưu key
KEY_FILE = "keytool.txt"

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
                return True, f"✅ Key hợp lệ! Hết hạn: {expiration_date.strftime('%Y-%m-%d %H:%M:%S')} ({days_left} ngày nữa)", key, days_left
            else:
                return False, "❌ Key đã hết hạn!", "", 0
    except:
        return False, "❌ Lỗi khi đọc file key!", "", 0

# Kiểm tra key
is_valid, message, key, days_left = check_saved_key()
print(message)
if not is_valid:
    print("\n🔑 Yêu cầu nhập key mới!")
    exit()

# Hiển thị banner (hiển thị mãi mãi)
def banner():
    banner_text = f'''
    ─────────────────────────────────────────
    🎀✨ Chào mừng bạn đến với Tool ✨🎀
    ─────────────────────────────────────────
    🌸 Chúc bạn một ngày vui vẻ và nhiều may mắn! 🌸
    🐱 Mèo con chúc bạn code không lỗi! 🐱
    ─────────────────────────────────────────
    🔑 Key của bạn: {key}
    📆 Thời hạn còn lại: {days_left} ngày
    ─────────────────────────────────────────
    🛠️ Admin support tool Zalo: 0367742346
    🔗 Chat support: https://zalo.me/g/uaahwq871
    🌐 Web VPN giá rẻ & ID Apple free: timgiare.top ✔️
    ─────────────────────────────────────────
    CopyRight: © KEDO@TOOL
    '''
    print(Colorate.Vertical(Colors.blue_to_green, Center.XCenter(banner_text)))

# Hiển thị menu tool


den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
# Mã màu ANSI cho nhiều màu sắc
rainbow_colors = [
    "\033[91m",  # Đỏ
    "\033[93m",  # Vàng
    "\033[92m",  # Xanh lá
    "\033[96m",  # Xanh dương nhạt
    "\033[94m",  # Xanh dương
    "\033[95m",  # Tím
    "\033[97m"   # Trắng
]

reset_color = "\033[0m"  # Màu mặc định

def in_dong_khung_cau_vong(text):
    # Tạo khung với màu sắc thay đổi cho mỗi ký tự trong thanh ngang và nội dung
    khung_tren = "┌"
    khung_duoi = "└"
    
    for i in range(len(text) + 2):
        khung_tren += rainbow_colors[i % len(rainbow_colors)] + "─" + reset_color
    khung_tren += "┐"
    
    # Tô màu cho nội dung bên trong
    noi_dung = ""
    for i, char in enumerate(text):
        noi_dung += rainbow_colors[i % len(rainbow_colors)] + char
    noi_dung = noi_dung + reset_color
    
    dong_duoc_khung = f"{khung_tren}\n{rainbow_colors[6]}│ {noi_dung} │{reset_color}\n{khung_duoi}"
    
    print(dong_duoc_khung)

# Mã màu ANSI cho nhiều màu sắc
rainbow_colors = [
    "\033[91m",  # Đỏ
    "\033[93m",  # Vàng
    "\033[92m",  # Xanh lá
    "\033[96m",  # Xanh dương nhạt
    "\033[94m",  # Xanh dương
    "\033[95m",  # Tím
    "\033[97m"   # Trắng
]

reset_color = "\033[0m"  # Màu mặc định

def in_mau(text):
    # Tô màu cho nội dung
    noi_dung = ""
    for i, char in enumerate(text):
        noi_dung += rainbow_colors[i % len(rainbow_colors)] + char
    noi_dung += reset_color
    
    print(noi_dung)
    

# Các dòng được đóng khung 7 sắc cầu vồng
print("\033[1;95m╔\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╗")
print("\033[1;95m║  \033[1;32mTool Auto Golike    \033[1;95m║")
print("\033[1;95m╚\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╝")
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [1] Tool Auto TikTok ADB auto follow,tim...')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [1.1] Tool Tiktok Không Auto Click[Mobile]')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [1.2] Tool Auto Facebook[Vip-PC]')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [1.3] Tool Auto Instagram[PC cần giả lập-Mobile]')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [1.4] Tool Auto LinkedIn[PC cần giả lập-Mobile]')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [1.5] Tool Auto X[PC cần giả lập-Mobile]')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [1.6] Tool Auto Threads[PC cần giả lập-Mobile]')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [1.7] Tool Auto Facebook 100% auto Giải Captcha New Update Thử Nghiệm[PC]')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [1.8] Tool Auto Youtube[Giả lập-Mobile]')
print("\033[1;95m╔\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╗")
print("\033[1;95m║  \033[1;32mTool Auto Hustmedia  \033[1;95m║")
print("\033[1;95m╚\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╝")
in_dong_khung_cau_vong('[TOOL]➩ Nhập  [7] Tool Auto Facebook, Instagram[All Thiết Bị]')
print("\033[1;95m╔\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╗")
print("\033[1;95m║  \033[1;32mTool Trao Đổi Sub   \033[1;95m║")
print("\033[1;95m╚\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╝")
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [2] Tool TDS TikTok ADB auto follow,tim...')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [2.1] Tool Auto Facebook[PC]')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [2.2] Tool Auto Facebook[PC+Mobile](die)')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [2.3] Tool Auto Instagram[PC+Mobile](die)')
print("\033[1;95m╔\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╗")
print("\033[1;95m║  \033[1;32mTool Tương Tác Chéo \033[1;95m║")
print("\033[1;95m╚\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╝")
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [3] Tool TTC Facebook[Mobile+PC]')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [3.1] Tool TTC Facebook[PC Untiblock,Vip]')
print("\033[1;95m║  \033[1;32mTool NUÔI FACEBOOK VIP \033[1;95m║")
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [4] Tool Nuôi Facebook[PC]')
print("\033[1;95m║  \033[1;32mTool Tiện ích \033[1;95m║")
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [5] Tool reg profile Facebook [PC+Mobile]')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [5] Tool Chuyển Quản Trị Profile Facebook [PC+Mobile](die)')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [5.2] Tool Unlock follow Tiktok Selenium [PC]')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [5.3] Tool reg Facebook Novery[PC+Mobile]')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [5.4] Tool reg Facebook Full100% Cần Proxy Xịn[PC+Mobile]')
print("\033[1;95m║  \033[1;32mTool Airdrop Auto\033[1;95m║")
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [6] Tool  Midas noproxy[All thiết bị]')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [6.1] Tool Midas proxy[All thiết bị]')


chon = str(input('\033[91mTOOL\033[93m➩ \033[96mNhập Số : \033[92m'))
#golike
if chon == '1':
    exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/glttadb.py').text)
elif chon == '1.2':
    exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/glfb.py').text)
elif chon == '2':
    exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/tdsttadb.py').text)
elif chon == '3':
    exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/ttcfb.py').text)
elif chon == '4':
	exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/nuoifb.py').text)
elif chon == '5':
	exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/regprofile.py').text)
elif chon == '1.3':
	exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/gljg.py').text)
elif chon == '1.4':
	exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/gllink.py').text)
if chon == '3.1':
	exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/ttcfbunti.py').text)
elif chon == '2.2':
	exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/tdsfb.py').text)
elif chon == '5.2':
        exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/unfollow.py').text)
elif chon == '5.4':
	exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/regcloneauto.py').text)
elif chon == '5.3':
	exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/regfbb.py').text)
elif chon == '1.5':
	exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/glx.py').text)
elif chon == '1.6':
	exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/threads.py').text)
elif chon == '2.3':
	exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/igtds.py').text)
elif chon == '1.1':
	exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/gltt.py').text)
elif chon == '1.7':
	exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/qk_fb.py').text)
elif chon == '6':
	exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/midas.py').text)
elif chon == '6.1':
	exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/midas_proxy.py').text)
elif chon == '7':
	exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/menuhust.py').text)
elif chon == '2.1':
	exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/tdsunti.py').text)
elif chon == '1.8':
	exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/glytb.py').text)



	exec(requests.get('accc').text)
else:
    print("Sai Lựa Chọn")
    exit()