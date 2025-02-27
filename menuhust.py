xanhduong ='\033[34m'
try:
    import requests, json, numpy
    from pystyle import Colors, Write
    import os, pystyle, cv2
    import base64
    from datetime import datetime
    import random
    from time import sleep
    import os
    import requests
# URL của file api.py trên GitHub

except ImportError as e:
    print(f"Lỗi: {e}")
    print("Có vẻ như một số module chưa được cài đặt.")


user_input = input("Bạn lần đầu chạy thì hãy nhập y lần sau cứ nhập n nhé, chỉ cần cài lần đầu (y/n): ").strip().lower()

if user_input in ['y', 'yes']:
    os.system('pip3 install requests')
    os.system('pip3 install pystyle')
    os.system('pip3 install pyfiglet')
    os.system('pip3 install numpy')
    os.system('pip3 install dnspython')
    os.system('install tabulate')
    os.system('pip3 install opencv-python-headless')
    print("Cài đặt hoàn tất.")
GITHUB_URL = "https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/api.py"
# Đường dẫn lưu file
FILE_PATH = "api.py"

# Kiểm tra xem file đã tồn tại chưa
if not os.path.exists(FILE_PATH):
    pass#print("File api.py chưa tồn tại. Đang tải xuống...")
    
    try:
        response = requests.get(GITHUB_URL)
        response.raise_for_status()  # Kiểm tra lỗi HTTP

        # Lưu file vào thư mục hiện tại
        with open(FILE_PATH, "wb") as file:
            file.write(response.content)
        
        pass#print("Tải xuống thành công!")

    except requests.RequestException as e:
        pass#print(f"Lỗi khi tải file: {e}")
else:
    pass#print("File api.py đã tồn tại.")
    print("Đang vào tool...")
    
if 'nt' in os.name:
    os.system('cls')
else:
    os.system('clear')
do = '\033[31m'
xanhla ='\033[32m' 
vang ='\033[33m'
tim ='\033[35m'
xanhCyan ='\033[36m'
trang ='\033[37m'

a = 'KEDO-TOOLS'
link = 'yt:https://youtube.com/@mletool'
Write.Print('    ',Colors.purple_to_blue,interval=0.0001)
Write.Print('   ',Colors.purple_to_blue,interval=0.0001)
Write.Print('   ',Colors.yellow,interval=0.0001)
Write.Print('  ',Colors.purple_to_blue,interval=0.0001)
Write.Print('   ',Colors.yellow,interval=0.001)
Write.Print(link,Colors.blue_to_red,interval=0.001)
Write.Print('',Colors.yellow,interval=0.001)
Write.Print(' ',Colors.purple_to_blue,interval=0.0001)
Write.Print('     ',Colors.yellow,interval=0.001)
Write.Print('     made by : ',Colors.red_to_purple,interval=0.001)
Write.Print('   MLE×QUY      ',Colors.white_to_blue,interval=0.001)
Write.Print('',Colors.yellow,interval=0.001)
Write.Print('',Colors.purple_to_blue,interval=0.0001)
Write.Print('    \n',Colors.yellow,interval=0.001)
Write.Print('TOOL HUST MEDIA    \n',Colors.pink,interval=0.001)
print(f'{do}[{trang}×_×{do}]{xanhduong}==>{xanhla} nhập{tim} [{xanhCyan}1{tim}] {xanhla}Tools auto facebook')
print(f'{do}[{trang}×_×{do}]{xanhduong}==>{xanhla} nhập{tim} [{xanhCyan}2{tim}] {xanhla}Tools auto instagram{trang}')
print(f'{trang}---------------------------------')
luachon = input(f'{xanhla}[{xanhCyan}KEDO-Tools{xanhla}]{xanhla}==>{tim} nhập lựa chọn của bạn : ')
if luachon == '1':
    exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/runfb.py').text)
if luachon == '2':
    exec(requests.get('https://raw.githubusercontent.com/mleccuuuu/cc/refs/heads/main/run.py').text)
 

else:
    print('sai dữ liệu vui lòng vào lại tool')
