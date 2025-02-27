import requests, base64, uuid, os, json
from random import randint
from datetime import datetime
import re
import time 
from time import sleep
import random
import sys
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pathlib import Path
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import platform
import os
import shutil
from colorama import Fore, Style, init
import requests, base64, uuid, os, json
from random import randint
from datetime import datetime
import re
import time 
from time import sleep
import random
import sys
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pathlib import Path
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import platform
import os
import shutil
from colorama import Fore, Style, init
init(autoreset=True)
RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
BLUE = Fore.BLUE
RESET = Style.RESET_ALL
MAGENTA = Fore.MAGENTA
current_dir = Path(__file__).parent
from time import sleep
import os
import platform
from pathlib import Path
# Xác định đường dẫn của thư mục Profile
if os.name == 'nt':  # Windows
    base_profile_path = Path(os.environ['USERPROFILE']) / "Profile"
elif os.name == 'posix' and platform.system() == 'Darwin':  # macOS
    base_profile_path = Path.home() / "Profile"
else:  # Linux hoặc hệ thống khác
    base_profile_path = Path.cwd() / "Profile"  # Thay vì `current_dir`, dùng `Path.cwd()`

# Tạo thư mục nếu chưa tồn tại
try:
    base_profile_path.mkdir(parents=True, exist_ok=True)
    print(f"Đã tạo thư mục: {base_profile_path}")
except Exception as e:
    print(f"Lỗi khi tạo thư mục: {e}")

# Lấy tên hệ điều hành
os_name = platform.system()
print(f"Hệ điều hành: {os_name}")
def slow_typing_with_actionchains(driver, element, text):
    delay = random.uniform(0.2, 0.5)
    for char in text:
        element.send_keys(char)
        sleep(delay)

success_count = 0
profile_path = None
profile = None
textcomment = None
passwords = None
gioihan = 5000
bill = 0
    
def getjob(token, nv):
    headers = {
        'Content-Type':'application/json'
    }
    # if nv == 'LIKE':
    #     nv = 'facebook_reaction'
    # else:
    #     nv = 'facebook_reactioncmt'

    url_get_nv = f"https://traodoisub.com/api/?fields=facebook_reaction&access_token={token}&type=LIKE"
    get = requests.get(url_get_nv,headers=headers)
    return get

def decode_base64(encoded_str):
	decoded_bytes = base64.b64decode(encoded_str)
	decoded_str = decoded_bytes.decode('utf-8')
	return decoded_str

def _encode_to_base64(_data):
	byte_representation = _data.encode('utf-8')
	base64_bytes = base64.b64encode(byte_representation)
	base64_string = base64_bytes.decode('utf-8')
	return base64_string
def countdown(value):
	while not(value <= 1) :
		value -= 0.123
		print(f'''    KEDO[{BLUE}{str(value)[0:5]}{RESET}]''', '               ', end = '\r')
		sleep(0.02)
		print(f'''    KEDO[{BLUE}{str(value)[0:5]}{RESET}]''', '               ', end = '\r')
		sleep(0.02)
		print(f'''    KEDO[{BLUE}{str(value)[0:5]}{RESET}]''', '               ', end = '\r')
		sleep(0.02)
		print(f'''    KEDO[{BLUE}{str(value)[0:5]}{RESET}]''', '               ', end = '\r')
		sleep(0.02)
		print(f'''    KEDO[{BLUE}{str(value)[0:5]}{RESET}]''', '               ', end = '\r')
		sleep(0.02)
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

