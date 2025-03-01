import requests
import time
import dns.resolver
import socket
from sys import platform
from time import sleep
from datetime import datetime
from random import randint
import base64
import uuid, re
from colored import stylize, fg
from art import *  # Nếu dùng thư viện art
from bs4 import BeautifulSoup
from colorama import Fore, Style

resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['8.8.8.8']
org_socket = socket.getaddrinfo
RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
BLUE = Fore.BLUE
RESET = Style.RESET_ALL
MAGENTA = Fore.MAGENTA

def google_socket(host, port, family=0, type=0, proto=0, flags=0):
    try:
        info = resolver.resolve(host)
        ip_address = info[0].to_text()
        return org_socket(ip_address, port, family, type, proto, flags)
    except:
        return org_socket(host, port, family, type, proto, flags)

socket.getaddrinfo = google_socket
def _encode_to_base64(_data):
	byte_representation = _data.encode('utf-8')
	base64_bytes = base64.b64encode(byte_representation)
	base64_string = base64_bytes.decode('utf-8')
	return base64_string
def _Infofb(cookie):
    heads={
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7", 
        "content-type": "application/x-www-form-urlencoded", 
        "sec-ch-prefers-color-scheme": "light", 
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"", 
        "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"", 
        "sec-ch-ua-mobile": "?0", 
        "sec-ch-ua-model": "\"\"", 
        "sec-ch-ua-platform": "\"Linux\"", 
        "sec-ch-ua-platform-version": "\"\"", 
        "sec-fetch-dest": "empty", 
        "sec-fetch-mode": "cors", 
        "sec-fetch-site": "same-origin", 
        "x-asbd-id": "129477", 
        "x-fb-friendly-name": "ProfileCometTimelineListViewRootQuery", 
        "x-fb-lsd": "7_RkODA0fo-6ShZlbFpHEW"
    }
    get = requests.get("https://www.facebook.com/me", headers=heads, cookies={"cookie": cookie})
    try:
        get = get.url
        get = requests.get(get, headers=heads, cookies={"cookie": cookie}).text
        _sea = get.split(',"NAME":"')[1].split('",')[0]
        _name = bytes(_sea, "utf-8").decode("unicode_escape")
        _fb1 = get.split('["DTSGInitialData",[],{"token":"')[1].split('"')[0]
        _idfb = cookie.split('c_user=')[1].split(';')[0]
        return [_fb1, _idfb, _name]
    except:
        return False

def countdown(value):
    while value > 0.30:
        value -= 0.05
        print(f'KEDO[{BLUE}{str(value)[0:5]}{RESET}]','\r                      ',end = ' ')

        sleep(0.05)
    print('\r                                   ','\n')

def get_user_info(token):
    res = requests.get(f"https://traodoisub.com/api/?fields=profile&access_token={token}").json()
    if "success" in res:
        data = res['data']
        username = data['user']
        xu = data['xu']
        xudie = data['xudie']
        print(f"🔹 Tài Khoản: {username} | 💰 Xu hiện tại: {xu} | ⚠️ Xu die: {xudie}") 
        return True
    else:
        print("❌ Lỗi: ", res['error'])
        return False

def set_nick(token, id_fb):
    res = requests.get(f"https://traodoisub.com/api/?fields=run&id={id_fb}&access_token={token}").json()
    if "success" in res:
        data = res['data']
        id_fb = data['id']
        msg = data['msg']
        print(f"✅ {msg} ({id_fb})")
        return True
    else:
        print(f"❌ Cấu hình thất bại cho ID {id_fb}!")
        return False

