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
# Đánh dấu bản quyền
huong_pc= "\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  "
huong_dev= "\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  "
##### Cài Thư Viện #####
try:
    import requests
    import time
    import os 
    import threading
    from art import *
    from colorama import Fore
    from time import sleep
    import json
    import random
    import platform
    import dns.resolver
    import socket
    from tabulate import tabulate
    from pystyle import Colorate, Colors
    from datetime import datetime
    import sys 
    from random import randint
    from pystyle import Write, Colors
    from datetime import datetime
    from time import sleep
    from random_user_agent.user_agent import UserAgent
    from random_user_agent.params import SoftwareName, OperatingSystem

resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['8.8.8.8']
org_socket = socket.getaddrinfo

def google_socket(host, port, family=0, type=0, proto=0, flags=0):
    try:
        info = resolver.resolve(host)
        ip_address = info[0].to_text()
        return org_socket(ip_address, port, family, type, proto, flags)
    except:
        return org_socket(host, port, family, type, proto, flags)

socket.getaddrinfo = google_socket
software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)



total = 0


may = 'mb' if platform.system().lower().startswith('lin') else 'pc'
def banner():
    os.system('cls' if os.name=='nt' else 'clear')
    Write.Print('''     
                      
             ─────────────────────────────────────────
    🎀✨ Chào mừng bạn đến với Tool ✨🎀
    ─────────────────────────────────────────
    🌸 Chúc bạn một ngày vui vẻ và nhiều may mắn! 🌸
    🐱 Mèo con chúc bạn code không lỗi! 🐱
    ─────────────────────────────────────────
      Admin support tool zalo: 0367742346 
                               0348865758
             Chat support: https://zalo.me/g/uaahwq871
             Web mạng vpn giá rẻ, nhận id apple free tại: timgiare.top ✔️
    
    ''',Colors.blue_to_cyan,interval=0.0001)
    Write.Print('''                CopyRight: © KEDO@TOOL\n''',Colors.red_to_purple,interval=0.0001)
    print(red+"-"*70)
    print(f''' ''')
    print(red+"-"*70)
    print('\r\r')
# =======================[ NHẬP KEY ]=======================
 
TOA_DO_FILE = "toa_do.txt"

def lay_toa_do_nut():
    """Lấy tọa độ nút từ người dùng nhập vào hoặc đọc từ file nếu có"""
    if os.path.exists(TOA_DO_FILE):
        try:
            with open(TOA_DO_FILE, "r") as file:
                toa_do = json.load(file)
            print("Sử dụng tọa độ đã lưu:", toa_do)
            return toa_do
        except Exception as e:
            print(f"Lỗi khi đọc tọa độ từ file: {e}, nhập lại tọa độ mới.")

    print("\n=== Cài đặt Tọa độ Nút Bấm ===")
    try:
        follow_x = int(input("Nhập tọa độ X của nút Follow: "))
        follow_y = int(input("Nhập tọa độ Y của nút Follow: "))
        like_x = int(input("Nhập tọa độ X của nút Like: "))
        like_y = int(input("Nhập tọa độ Y của nút Like: "))

        if any(toa_do < 0 for toa_do in [follow_x, follow_y, like_x, like_y]):
            raise ValueError("Tọa độ không thể là số âm")

        toa_do = {
            "follow": (follow_x, follow_y),
            "like": (like_x, like_y)
        }

        # Lưu tọa độ vào file
        with open(TOA_DO_FILE, "w") as file:
            json.dump(toa_do, file)

        print("Tọa độ đã được lưu!")
        return toa_do

    except ValueError as e:
        print(f"Lỗi nhập tọa độ: {str(e)}. Vui lòng nhập số hợp lệ.")
        return None

def kiem_tra_adb():
    """Kiểm tra xem thiết bị có kết nối với ADB hay không"""
    output = os.popen("adb devices").read()
    if "device" in output.split("\n")[1]:  # Dòng thứ hai chứa danh sách thiết bị
        return True
    print("Lỗi: Không tìm thấy thiết bị ADB!")
    return False