def CMT(cookie, id, idfb, fb1, msg:str):
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
    _data = {
        'av': idfb,
        '__aaid': '0',
        '__user': idfb,
        '__a': '1',
        '__req': '3a',
        '__hs': '19892.HYP:comet_pkg.2.1..2.1',
        'dpr': '1',
        '__ccg': 'GOOD',
        '__rev': '1014295603',
        '__s': 'xrpwhz:69a31q:w9xo5s',
        '__hsi': '7381711750373683802',
        '__dyn': '7AzHK4HwkEng5K8G6EjBAg2owIxu13wFwhUngS3q2ibwNw9G2Saw8i2S1DwUx60GE5O0BU2_CxS320om78c87m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwwwi831wiE567Udo5qfK0zEkxe2GewDG1jwUBwJK2W5olwUwgojUlDw-wUwxwjFovUaU3VBwFKq2-azo2NwwwOg2cwMwhEkxebwHwNxe6Uak0zU8oC1hxB0qo4e16wWwjHDzUiwRK6E4-8wLwHw','__csr': 'gaRMHkaEj4EQgznFON5ifOjsLJA9idO8LqsAHJXeIX48l9lRN4kDmyTAvcKSIAGQtljy9kV4DlGaBAnWUCiqqWmWKA6pBBUymnHBArrCDDKaGaggAQubV8V34iVUCiicoC32Ujm8Ki8H-6UJ1h2KlAyECdg4237CxmQ6F89onXAwjEe8uwxxu5ES2G1qxy3K0xonx21ewnEb8eU2yG2q0hm1yw8G7o7G7oaodU1381T84m0auwdy0dDwb201Z4w2Fo036dg0gYCw2BA0wU7e04WU0qQwlodE04Dq01zOw4Bw51w7hxK',
        '__comet_req': '15',
        'fb_dtsg': fb1,
        'jazoest': '25686',
        'lsd': 'H5eT-P3p1zI2ywmbuNcbRm',
        '__spin_r': '1014295603',
        '__spin_b': 'trunk',
        '__spin_t': '1718688698',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'useCometUFICreateCommentMutation',
        'variables': fr'{{"feedLocation":"DEDICATED_COMMENTING_SURFACE","feedbackSource":110,"groupID":null,"input":{{"client_mutation_id":"4","actor_id":"{idfb}","attachments":null,"feedback_id":"{_encode_to_base64(f"feedback:{id}")}","formatting_style":null,"message":{{"ranges":[],"text":"{msg}"}},"attribution_id_v2":"CometHomeRoot.react,comet.home,via_cold_start,1718688700413,194880,4748854339,,","vod_video_timestamp":null,"feedback_referrer":"/","is_tracking_encrypted":true,"tracking":["AZX1ZR3ETYfGknoE2E83CrSh9sg_1G8pbUK70jA-zjEIcfgLxA-C9xuQsGJ1l2Annds9fRCrLlpGUn0MG7aEbkcJS2ci6DaBTSLMtA78T9zR5Ys8RFc5kMcx42G_ikh8Fn-HLo3Qd-HI9oqVmVaqVzSasZBTgBDojRh-0Xs_FulJRLcrI_TQcp1nSSKzSdTqJjMN8GXcT8h0gTnYnUcDs7bsMAGbyuDJdelgAlQw33iNoeyqlsnBq7hDb7Xev6cASboFzU63nUxSs2gPkibXc5a9kXmjqZQuyqDYLfjG9eMcjwPo6U9i9LhNKoZwlyuQA7-8ej9sRmbiXBfLYXtoHp6IqQktunSF92SdR53K-3wQJ7PoBGLThsd_qqTlCYnRWEoVJeYZ9fyznzz4mT6uD2Mbyc8Vp_v_jbbPWk0liI0EIm3dZSk4g3ik_SVzKuOE3dS64yJegVOQXlX7dKMDDJc7P5Be6abulUVqLoSZ-cUCcb7UKGRa5MAvF65gz-XTkwXW5XuhaqwK5ILPhzwKwcj3h-Ndyc0URU_FJMzzxaJ9SDaOa9vL9dKUviP7S0nnig0sPLa5KQgx81BnxbiQsAbmAQMr2cxYoNOXFMmjB_v-amsNBV6KkES74gA7LI0bo56DPEA9smlngWdtnvOgaqlsaSLPcRsS0FKO3qHAYNRBwWvMJpJX8SppIR1KiqmVKgeQavEMM6XMElJc9PDxHNZDfJkKZaYTJT8_qFIuFJVqX6J9DFnqXXVaFH4Wclq8IKZ01mayFbAFbfJarH28k_qLIxS8hOgq9VKNW5LW7XuIaMZ1Z17XlqZ96HT9TtCAcze9kBS9kMJewNCl-WYFvPCTCnwzQZ-HRVOM04vrQOgSPud7vlA3OqD4YY2PSz_ioWSbk98vbJ4c7WVHiFYwQsgQFvMzwES20hKPDrREYks5fAPVrHLuDK1doffY1hPTWF2KkSt0uERAcZIibeD5058uKSonW1fPurOnsTpAg8TfALFu1QlkcNt1X4dOoGpYmBR7HGIONwQwv5-peC8F758ujTTWWowBqXzJlA2boriCvdZkvS15rEnUN57lyO8gINQ5heiMCQN8NbHMmrY_ihJD3bdM4s2TGnWH4HBC2hi0jaIOJ8AoCXHQMaMdrGE1st7Y3R_T6Obg6VnabLn8Q-zZfToKdkiyaR9zqsVB8VsMrAtEz0yiGpaOF3KdI2sxvii3Q5XWIYN6gyDXsXVykFS25PsjPmXCF8V1mS7x6e9N9PtNTWwT8IGBZp9frOTQN2O52dOhPdsuCHAf0srrBVHbyYfCMYbOqYEEXQG0pNAmG_wqbTxNew9kTsXDRzYKW-NmEJcvy_xh1dDwg8xJc58Cl71e-rau3iP7o8mWhVSaxi4Bi6LAuj4UKVCt3IYCfm9AR1d5LqBFWU9LrJbRZSMlmUYwZf7PlrKmpnCnZvuismiL7DH3cnUjP0lWAvhy3gxZm1MK8KyRzWmHnTNqaVlL37c2xoE4YSyponeOu5D-lRl_Dp_C2PyR1kG6G0TCWS66UbU89Fu1qmwWjeQwYhzj2Jly9LRyClAbe86VJhIZE18YLPB-n1ng78qz7hHtQ8qT4ejY4csEjSRjjnHdz8U-06qErY-CXNNsVtzpYGuzZ1ZaXqzAQkUcREm98KR8c1vaXaQXumtDklMVgs76gLqZyiG1eCRbOQ6_EcQv7GeFnq5UIqoMH_Xzc78otBTvC5j3aCs5Pvf6k3gQ5ZU7E4uFVhZA7xoyD8sPX6rhdGL8JmLKJSGZQM5ccWpfpDJ5RWJp0bIJdnAJQ8gsYMRAI2OBxx2m2c76lNiUnB750dMe2H3pFzFQVkWQLkmGVY37cgmRNHyXboDMQ1U2nlbNH017dmklJCk4jVU8aA9Gpo8oHw","{{\"assistant_caller\":\"comet_above_composer\",\"conversation_guide_session_id\":\"{uuid.uuid4()}\",\"conversation_guide_shown\":null}}"],"feedback_source":"DEDICATED_COMMENTING_SURFACE","idempotence_token":"client:{uuid.uuid4()}","session_id":"{uuid.uuid4()}"}},"inviteShortLinkKey":null,"renderLocation":null,"scale":1,"useDefaultActor":false,"focusCommentID":null}}',
        'server_timestamps': 'true',
        'doc_id': '7994085080671282',
    }
    cookies = {
        "cookie": cookie
    }
    try:
        _get = requests.post("https://www.facebook.com/api/graphql/",headers=headers, cookies=cookies, params=_data)
        if '"errors"' not in _get.text:
            return True
        else:
            return False
    except:
        return False