def get_quests(token):
    """Lấy nhiệm vụ like bài viết Facebook"""
    url = f"https://traodoisub.com/api/?fields=facebook_reaction&access_token={token}&type=LIKE"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"❌ Lỗi: API trả về mã {response.status_code}")
        return []

    try:
        res = response.json()  # Chuyển đổi sang JSON
    except requests.exceptions.JSONDecodeError:
        print("❌ Lỗi: Không thể parse JSON từ API")
        print("Phản hồi từ server:", response.text)  # In ra nội dung phản hồi để debug
        return []

    try:
        if len(res['data']) > 0:
            list = []
            for i in res['data']:
                uid = i['id']
                code_job = i['code']
                try:
                    uid = uid.split('_')[1]
                except:
                    pass
                list.append([uid,code_job])
            return list
        else:
            print(f"❌ Không tìm thấy nhiệm vụ like Facebook")
            return []
    except:
        print(f"❌ Không tìm thấy nhiệm vụ like Facebook")
        return []

def claim_xu(token, id_job):
    """Nhận xu sau khi hoàn thành like"""
    url = f"https://traodoisub.com/api/coin/?type=facebook_reaction&id={id_job}&access_token={token}"
    res = requests.get(url).json()
    if "success" in res:
        xu = res['data']['xu']
        msg = res['data']['msg']
        # print(f"💰 {id_job} : {msg} (+{xu} xu)")
        return msg,xu
    else:
        print("❌ Nhận xu thất bại!")
        return 0