def click_tiktok_buttons(toa_do, delay):
    """Click vào nút Follow và thả tim bằng nhấp đúp trên TikTok."""
    if not kiem_tra_adb():
        return False

    try:
        # Click vào nút Follow
        os.system(f"adb shell input tap {toa_do['follow'][0]} {toa_do['follow'][1]}")
        time.sleep(random.uniform(delay, delay + 2))  # Delay ngẫu nhiên để tránh bị phát hiện

        # Nhấp đúp vào màn hình để thả tim (double tap)
        #print("❤️ Nhấp đồng thời vào màn hình để thả tim...")
        x, y = toa_do['like']

        # Chạy 5 lệnh nhấn like đồng thời
        os.system(f"""
            adb shell input tap {x} {y} & 
            adb shell input tap {x} {y} & 
            adb shell input tap {x} {y} & 
            adb shell input tap {x} {y} & 
            adb shell input tap {x} {y}
        """)

        time.sleep(random.uniform(delay, delay + 1))  # Delay tiếp tục
        return True

    except Exception as e:
        print(f"❌ Lỗi khi thực hiện click ADB: {str(e)}")
        return False
def auto_click():
    """Chạy auto click Follow và Like trong một luồng riêng."""
    while True:
        actual_delay = random.randint(delay_min, delay_max)
        click_tiktok_buttons(toa_do_nut, actual_delay)
        #print(f"Đã click, chờ {actual_delay} giây trước lần tiếp theo...")
        time.sleep(actual_delay)
# Chạy chương trình
# Chạy chương trình liên tục
# Chạy chương trình liên tục trong một luồng riêng
toa_do_nut = lay_toa_do_nut()
if toa_do_nut:
    try:
        delay_min = int(input("Nhập thời gian delay tối thiểu giữa các lần click (giây): "))
        delay_max = int(input("Nhập thời gian delay tối đa giữa các lần click (giây): "))

        # Chạy auto click trong thread
        click_thread = threading.Thread(target=auto_click)
        click_thread.daemon = True  # Chạy nền
        click_thread.start()

    except ValueError:
        print("Lỗi: Delay phải là số nguyên!")

def bongoc(so):
    for i in range(so):
        print(red+'────', end = '' )
    print('')
class TraoDoiSub_Api (object):
    def __init__ (self, token):
        self.token = token
    
    def main(self):
        try:
            main = requests.get('https://traodoisub.com/api/?fields=profile&access_token='+self.token).json()
            try:
                return main['data']
            except:
                False
        except:
            return False
    def run(self, user):
        try:
            run = requests.get(f'https://traodoisub.com/api/?fields=tiktok_run&id={user}&access_token={self.token}').json()
            try:
                return run['data']
            except:
                return False
        except:
            return False
    #tiktok_like, tiktok_follow
    def get_job(self, type):
        try:
            get = requests.get(f'https://traodoisub.com/api/?fields={type}&access_token={self.token}')
            return get
        except:
            return False
    
    def cache(self, id, type):
#TIKTOK_LIKE_CACHE, TIKTOK_FOLLOW_CACHE
        try:
            cache = requests.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}').json()
            try:
                cache['cache']
                return True
            except:
                return False
        except:
            return False

    def nhan_xu(self, id, type):
        try:
            nhan = requests.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}')
            try:
                xu = nhan.json()['data']['xu']
                msg = nhan.json()['data']['msg']
                job = nhan.json()['data']['job_success']
                xuthem = nhan.json()['data']['xu_them']
                global total
                total+=xuthem
                bongoc(14)
                print(f'{lam}Nhận Thành Công {job} Nhiệm Vụ {red}| {luc}{msg} {red}| {luc}TOTAL {vang}{total} {luc}Xu {red}| {vang}{xu} ')
                bongoc(14)
                if job == 0:
                    return 0
            except:
                if '"code":"error","msg"' in nhan.text:
                    hien = nhan.json()['msg']; print(red+hien, end = '\r'); sleep(2); print(' '*len(hien), end = '\r')
                else:
                    print(red+'Nhận Xu Thất Bại !', end = '\r'); sleep(2); print('                                                       ', end = '\r')
                return False
        except:
            print(red+'Nhận Xu Thất Bại !', end = '\r'); sleep(2); print('                                                       ', end = '\r')
            return False
def delay(dl):
    try:
        for i in range(dl + 5, -1, -1):  # Tăng thêm 5 giây chờ
            print(f'{vang}[{trang}Đớp{vang}][{trang}'+str(i)+vang+']           ', end='\r')
            sleep(1)
    except:
        sleep(dl + 5)
        print(dl, end='\r')

def chuyen(link, may):
    if may == 'mb':
        os.system(f'xdg-open {link}')
    else:
        os.system(f'cmd /c start {link}')




#----------------------------------------------------------------------------