def _Bypass(cookie, idfb, fb1):
    headers = {
        "accept": "*/*", 
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7", 
        "content-type": "application/x-www-form-urlencoded", 
        "sec-ch-prefers-color-scheme": "light", 
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"", 
        "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"", 
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-model": "\"\"", 
        "sec-ch-ua-platform": "\"Linux\"", 
        "sec-ch-ua-platform-version": "\"\"", 
        "sec-fetch-dest": "empty", 
        "sec-fetch-mode": "cors", 
        "sec-fetch-site": "same-origin", 
        "x-asbd-id": "129477", 
        "x-fb-friendly-name": "CometUserFollowMutation", 
        "x-fb-lsd": "7_RkODA0fo-6ShZlbFpHEW"
    }
    data = {
        "av": idfb,
        "__user": idfb,
        "__a": "1",
        "__req": "8",
        "__hs": "20038.HYP:comet_pkg.2.1..2.1",
        "dpr": "1",
        "__ccg": "EXCELLENT",
        "__rev": "1018089718",
        "__s": "mtrukx:3ui1ys:yphvdu",
        "__hsi": "7435940161710523784",
        "__dyn": "7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo19oe8hw2nVE4W099w8G1Dz81s8hwnU2lwv89k2C1Fwc60D8vwRwlE-U2zxe2GewbS361qw8Xwn82Lx-0lK3qazo720Bo2ZwrU6C0hq1Iwqo35wvodo7u2-2K0UE",
        "__csr": "gzl5849ahWFaeU-rK4Uyii9VAmWl6zpUCUgK3K2mi2q2Ki687W08Pyo1yp9Esw14e0OE1u80now05XXw0Dhw0eNi",
        "__comet_req": "15",
        "fb_dtsg": fb1,
        "jazoest": "25487",
        "lsd": "PEkEdpWB34ZUqD6iqvcwMP",
        "__spin_r": "1018089718",
        "__spin_b": "trunk",
        "__spin_t": "1731314734",
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "FBScrapingWarningMutation",
        "variables": "{}",
        "server_timestamps": "true",
        "doc_id": "6339492849481770"
    }
    cookies = {
        "cookie": cookie
    }
    bypass = requests.post('https://www.facebook.com/api/graphql/',headers=headers, cookies=cookies, params=data)
    return bypass.text

#define hệ thống
def lay_data():
    base_profile_path = os.getcwd()+'\\profiles'
    profiles = [f for f in os.listdir(base_profile_path) if os.path.isdir(os.path.join(base_profile_path, f))]
    profiles.sort()
    
    if not profiles:
        return [], {}
    
    passwords = {}
    for profile in profiles:
        
        info_file_path = os.path.join(base_profile_path, profile, 'acc.txt')
        if os.path.exists(info_file_path):
            with open(info_file_path, 'r') as info_file:
                profiles , passwords = info_file.read().split()

    
    def get_element_color(driver, xpath):
        element = driver.find_element(By.XPATH, xpath)
        color = element.value_of_css_property('color')
        return color
    return [f"{profiles}"], passwords