def _Like(cookie, uid, type, fb1, idfb):
    headers = {
        "accept": "*/*", 
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7", 
        "content-type": "application/x-www-form-urlencoded", 
        "sec-ch-prefers-color-scheme": "light", 
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"", 
        "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"", 
        "sec-ch-ua-mobile": "?0", 
        "sec-ch-ua-model": "\"\"", 
        "sec-ch-ua-platform": "\"Linux\"", 
        "sec-ch-ua-platform-version": "\"\"", 
        "sec-fetch-dest": "empty", 
        "sec-fetch-mode": "cors", 
        "sec-fetch-site": "same-origin", 
        "x-asbd-id": "129477", 
        "x-fb-friendly-name": "CometUFIFeedbackReactMutation", 
        "x-fb-lsd": "7_RkODA0fo-6ShZlbFpHEW"
    }
    _reac = {
        "LIKE": "1635855486666999",
        "LOVE": "1678524932434102",
        "CARE": "613557422527858",
        "HAHA": "115940658764963",
        "WOW": "478547315650144",
        "SAD": "908563459236466",
        "ANGRY": "444813342392137"
    }
    _id_reac = _reac.get(type)
    _data = {
        'av': idfb,
        '__usid': r'6-Tsfgotwhb2nus:Psfgosvgerpwk:0-Asfgotw11gc1if-RV=6:F=',
        '__aaid': '0',
        '__user': idfb,
        '__a': '1',
        '__req': '2c',
        '__hs': '19896.HYP:comet_pkg.2.1..2.1',
        'dpr': '1',
        '__ccg': 'EXCELLENT',
        '__rev': '1014402108',
        '__s': '5vdtpn:wbz2hc:8r67q5',
        '__hsi': '7383159623287270781',
        '__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C17xt3odE98K361twYwJyE24wJwpUe8hwaG1sw9u0LVEtwMw65xO2OU7m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewyDwkUe9obrwKxm5oe8464-5pUfEdK261eBx_wHwdG7FoarCwLyES0Io88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13whEeE4WVU-4EdrxG1fy8bUaU','__csr': 'gug_2A4A8gkqTf2Ih6RFnbk9mBqaBaTs8_tntineDdSyWqiGRYCiPi_SJuLCGcHBaiQXtLpXsyjIymm8oFJswG8CSGGLzAq8AiWZ6VGDgyQiiTBKU-8GczE9USmi4A9DBABHgWEK3K9y9prxaEa9KqQV8qUlxW22u4EnznDxSewLxq3W2K16BxiE5VqwbW1dz8qwCwjoeEvwaKVU6q0yo5a2i58aE7W0CE5O0fdw1jim0dNw7ewPBG0688025ew0bki0cow3c8C05Vo0aNF40BU0rmU3LDwaO06hU06RG6U1g82Bw0Gxw6Gw',
        '__comet_req': '15',
        'fb_dtsg': fb1,
        'jazoest': '25509',
        'lsd': '2JgeTE-rDuLtIVUViHpGjH',
        '__spin_r': '1014402108',
        '__spin_b': 'trunk',
        '__spin_t': '1719025807',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
        'variables': fr'{{"input":{{"attribution_id_v2":"CometHomeRoot.react,comet.home,tap_tabbar,1719027162723,322693,4748854339,,","feedback_id":"{_encode_to_base64("feedback:"+str(uid))}","feedback_reaction_id":"{_id_reac}","feedback_source":"NEWS_FEED","is_tracking_encrypted":true,"tracking":["AZWUDdylhKB7Q-Esd2HQq9i7j4CmKRfjJP03XBxVNfpztKO0WSnXmh5gtIcplhFxZdk33kQBTHSXLNH-zJaEXFlMxQOu_JG98LVXCvCqk1XLyQqGKuL_dCYK7qSwJmt89TDw1KPpL-BPxB9qLIil1D_4Thuoa4XMgovMVLAXncnXCsoQvAnchMg6ksQOIEX3CqRCqIIKd47O7F7PYR1TkMNbeeSccW83SEUmtuyO5Jc_wiY0ZrrPejfiJeLgtk3snxyTd-JXW1nvjBRjfbLySxmh69u-N_cuDwvqp7A1QwK5pgV49vJlHP63g4do1q6D6kQmTWtBY7iA-beU44knFS7aCLNiq1aGN9Hhg0QTIYJ9rXXEeHbUuAPSK419ieoaj4rb_4lA-Wdaz3oWiWwH0EIzGs0Zj3srHRqfR94oe4PbJ6gz5f64k0kQ2QRWReCO5kpQeiAd1f25oP9yiH_MbpTcfxMr-z83luvUWMF6K0-A-NXEuF5AiCLkWDapNyRwpuGMs8FIdUJmPXF9TGe3wslF5sZRVTKAWRdFMVAsUn-lFT8tVAZVvd4UtScTnmxc1YOArpHD-_Lzt7NDdbuPQWQohqkGVlQVLMoJNZnF_oRLL8je6-ra17lJ8inQPICnw7GP-ne_3A03eT4zA6YsxCC3eIhQK-xyodjfm1j0cMvydXhB89fjTcuz0Uoy0oPyfstl7Sm-AUoGugNch3Mz2jQAXo0E_FX4mbkMYX2WUBW2XSNxssYZYaRXC4FUIrQoVhAJbxU6lomRQIPY8aCS0Ge9iUk8nHq4YZzJgmB7VnFRUd8Oe1sSSiIUWpMNVBONuCIT9Wjipt1lxWEs4KjlHk-SRaEZc_eX4mLwS0RcycI8eXg6kzw2WOlPvGDWalTaMryy6QdJLjoqwidHO21JSbAWPqrBzQAEcoSau_UHC6soSO9UgcBQqdAKBfJbdMhBkmxSwVoxJR_puqsTfuCT6Aa_gFixolGrbgxx5h2-XAARx4SbGplK5kWMw27FpMvgpctU248HpEQ7zGJRTJylE84EWcVHMlVm0pGZb8tlrZSQQme6zxPWbzoQv3xY8CsH4UDu1gBhmWe_wL6KwZJxj3wRrlle54cqhzStoGL5JQwMGaxdwITRusdKgmwwEQJxxH63GvPwqL9oRMvIaHyGfKegOVyG2HMyxmiQmtb5EtaFd6n3JjMCBF74Kcn33TJhQ1yjHoltdO_tKqnj0nPVgRGfN-kdJA7G6HZFvz6j82WfKmzi1lgpUcoZ5T8Fwpx-yyBHV0J4sGF0qR4uBYNcTGkFtbD0tZnUxfy_POfmf8E3phVJrS__XIvnlB5c6yvyGGdYvafQkszlRrTAzDu9pH6TZo1K3Jc1a-wfPWZJ3uBJ_cku-YeTj8piEmR-cMeyWTJR7InVB2IFZx2AoyElAFbMuPVZVp64RgC3ugiyC1nY7HycH2T3POGARB6wP4RFXybScGN4OGwM8e3W2p-Za1BTR09lHRlzeukops0DSBUkhr9GrgMZaw7eAsztGlIXZ_4"],"session_id":"{uuid.uuid4()}","actor_id":"{idfb}","client_mutation_id":"3"}},"useDefaultActor":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false}}',
        'server_timestamps': 'true',
        'doc_id': '7047198228715224',
    }
    cookies = {
        "cookie": cookie
    }
    _get = requests.post("https://www.facebook.com/api/graphql/",headers=headers, cookies=cookies, params=_data)
    if '{"data":{"feedback_react":{"feedback":{"id":' in _get.text:
        return True
    else:
        return False