def main():
    dem=0
    banner()
    while True:
        if os.path.exists('configtds.txt'):
            with open('configtds.txt', 'r') as f:
                token = f.read()
            tds = TraoDoiSub_Api(token)
            data = tds.main()
            try:
                print(f'{huong_pc}{luc}Nhập {vang}[{trang}1{vang}] {luc}Giữ Lại Tài Khoản '+vang+ data['user'] )
                print(f'{huong_pc}{luc}Nhập {vang}[{trang}2{vang}] {luc}Nhập Access_Token TDS Mới')
                chon = input(f'{huong_pc}{luc}Nhập {trang}===>: {vang}')
                if chon == '2':
                    os.remove('configtds.txt')
                elif chon == '1':
                    pass
                else:
                    print(red+'Lựa chọn không xác định !!!');bongoc(14)
                    continue 
            except:
                os.remove('configtds.txt')
        if not os.path.exists('configtds.txt'):
            token = input(f'{huong_pc}{luc}Nhập Access_Token TDS: {vang}')
            with open('configtds.txt', 'w') as f:
                f.write(token)
        with open('configtds.txt', 'r') as f:
            token = f.read()
        tds = TraoDoiSub_Api(token)
        data = tds.main()
        try:
            xu = data['xu']
            xudie = data['xudie']
            user = data['user']
            print(lam+' Đăng Nhập Thành Công ')
            break
        except:
            print(red+'Access Token Không Hợp Lệ! Xin Thử Lại ')
            os.remove('configtds.txt')
            continue 
    bongoc(14)
    
        