def quan_li(profile, passwords):
    global driver, ck
    profile_path = os.path.join(base_profile_path, profile)
    options = Options()
    options.add_argument(f"--user-data-dir={profile_path}")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-cache")
    options.add_argument("--disable-extensions")
    options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://traodoisub.com")
    sleep(2)
    try:
        user_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="username"]'))
        )
        # user_input.send_keys(accound_tds)
        slow_typing_with_actionchains(driver, user_input, profile)

        # Nhập mật khẩu
        pass_input = driver.find_element(By.XPATH, '//input[@id="password"]')
        # pass_input.send_keys(password_tds)
        slow_typing_with_actionchains(driver, pass_input, passwords)

        # Nhấn nút đăng nhập
        login_submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_submit.click()
        
    except:
        sleep(0.1)
    sleep(3)
    driver.get('https://traodoisub.com/view/setting/')
    sleep(2)
    value_values = driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div[2]/div[1]/div[1]/div[2]/form/div[3]/input')

    tk = value_values.get_attribute("value")
    driver.execute_script("window.open('https://m.facebook.com', '_blank');")
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    sleep(10)
    cookies = driver.get_cookies()
    ck = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
    return driver
def thuc_thi(profile, passwords):
    global tk,driver
    profile_path = os.path.join(base_profile_path, profile[0])
    options = Options()
    options.add_argument(f"--user-data-dir={profile_path}")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-cache")
    options.add_argument('--headless')
    options.add_argument("--disable-extensions")
    options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://traodoisub.com")
    sleep(3)
    try:
        user_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="username"]'))
        )
        # user_input.send_keys(accound_tds)
        slow_typing_with_actionchains(driver, user_input, profile)

        # Nhập mật khẩu
        pass_input = driver.find_element(By.XPATH, '//input[@id="password"]')
        # pass_input.send_keys(password_tds)
        slow_typing_with_actionchains(driver, pass_input, passwords)

        # Nhấn nút đăng nhập
        login_submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_submit.click()
        
    except:
        sleep(0.1)
    sleep(3)
    driver.get('https://traodoisub.com/view/setting/')
    sleep(2)
    value_values = driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div[2]/div[1]/div[1]/div[2]/form/div[3]/input')

    tk = value_values.get_attribute("value")
    driver.execute_script("window.open('https://m.facebook.com', '_blank');")
    sleep(5)
    handles = driver.window_handles
    
    driver.switch_to.window(handles[0])
    driver.close()
    driver.switch_to.window(handles[1])
    sleep(3)
    print(f"ĐANG {RED}Xác Thực Tài Khoản{RESET}")
    sleep(3)
    print(f"ĐANG {RED}Chuẩn Bị Thuật Toán Chống Block{RESET}")
    sleep(3)
    print(f" {GREEN} CHUẨN BỊ THÀNH CÔNG{RESET}")
    cookies = driver.get_cookies()
    ck = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
    # driver.close()
    driver.quit()
    return tk,ck


def tao_profile():
    while True:
        accound_tds = input("\nNhập 'TÊN ĐĂNG NHẬP TRAO ĐỔI SUB' của bạn: ").strip()
        password_tds = input("Nhập 'MẬT KHẨU TRAO ĐỔI SUB' của bạn: ").strip()
        
        # Cấu hình Chrome
        options = Options()
        # options.add_argument("--headless")  # Chạy ẩn nếu không muốn mở trình duyệt
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
        try:
            # print("Đang mở trang đăng nhập...")
            # driver.get("https://traodoisub.com")
            # sleep(2)
            # # Nhập tên đăng nhập
            # user_input = WebDriverWait(driver, 5).until(
            #     EC.presence_of_element_located((By.XPATH, '//input[@id="username"]'))
            # )
            # # user_input.send_keys(accound_tds)
            # slow_typing_with_actionchains(driver, user_input, accound_tds)

            # # Nhập mật khẩu
            # pass_input = driver.find_element(By.XPATH, '//input[@id="password"]')
            # # pass_input.send_keys(password_tds)
            # slow_typing_with_actionchains(driver, pass_input, password_tds)

            # # Nhấn nút đăng nhập
            # login_submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
            # login_submit.click()
            # print("Đã gửi thông tin đăng nhập.")

            # # Chờ trang chuyển hướng sau khi đăng nhập
            # # WebDriverWait(driver, 5).until(
            # #     EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Đăng xuất")]'))
            # # )
            # print("Đăng nhập thành công!")

            # Tạo profile nếu đăng nhập thành công
            base_profile_path = "profiles"
            profile_path = os.path.join(base_profile_path, accound_tds)

            if not os.path.exists(profile_path):
                os.makedirs(profile_path)

            info_file_path = os.path.join(profile_path, 'acc.txt')
            with open(info_file_path, 'w') as info_file:
                info_file.write(f"{accound_tds} {password_tds}")
            
            print(f"Đã tạo profile cho tài khoản: {accound_tds}")
            driver.quit()
            khuyen_cao()
            driver = quan_li(accound_tds, password_tds)
            input("Nhấn Enter để đóng trình duyệt...")
            break
        except Exception as e:
            print("Lỗi đăng nhập:", e)
            print("Vui lòng kiểm tra lại tài khoản hoặc thử lại sau.")
            sleep(3)
        finally:
            driver.quit()