def nhap_token():
    return input("🔑 Nhập Token TraoDoiSub: ")

def nhap_cookie():
    cookie = input("🍪 Nhập Cookie Facebook: ")
    
    # Gửi request để lấy thông tin user
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "cookie": cookie
    }
    
    url = "https://www.facebook.com/api/graphql/"
    
    try:
        response = requests.get(url, headers=headers)
        
        if "c_user=" in cookie:
            uid = re.search(r"c_user=(\d+)", cookie).group(1)  # Lấy UID từ cookie
            print(f"✅ Đăng nhập thành công! UID: {uid}")
            return cookie, uid
        else:
            print("❌ Đăng nhập thất bại! Cookie không hợp lệ.")
            return None, None
    except Exception as e:
        print("❌ Lỗi khi kiểm tra cookie:", str(e))
        return None, None

def main():
    # Nhập token và khởi tạo API
    token = nhap_token()

    # Kiểm tra tài khoản
    if not get_user_info(token):
        print("❌ Token không hợp lệ, thoát!")
        return

    # Nhập cookie & ID Facebook
    cookie, idfb = nhap_cookie()
    
    # Đặt nick chạy
    if not set_nick(token, idfb):
        print("❌ Không thể đặt nick chạy! Kiểm tra lại UID hoặc Token.")
        return

    print("\n🔄 Bắt đầu auto like Facebook...\n")
    _info = _Infofb(cookie)
    print('info: ',_info)
    while True:
        # Lấy danh sách nhiệm vụ like Facebook
        jobs = get_quests(token)
        if jobs == []:
            print("⏳ Không có nhiệm vụ nào, đợi 10s...")
            countdown(17)
            continue

        for job_id,code_job in jobs:
            print(f"👉 Đang thực hiện like bài viết {job_id}...",time.sleep(0.5),'\r                                      ',end = ' ')

            reactions = ["LIKE", "LOVE", "CARE", "HAHA", "WOW", "SAD", "ANGRY"]
            # reaction_type = random.choice(reactions)  # Chọn ngẫu nhiên 1 kiểu cảm xúc
            reaction_type = 'LIKE'
            if _Like(cookie, job_id, reaction_type, _info[0], _info[1]):
               print(f"✅ {reaction_type} thành công! Nhận xu...",time.sleep(0.5),'\r                                                 ',end = ' ')
               msg,xu = claim_xu(token, code_job)
               print(f"💰 {GREEN}Nhận được {msg}!|{BLUE}Bạn có {xu}xu")
            else:
               print("❌ Like thất bại!")

            countdown(35)  # Delay tránh spam

        # print("\n🔄 Tiếp tục vòng lặp sau 35s...\n")
        countdown(37)

if __name__ == "__main__":
    main()