#while True:
    #cookie=input('Nhập Cookie Tiktok: ')
    #try:
        #headers={'Host':'www.tiktok.com','sec-ch-ua':'";Not A Brand";v="99", "Chromium";v="94"','sec-ch-ua-mobile':'?1','user-agent':'Mozilla/5.0 (Linux; Android 11; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.56 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','accept':'*/*','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.tiktok.com/foryou?is_from_webapp=v1&is_copy_url=1','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':cookie}
        #info = requests.post(f'https://www.tiktok.com/passport/web/account/info/?aid=1459&app_language=vi-VN&app_name=tiktok_web&battery_info=0.79&browser_language=vi-VN&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20aarch64&browser_version=5.0%20%28Linux%3B%20Android%2011%3B%20vivo%201904%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F94.0.4606.56%20Mobile%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7126951839819712002&device_platform=web_mobile&focus_state=true&from_page=fyp&history_len=28&is_fullscreen=false&is_page_visible=true&os=android&priority_region=VN&referer=&region=VN&screen_height=772&screen_width=360&tz_name=Asia%2FSaigon&webcast_language=vi-VN',headers=headers).json()
        #id_tikok=info['data']['user_id_str']
        #user_tiktok=info['data']['username']
        #name_tiktok=info['data']['screen_name']
        #print('User Tiktok:',user_tiktok)
        #sleep(1)
        #break
    #except:
        #print('Kiểm Tra Lại Cookie')

    banner()
    print(f'{huong_pc}{luc}Tên Tài Khoản: {vang}{user} ')
    print(f'{huong_pc}{luc}Xu Hiện Tại: {vang}{xu}')
    print(f'{huong_pc}{luc}Xu Bị Phạt: {vang}{xudie} ')
    while True:
        ntool=0
        bongoc(14)
        print(f'{huong_pc}{luc}Nhập {red}[{vang}1{red}] {luc}Để Chạy Nhiệm Vụ Tim')
        print(f'{huong_pc}{luc}Nhập {red}[{vang}2{red}] {luc}Để Chạy Nhiệm Vụ Follow')
        print(f'{huong_pc}{luc}Nhập {red}[{vang}3{red}] {luc}Để Chạy Nhiệm Vụ Comment(Đang thử test mà hơi lỏ chạy thử coi🤣)')
        print(f'{huong_pc}{luc}Nhập {red}[{vang}4{red}] {luc}Để Chạy Nhiệm Vụ Follow Tiktok Now')
        nhiem_vu = input(f'{huong_pc}{luc}Nhập số nhiệm vụ (cách nhau bằng dấu phẩy, VD: 1,2): {vang}')
        
        nhiem_vu = nhiem_vu.replace(" ", "").split(",")  # Xóa khoảng trắng và tách danh sách
        dl = int(input(f'{huong_pc}{luc}Nhập Delay: {vang}'))
        while True:
            if ntool == 2:
                break
            ntool = 0
            bongoc(14)
            nv_nhan=int(input(f'{huong_pc}{luc}Sau Bao Nhiêu Nhiệm Vụ Thì Nhận Xu: {vang}'))
            if nv_nhan < 8:
                print(red+'Trên 8 Nhiệm Vụ Mới Được Nhận Tiền!')
                continue
            if nv_nhan > 15:
                print(red+'Nhận Xu Dưới 15 Nhiệm Vụ Để Tránh Lỗi')
                continue
            user_cau_hinh=input(f'{huong_pc}{luc}Nhập User Name Tik Tok Cần Cấu Hình: {vang}')
            cau_hinh=tds.run(user_cau_hinh)
            if cau_hinh != False:
                user=cau_hinh['uniqueID']
                id_acc=cau_hinh['id']
                bongoc(14)
                print(f'{luc}Đang Cấu Hình ID: {vang}{id_acc} {red}| {luc}User: {vang}{user} {red}| ')
                bongoc(14)
            else:
                print(f'{red}Cấu Hinh Thất Bại User: {vang}{user_cau_hinh} ')
                continue 
            while True:
                if ntool==1 or ntool==2:break
                if '1' in nhiem_vu:
                    listlike = tds.get_job('tiktok_like')
                    if listlike == False:
                        print(red+'Không Get Được Nhiệm Vụ Like              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                    elif 'error' in listlike.text:
                        if listlike.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            coun = listlike.json()['countdown']
                            print(f'{red}Đang Get Nhiệm Vụ Like, COUNTDOWN: {str(round(coun, 3))} ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
                        elif listlike.json()['error'] == 'Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
                            nhan = tds.nhan_xu('TIKTOK_LIKE_API', 'TIKTOK_LIKE') #TIKTOK_LIKE, TIKTOK_FOLLOW, TIKTOK_COMMENT
                        else:
                            print(red+listlike.json()['error'] , end ='\r');sleep(2); print('                                                        ', end = '\r')
                    else:
                        try:
                            listlike = listlike.json()['data']
                        except:
                            print(red+'Hết Nhiệm Vụ Like                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                            continue
                        if len(listlike) == 0:
                            print(red+'Hết Nhiệm Vụ Like                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                        else:
                            print(f'{luc}Tìm Thấy {vang}{len(listlike)} {luc}Nhiệm Vụ Like                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                            for i in listlike:
                                id = i['id']
                                link = i['link']
                                chuyen(link, may)
                                cache = tds.cache(id, 'TIKTOK_LIKE_CACHE')
                                if cache != True:
                                    tg=datetime.now().strftime('%H:%M:%S')
                                    hien = f'{vang}[{red}X{vang}] {red}| {lam}{tg} {red}| {vang}TIM {red}| {trang}{id} {red}|'; print(hien, end = '\r');sleep(1); print('                                                                                        ', end = '\r')
                                else:
                                    dem+=1
                                    tg=datetime.now().strftime('%H:%M:%S')
                                    print(f'{vang}[{trang}{dem}{vang}] {red}| {lam}{tg} {red}| {Colorate.Horizontal(Colors.yellow_to_red, "TIM")} {red}| {trang}{id} {red}|')
                                    delay(dl)
                                    if dem % nv_nhan == 0:
                                        nhan = tds.nhan_xu('TIKTOK_LIKE_API', 'TIKTOK_LIKE')
                                        if nhan == 0:
                                            print(luc+'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ') 
                                            print(f'{huong_pc}{luc}Nhập {red}[{vang}1{red}] {luc}Để Thay Nhiệm Vụ ')
                                            print(f'{huong_pc}{luc}Nhập {red}[{vang}2{red}] {luc}Thay Acc Tiktok ')
                                            print(f'{huong_pc}{luc}Nhấn {red}[{vang}Enter{red}] {luc}Để Tiếp Tục')
                                            chon=input(f'{huong_pc}{luc}Nhập {trang}===>: {vang}')
                                            if chon == '1':
                                                ntool=2
                                                break
                                            elif chon =='2':
                                                ntool = 1
                                                break
                                            bongoc(14)
                if ntool==1 or ntool==2:break
                if '2' in nhiem_vu:
                    listfollow = tds.get_job('tiktok_follow')
                    if listfollow == False:
                        print(red+'Không Get Được Nhiệm Vụ Follow              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                    elif 'error' in listfollow.text:
                        if listfollow.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            coun = listfollow.json()['countdown']
                            print(red+f'Đang Get Nhiệm Vụ Follow, COUNTDOWN: {str(round(coun, 3))} ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
                        elif listfollow.json()['error'] == 'Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
                            nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW') #TIKTOK_LIKE, TIKTOK_FOLLOW, TIKTOK_COMMENT
                        else:
                            print(red+listfollow.json()['error'] , end ='\r');sleep(2); print('                                                        ', end = '\r')
                    else:
                        try:
                            listfollow = listfollow.json()['data']
                        except:
                            print(red+'Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                            continue
                        if len(listfollow) == 0:
                            print(red+'Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                        else:
                            print(luc+f'Tìm Thấy {vang}{len(listfollow)} {luc}Nhiệm Vụ Follow                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                            for i in listfollow:
                                id = i['id']
                                link = i['link']
                                chuyen(link, may)
                                cache = tds.cache(id, 'TIKTOK_FOLLOW_CACHE')
                                if cache != True:
                                    tg=datetime.now().strftime('%H:%M:%S')
                                    hien = f'{vang}[{red}X{vang}] {red}| {lam}{tg} {red}| {vang}FOLLOW {red}| {trang}{id} {red}|'; print(hien, end = '\r');sleep(1); print('                                                                                        ', end = '\r')
                                else:
                                    dem+=1
                                    tg=datetime.now().strftime('%H:%M:%S')
                                    print(f'{vang}[{trang}{dem}{vang}] {red}| {lam}{tg} {red}| {Colorate.Horizontal(Colors.yellow_to_red, "FOLLOW")} {red}| {trang}{id} {red}|')
                                    delay(dl)
                                    if dem % nv_nhan == 0:
                                        nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW')
                                        if nhan == 0:
                                            print(luc+'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ') 
                                            print(f'{huong_pc}{luc}Nhập {red}[{vang}1{red}] {luc}Để Thay Nhiệm Vụ ')
                                            print(f'{huong_pc}{luc}Nhập {red}[{vang}2{red}] {luc}Thay Acc Tiktok ')
                                            print(f'{huong_pc}{luc}Nhấn {red}[{vang}Enter{red}] {luc}Để Tiếp Tục')
                                            chon=input(f'{huong_pc}{luc}Nhập {trang}===>: {vang}')
                                            if chon == '1':
                                                ntool=2
                                                break
                                            elif chon =='2':
                                                ntool = 1
                                                break
                                            bongoc(14)
                if ntool==1 or ntool==2:break
                if '3' in nhiem_vu:  # Thêm tùy chọn cho nhiệm vụ comment
                    listcomment = tds.get_job('tiktok_comment')
                    if not listcomment:  # Kiểm tra nếu request thất bại
                        print(red + 'Không Get Được Nhiệm Vụ Comment', end='\r')
                        sleep(2)
                        continue
                    try:
                       response = listcomment.json()  # Chuyển đổi JSON
                    except Exception as e:
                       print(red + 'Lỗi khi parse JSON:', str(e), end='\r')
                       sleep(2)
                       continue
                    if isinstance(response, dict) and 'error' in response:  # Kiểm tra JSON hợp lệ
                       error_msg = response['error']
                       
                       if error_msg == 'Thao tác quá nhanh vui lòng chậm lại':
                           coun = listcomment.json()['countdown']
                           print(f'{red}Đang Get Nhiệm Vụ Comment, COUNTDOWN: {str(round(coun, 3))} ', end='\r')
                           sleep(2)
                       elif error_msg == 'Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
                        
                          nhan = tds.nhan_xu('TIKTOK_COMMENT_API', 'TIKTOK_COMMENT') 
                       else:
                          print(red+listcomment.json()['error'], end='\r')
                          sleep(2)
                       continue
                    try:
                       listcomment = response.get('data', [])  # Lấy danh sách nhiệm vụ comment
                    except:
                       print(red + 'Hết Nhiệm Vụ Comment', end='\r')
                       sleep(2)
                       continue
                

                    if len(listcomment) == 0:
                        print(red+'Hết Nhiệm Vụ Comment', end='\r')
                        sleep(2)
                    else:
                        print(f'{luc}Tìm Thấy {vang}{len(listcomment)} {luc}Nhiệm Vụ Comment', end='\r')
                        sleep(2)
                        for i in listcomment:
                            id = i['id']
                            link = i['link']
                            noidung = i['noidung']  # Lấy nội dung cần comment
                            chuyen(link, may)
                            cache = tds.cache(id, 'TIKTOK_COMMENT_CACHE')

                            if cache != True:
                                tg = datetime.now().strftime('%H:%M:%S')
                                hien = f'{vang}[{red}X{vang}] {red}| {lam}{tg} {red}| {vang}COMMENT {red}| {trang}{id} {red}| {lam}Nội dung: {trang}{noidung} {red}|'
                                print(hien, end='\r')
                                sleep(1)
                            else:
                                dem += 1
                                tg = datetime.now().strftime('%H:%M:%S')
                                print(f'{vang}[{trang}{dem}{vang}] {red}| {lam}{tg} {red}| {Colorate.Horizontal(Colors.yellow_to_red, "COMMENT")} {red}| {trang}{id} {red}| {lam}Nội dung: {trang}{noidung} {red}|')
                                delay(dl)
                            if dem % nv_nhan == 0:
                               nhan = tds.nhan_xu('TIKTOK_COMMENT_API', 'TIKTOK_COMMENT')
                            if nhan == 0:
                               print(luc+'Nhận Xu Thất Bại, Acc TikTok Của Bạn Ổn Chứ?') 
                               print(f'{huong_pc}{luc}Nhập {red}[{vang}1{red}] {luc}Để Thay Nhiệm Vụ')
                               print(f'{huong_pc}{luc}Nhập {red}[{vang}2{red}] {luc}Thay Acc TikTok')
                               print(f'{huong_pc}{luc}Nhấn {red}[{vang}Enter{red}] {luc}Để Tiếp Tục')
                               chon = input(f'{huong_pc}{luc}Nhập {trang}===>: {vang}')
                            if chon == '1':
                                ntool = 2
                                break
                            elif chon == '2':
                                ntool = 1
                                break
                            bongoc(14)         
                if '4' in nhiem_vu:
                    listfollow = tds.get_job('tiktok_follow')
                    if listfollow == False:
                        print(red+'Không Get Được Nhiệm Vụ Follow              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                    elif 'error' in listfollow.text:
                        if listfollow.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            coun = listfollow.json()['countdown']
                            print(f'{red}Đang Get Nhiệm Vụ Follow, COUNTDOWN: {str(round(coun, 3))} ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
                        elif listfollow.json()['error'] == 'Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
                            nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW') #TIKTOK_LIKE, TIKTOK_FOLLOW, TIKTOK_COMMENT
                        else:
                            print(red+listfollow.json()['error'] , end ='\r');sleep(2); print('                                                        ', end = '\r')
                    else:
                        try:
                            listfollow = listfollow.json()['data']
                        except:
                            print(red+'Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                            continue
                        if len(listfollow) == 0:
                            print(red+'Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                        else:
                            print(f'{luc}Tìm Thấy {vang}{len(listfollow)} {luc}Nhiệm Vụ Follow                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                            for i in listfollow:
                                id = i['id']
                                uid = id.split('_')[0] 
                                link = i['link']
                                que = i['uniqueID']
                                if may == 'mb':
                                    chuyen(f'tiktoknow://user/profile?user_id={uid}', may)
                                else:
                                    chuyen(f'https://now.tiktok.com/@{que}', may)
                                cache = tds.cache(id, 'TIKTOK_FOLLOW_CACHE')
                                if cache != True:
                                    tg=datetime.now().strftime('%H:%M:%S')
                                    hien = f'{vang}[{red}X{vang}] {red}| {lam}{tg} {red}| {vang}FOLLOW_TIKTOK_NOW {red}| {trang}{id} {red}|'; print(hien, end = '\r');sleep(1); print('                                                                                        ', end = '\r')
                                else:
                                    dem+=1
                                    tg=datetime.now().strftime('%H:%M:%S')
                                    print(f'{vang}[{trang}{dem}{vang}] {red}| {lam}{tg} {red}| {Colorate.Horizontal(Colors.yellow_to_red, "FOLLOW_TIKTOK_NOW")} {red}| {trang}{id} {red}|')
                                    delay(dl)
                                    if dem % nv_nhan == 0:
                                        nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW')
                                        if nhan == 0:
                                            print(luc+'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ') 
                                            print(f'{huong_pc}{luc}Nhập {red}[{vang}1{red}] {luc}Để Thay Nhiệm Vụ ')
                                            print(f'{huong_pc}{luc}Nhập {red}[{vang}2{red}] {luc}Thay Acc Tiktok ')
                                            print(f'{huong_pc}{luc}Nhấn {red}[{vang}Enter{red}] {luc}Để Tiếp Tục')
                                            chon=input(f'{huong_pc}{luc}Nhập {trang}===>: {vang}')
                                            if chon == '1':
                                                ntool=2
                                                break
                                            elif chon =='2':
                                                ntool = 1
                                                break
                                            bongoc(14)
main()