def clean(folder_path):
    global profiles, passwords
    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        else:
            print(f"Thư mục không tồn tại: {folder_path}")
    except Exception as e:
        print(f"Không thể xóa {folder_path}: {e}")
    # profiles, passwords = lay_data()
def clean_all(profiles):
    
    for profile in profiles:
        profile_path = os.path.join(base_profile_path, profile)
        clean(profile_path)
    print(f"Đã {GREEN}xóa toàn bộ dữ liệu{RESET} trong tất cả cấu hình.")
    profiles = lay_data()
    if not profiles:
        print(f"{RED}Không có Tài Khoản nào trong hệ thống!{RESET}")
        input("Nhấn Enter để tạo mới...")
        tao_profile()

    
# define chức năng
def facebok_all(profiles, passwords):
    drivers = []
    for profile in profiles:
        driver = quan_li(profile, passwords[profile])
        drivers.append(driver)
    khuyen_cao()
    input(f"Nhấn {RED}Enter{RESET} để đóng tất cả các trình duyệt đã mở...")
    for driver in drivers:
        driver.quit()
    print("Đã đóng tất cả các trình duyệt.")
def facebook():
    while True:
        print(f"\n" + "="*40)  # Đúng mức thụt dòng
        print(f"\n=== {BLUE}KEDO TOOL{RESET} ===")  # Đúng mức thụt dòng
        print(f"----------copyright: Mle × Quý")

        for i, profile in enumerate(profiles):
            print(f"[{i}] {RED}{profile}{RESET}")

        choice = input(f"Chọn {GREEN}CẤU HÌNH{RESET} để sử dụng ( X để quay lại): ").strip().upper()
        
        if choice.isdigit() and 0 <= int(choice) < len(profiles):
            quan_li(profiles[int(choice)], passwords[profiles[int(choice)]])
            khuyen_cao()
            input(f"Nhấn Enter để đóng trình duyệt...")
            driver.quit()
            break
        elif choice == "X":
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")
# def lay_token():
#     options = Options()
#     options.add_argument("--headless")  # Chạy ẩn nếu không muốn mở trình duyệt
#     options.add_argument("--disable-gpu")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     driver.get("https://traodoisub.com")
#     sleep(2)
#     print("đang lấy token của bạn")
#     sleep(2)
#     # Nhập tên đăng nhập
#     user_input = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.XPATH, '//input[@id="username"]'))
#     )
#     # user_input.send_keys(accound_tds)
#     slow_typing_with_actionchains(driver, user_input, accound_tds)

#     # Nhập mật khẩu
#     pass_input = driver.find_element(By.XPATH, '//input[@id="password"]')
#     # pass_input.send_keys(password_tds)
#     slow_typing_with_actionchains(driver, pass_input, password_tds)

#     # Nhấn nút đăng nhập
#     login_submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
#     login_submit.click()
#     time.slep

'''def _like_p():
    time.sleep(5)

    like_xpaths = [
        '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[3]/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]',
        '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]',
        '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[3]/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]',
        '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[3]/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div[2]'

    ]

    for xpath in like_xpaths:
        try:
            bt_like= driver.find_element(By.XPATH, xpath)
            bt_like.click()
            time.sleep(0.05)
            return True
        except Exception as e:
            continue
    return False
    #     return False
    # if lk() == True:
    #     return True
'''

def tds(profile=None):

    while profile is None:
        print(f"\n" + "="*40)
        print(f"\n=== {BLUE}KEDO TOOL{RESET} ===")
        print(f"----------copyright: Mle × Quý")
        print(f'[{GREEN}1{RESET}] - LIKE {RED}ANTI BLOCK{RESET}\n[{GREEN}2{RESET}] - COMMENT {RED}ANTI BLOCK{RESET}\n')
        chonjob = input(f"Chọn {GREEN}Hoạt Động Cấu Hình{RESET} để sử dụng ( X để quay lại)").strip().upper()
        if chonjob == "X":
            return
        elif chonjob != "1" or chonjob != "2":
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")
        print(f"\n" + "="*40)
        print(f"\n=== {BLUE}KEDO TOOL{RESET} ===")
        print(f"----------copyright: Mle × Quý")
        for i, profile in enumerate(profiles):
            print(f"[{i}] {RED}{profile}{RESET}")
        choice = input(f"Chọn {GREEN}CẤU HÌNH{RESET} để sử dụng ( X để quay lại): ").strip().upper()
        if choice.isdigit() and 0 <= int(choice) < len(profiles):
            profile = profiles[int(choice)]
        elif choice == "X":
            return
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")
    
    tk,ck = thuc_thi(profiles, passwords)
    # print(ck)
    # sys.exit()
    success_count = 0
    while True:
        login = requests.get(f'https://traodoisub.com/api/?fields=profile&access_token={tk}')
        if login.json()['success'] == 200:
            
            user = login.json()['data']['user']
            xu = login.json()['data']['xu']
            xu = int(xu)
            break
        else:
            continue
    _info = _Infofb(ck)
    if _info == False:
        print(' Facebook Die !!!')
    else:
        print(f'UID FACEBOOK: {GREEN}{_info[1]}{RESET} | NAME FACEBOOK: {BLUE}{_info[2]}{RESET}')
    print(f"CẤU HÌNH: {RED}{user}{RESET} | SỐ DƯ: {YELLOW}{xu}{RESET} |  ")
    while True:
            listck = ck
            loilike, loicmt = 0, 0, 
            _info = _Infofb(ck)
            if _info != False:
                uidfb = _info[1]
                tenfb = _info[2]
            else:
                uidfb = ck.split('c_user=')[1].split(';')[0]
                print(f'Cookie Tài Khoản {uidfb} Die', end='\r');sleep(3); print('                                     ', end = '\r' )
                listck.remove(ck)
                continue
            # headers = {
            #     'Host': 'traodoisub.com',
            #     'accept':'*/*',
            #     'origin':'https://traodoisub.com',
            #     'x-requested-with':'XMLHttpRequest',
            #     'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
            #     'referer':'https://traodoisub.com/view/cauhinh/',
            #     "cookie": cookie
            # }
            # data = {
            #     'iddat[]': uidfb,
            #     'loai': 'fb'
            # }
            # cauhinh = requests.post('https://traodoisub.com/view/cauhinh/',headers=headers, data=data, timeout=5).text
            # if '1' in cauhinh:
            khuyen_cao()
            # else:
            #     print(f"  Cấu Hình {RED}Thất Bại{RESET} UID FB: {uidfb} | Tên FB: {tenfb}")
            #     continue
            if chonjob == "1":
                while True:
                    listlike = getjob(tk, 'LIKE')
                    like1 = listlike.text
                    like2 = listlike.json()
                    if (like1 == [] and like2 == []) or (len(str(like1)) == 0):
                        print(f'{RED}Hết Nhiệm Vụ{GREEN}-sau 10s sẽ load lại', end = '\r');sleep(10); print('                                                     ', end = '\r')
                    elif 'error' in like2:
                        print(f'{RED}ĐANG{RESET} Lấy Nhiệm Vụ                          ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                        countdown(20)
                    else:
                        print(f'{GREEN}Tìm Thấy{RESET} {len(like2['data'])} Nhiệm Vụ                      ', end = '\r')
                        for x in like2['data']:
                            try:
                                uid = x['id'].split('_')[1]
                                code_job = x['code']
                            except Exception as e:
                                uid = x['id']
                            # like = _Like(ck, uid, "LIKE", _info[0], _info[1])
                            # print(uid)
                            headers = {
                            "authority": "mbasic.facebook.com",
                            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                            "content-type": "application/x-www-form-urlencoded",
                            #"sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                            "sec-ch-ua-mobile": "?0",
                            'sec-ch-ua-platform': '"Windows"',
                            "sec-fetch-dest": "document",
                            "sec-fetch-mode": "navigate",
                            "sec-fetch-site": "none",
                            "sec-fetch-user": "?1",
                            "upgrade-insecure-requests": "1",
                            "accept-language": "vi",
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                            "cookie": ck
                            }
                            like_p = _Like(ck, uid, "LIKE", _info[0], _info[1])
                            if like_p == False:
                                print(f" FAIL LIKE : {uid}             ", end = '\r'); sleep(2); print('                                                       ', end = '\r')
                                _Bypass(ck, _info[1], _info[0])
                                loilike += 1
                                countdown(5)
                            else:
                                countdown(2)
                                url_nhan_xu = f"https://traodoisub.com/api/coin/?type=facebook_reaction&id={code_job}&access_token={tk}"
                                url_nhan_xu = requests.get(url_nhan_xu).json()
                                success_count += 1
                                time = datetime.now().strftime("%H:%M:%S")
                                try:
                                    if url_nhan_xu["success"] == 200:
                                        tien_job = url_nhan_xu['data']['msg']
                                        print(f"[{success_count}]{RED}{time}{RESET}|Kedo SĂN{YELLOW}|{tien_job}|{RESET}SỐ DƯ: {YELLOW}{xu}{RESET}|")
                                        msg = url_nhan_xu['data']['msg']
                                        so_xu = int(msg.split()[0])
                                        xu+=so_xu
                                        sleep(2)
                                except:
                                    print(url_nhan_xu['error'])
                                    continue
                                countdown(10)
                                    
            elif chonjob == "2":
                while True:
                    cmtcheo = getjob(tk, 'comment')
                    like1 = cmtcheo.text
                    like2 = cmtcheo.json()
                    if like1 == []:
                        print(f'Hết Nhiệm Vụ              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                    elif 'error' in like2:
                        print(f'{RED}ĐANG{RESET} Lấy Nhiệm Vụ                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                        countdown(20)
                    else:
                        print(f'{GREEN}Tìm Thấy{RESET} {len(like2)} Nhiệm Vụ                      ', end = '\r')
                        for x in like2:
                            try:
                                idpost = x['idpost']
                                link = x['link']
                                ndcmt = json.loads(x["nd"])[0]
                            except:
                                countdown(6)
                            getuid = requests.post('https://id.traodoisub.com/api.php',data={'link': link}, timeout=None).json()
                            if 'success' in getuid:
                                uid = getuid['id']
                            else:
                                print(f'link bài viết die', end = '\r'); sleep(2); print('                                                       ', end = '\r')
                                countdown(3)
                            like = CMT(ck, uid, _info[1], _info[0], ndcmt)
                            if like == False:
                                print(f"FAIL CMT:{uid}             ", end = '\r'); sleep(2); print('                                                       ', end = '\r')
                                _Bypass(ck, _info[1], _info[0])
                                loicmt += 1
                                countdown(3)
                            else:
                                headers = {
                                    "Host":"traodoisub.com",
                                    "x-requested-with":"XMLHttpRequest",
                                    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
                                    "origin":"https://traodoisub.com",
                                    "cookie": cookie
                                }
                                data = {
                                    'id': idpost
                                }
                                nhan = requests.post('https://traodoisub.com/ex/comment/nhantien.php',headers=headers, data=data).json()
                                if 'mess' in nhan:
                                    headers = {
                                        "Host": "traodoisub.com",
                                        "x-requested-with": "XMLHttpRequest",
                                        "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
                                        "cookie": cookie
                                    }
                                    get = requests.get('https://traodoisub.com/home/',headers=headers).text
                                    xu = get.split('"soduchinh">')[1].split('<')[0]
                                    success_count+=1
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(f"[{success_count}]{RED}{time}{RESET}|Kedo SĂN{YELLOW}|>1400<|{RESET}SỐ DƯ: {YELLOW}{xu}{RESET}|")
                                    try: 
                                        handles = driver.window_handles
                                        driver.switch_to.window(handles[0])
                                        driver.execute_script("window.open('https://www.facebook.com/profile.php?id=', '_blank');")
                                        handles = driver.window_handles
                                        driver.switch_to.window(handles[1])  
                                        #ba chấm
                                        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div'))).click() 
                                        #nhật kí hoạt động
                                        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/div/a[5]'))).click()
                                        #bình luận
                                        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[6]/div[1]/div/div[1]/div[2]/div[1]/div/div/div/span'))).click()
                                        #gỡ
                                        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[4]/div[2]/div[2]/div[2]/div[2]'))).click()
                                        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div'))).click()
                                        sleep(2)
                                        print(f'          [{GREEN}PASS{RESET}]              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                                        driver.close()
                                    except:
                                        print(f'          [{RED}FAIL{RESET}]              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                                        driver.close()
                                        sleep(0.1)

# define hiển thị
def option_menu(profiles):
    
    print("="*40)
    print(f"\n=== {BLUE}CHỈNH SỬA CẤU HÌNH{RESET} ===")
    print(f"[{RED}1{RESET}] Xóa tất cả cấu hình Trao Đổi Sub")
    print(f"[{YELLOW}2{RESET}] Xóa chỉ định cấu hình Trao Đổi Sub")
    print(f"[{GREEN}3{RESET}] Thêm cấu hình Trao Đổi Sub ")
    
    choice = input(f'{GREEN}Nhập lựa chọn,(X để quay lại):{RESET}').strip().upper()

    if choice == "1":
        clean_all(profiles)
    elif choice == "2":
        while True:
            # print("="*40)
            # print(f"\n=== {BLUE}Kedo TOOL{RESET} ===")
            # print(f"----------copyright: Mle × KEDO")
            asdfads, passwords = lay_data()
            for i, profile in enumerate(asdfads):
                print(f"[{i}] {RED}{profile}{RESET}")
                
            choice = input(f'{GREEN}Nhập tài khoản muốn xóa,(X để quay lại):{RESET}').strip().upper()
            if choice.isdigit() and 0 <= int(choice) < len(asdfads):
                selected_profile = asdfads[int(choice)]
                base_profile_path = os.path.dirname(os.path.abspath(__file__))+'\profiles'
                selected_profile_path = os.path.join(base_profile_path, selected_profile)
                print(selected_profile_path)
                clean(selected_profile_path)
                print(f"Đã xóa dữ liệu: {selected_profile}")
            elif choice == "X":
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng thử lại.")
                # os.system('cls' if os.name == 'nt' else 'clear')
    elif choice == "3":
        tao_profile()
    elif choice == "X":
        print("Đang quay lại menu chính.")
        sleep(1)
    else:
        print("Lựa chọn không hợp lệ, vui lòng thử lại.")
        # os.system('cls' if os.name == 'nt' else 'clear')
def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    lsohfoishd = fr"""{Fore.BLUE}{Style.BRIGHT}                 _  __ _____  ____    ___    _____   ___    ___   _     
                | |/ /| ____||  _ \  / _ \  |_   _| / _ \  / _ \ | |
                | ' / |  _|  | | | || | | |   | |  | | | || | | || |
                | . \ | |___ | |_| || |_| |   | |  | |_| || |_| || |___
                |_|\_\|_____||____/  \___/    |_|   \___/  \___/ |_____|
    """
    print(lsohfoishd)
    print(f"                {Fore.CYAN}╔════════════════════════════════════════════════════╗")
    print(f"                ║ {Style.BRIGHT}         📢 COPYRIGHT: Mle × KEDO 📢{Style.RESET_ALL}               ║")
    print(f"                ║ {Fore.YELLOW}     🔗 Link: https://zalo.me/g/uaahwq871{Style.RESET_ALL}          ║")
    print(f"                ╚════════════════════════════════════════════════════╝")
    print(f"\n{Fore.YELLOW}🛠️ QUẢN TRỊ CẤU HÌNH{Style.RESET_ALL}")
    print(f"  [{Fore.YELLOW}1{Style.RESET_ALL}] MỞ TẤT CẢ CẤU HÌNH 🔧")
    print(f"  [{Fore.YELLOW}2{Style.RESET_ALL}] MỞ CHỈ ĐỊNH CẤU HÌNH 📂")
    print(f"  [{Fore.YELLOW}3{Style.RESET_ALL}] CHỈNH SỬA CẤU HÌNH ✏️")
    print(f"\n{Fore.RED}⚙️ HOẠT ĐỘNG CẤU HÌNH{Style.RESET_ALL}")
    print(f"  [{Fore.RED}4{Style.RESET_ALL}] TTC POST ANTI BLOCK 🚫")
    print(f"\n        [X] Thoát chương trình ❌")
def khuyen_cao():
    print(f"\n{Fore.CYAN}▲▲▲ THÔNG BÁO QUAN TRỌNG ▲▲▲{Style.RESET_ALL}")
    print(f"{'─'*40}")
    print(f"➀ {Fore.YELLOW}BẮT BUỘC{Style.RESET_ALL}: Đăng nhập tài khoản Facebook trước khi chạy.")
    print(f"➁ {Fore.YELLOW}BẮT BUỘC{Style.RESET_ALL}: Đảm bảo tài khoản đã đặt làm nick chạy.")
    print(f"➂ {Fore.YELLOW}KHUYẾN NGHỊ{Style.RESET_ALL}: Đợi 24-48 giờ để tài khoản được tin cậy.")
    print(f"✗ {Fore.RED}KHÔNG{Style.RESET_ALL}: Đóng trình duyệt thủ công khi đang chạy.")
    print(f"✗ {Fore.RED}KHÔNG{Style.RESET_ALL}: Sử dụng ngay khi đang thiết lập cấu hình.")
    print(f"{'─'*40}")
    print(f"✦ Cấu hình chỉ khả dụng khi đã {Fore.YELLOW}liên kết{Style.RESET_ALL} với TraoDoiSub.")
    print(f"✦ ANTI BLOCK hoạt động ổn định khi tài khoản {Fore.YELLOW}được tin cậy{Style.RESET_ALL}.")
    print(f"✦ Hiệu suất tối đa với tài khoản {Fore.YELLOW}VIA đã xác minh{Style.RESET_ALL}.")
    print(f"☒ Đang khắc phục lỗi hiển thị nhỏ trên Windows.")
    print(f"◆ các bạn hãy SĂN cùng {Fore.LIGHTBLUE_EX}Quý x Mạnh{Style.RESET_ALL}!")
    print(f"{'─'*40}")
while True:
    profiles, passwords = lay_data()
    print(profiles)
    if not profiles:
        print(f"{RED}Không có Tài Khoản nào trong hệ thống!{RESET}")
        input("Nhấn Enter để tạo mới...")
        tao_profile()
        profiles, passwords = lay_data()
    # tk = input(f'{GREEN}Nhập Token TDS của bạn: ')
    tk =''
    
    main_menu()
    choice = input(f'{GREEN}Nhập lựa chọn:{RESET}').strip().upper()
    if choice == "1":
        facebok_all(profiles, passwords)
    elif choice == "2":
        facebook()
    elif choice == "3":
        option_menu(profiles)
        continue
    elif choice == "4":
        tds()
    elif choice == "X":
        print("Đã thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng thử lại.")







    
