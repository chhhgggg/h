from pystyle import Write,Colorate,Colors
import os,json,random,time
import numpy as np
from api import hustmedia , instagram
do = '\033[31m'
xanhla ='\033[32m' 
xanhduong ='\033[34m'
vang ='\033[33m'
tim ='\033[35m'
xanhCyan ='\033[36m'
trang ='\033[37m'
class hustmedia_instagram:
    def __init__(self):
        pass
    def menu():
        if 'nt' in os.name:
            os.system('cls')
        else:
            os.system('clear')
        
        print(f'{vang}════════════════════════════════════════════════════════════════════════')
        file = os.listdir()
        if "data.json" in file:
            with open('data.json','r') as file1 :
                datab = json.load(file1)
            apikeycheck = datab['apikey']
            hustmedia(apikeycheck).danngnhap("insta")
            stt = 1
            text_cookie = Colorate.Horizontal(Colors.green_to_red,'Do you want to use cookie(y/n) : ')
            text_setting = Colorate.Horizontal(Colors.purple_to_blue,"Do you want to use setting(y/n) : ")
            text_apikey = Colorate.Horizontal(Colors.blue_to_cyan,'Do you want to use apikey(y/n) : ')
            select_apikey = input(text_apikey)
            if select_apikey == 'y':
                pass
            else:
                while True:
                    nhapApikey1 = input(Colorate.Horizontal(Colors.green_to_red,'Nhập apikey của bạn : '))
                    try:    
                            sodu = hustmedia(nhapApikey1).danngnhap('instagram')
                            writesodu = 'số dư:'+str(sodu)+'\n'
                            ten = hustmedia(nhapApikey1).get_usernameHutsmedia()
                            writeTen = 'username:'+ten+'\n'
                            Write.Print('════════════════════════════\n',Colors.blue_to_black,interval=0.0001)
                            Write.Print(writeTen,Colors.red_to_purple,interval=0.0001)
                            Write.Print(writesodu,Colors.green_to_red,interval=0.0001)
                            Write.Print('════════════════════════════\n',Colors.blue_to_black,interval=0.0001)
                            # đọc file
                            with open('data.json', 'r') as file:
                                data = json.load(file)
                            data['apikey'] = nhapApikey1
                            # ghi apikey vào file
                            with open('data.json','w') as apikey3:
                                json.dump(data,apikey3,indent=4)
                            break
                    except :
                        print(f'{do}apikey không đúng ')
                        continue
            with open('data.json', 'r') as lay_cookie:
                listcookie = json.load(lay_cookie)['listcookie']
            for name_and_cookie in listcookie:
                name = name_and_cookie['name']
                cookie = name_and_cookie['cookie'] 
                check = instagram(cookie).check_live_ig()
                if check == 'live':
                    status = f'{trang}[{xanhla}live{trang}]'
                elif check == 'die':
                    status = f'{trang}[{do}die{trang}]'
                print(Colorate.Horizontal(Colors.red_to_blue,f'           >>>>>> [{stt}]'),end="")
                print(xanhduong,name,status)
                stt += 1             
            with open('data.json', 'r') as getapikey:
                get_apikey = json.load(getapikey)
            apikey = get_apikey['apikey']
            select_cookie = input(text_cookie)
            if select_cookie == 'y':
                pass
            else :
                luaChon =input(Colorate.Horizontal(Colors.yellow_to_red,'Bạn muốn đổi tất cả [all] hay 1 trong các cookie [nhập kí tự bất kì] : '))
                if luaChon == 'all':
                    arrcookie = []
                    lanNhap = 1
                    while True:
                        nhapCookie = input(Colorate.Horizontal(Colors.blue_to_green,f'[{lanNhap}]Nhập cookie của bạn nhập (out) để thoát nhập cookie :  '))
                        if nhapCookie == 'out':
                            with open('data.json', 'r') as getcookie:
                                get_cookie = json.load(getcookie)
                            get_cookie .update({'listcookie':arrcookie})
                            with open('data.json', 'w') as getcookie1:
                                json.dump(get_cookie,getcookie1,indent=4)
                            break
                        try:
                            check = instagram(nhapCookie).ten()
                            if check in hustmedia(apikey).get_list_nick('instagram'):
                                print(vang,'═══════════════════════════════════════════════════════════════════\r')
                                print(xanhCyan,check,f'{trang}</>',xanhCyan,f'https://www.instagram.com/{check}/')
                                print(vang,'═══════════════════════════════════════════════════════════════════\r')
                                lanNhap += 1
                                arrcookie.append({'name':check,'cookie':nhapCookie})
                                continue
                            else :
                                print(f'{do} Nick chưa thêm vào hệ thống ')
                                lanNhap += 1
                                continue
                        except IndexError:
                            print(f'{do}cookie không đúng')
                            lanNhap += 1
                else:
                    with open('data.json', 'r') as lay_cookie:
                        listcookie1= json.load(lay_cookie)
                        listcookie = listcookie1['listcookie']
                    index_cookie = input(Colorate.Horizontal(Colors.cyan_to_green,'Chọn nick muốn thay đổi (nhập số) : '))
                    input_cookie = input(f'{do} ➺ {xanhCyan}Nhập cookie của bạn : ')
                    listcookie1['listcookie'][int(index_cookie) - 1]['cookie'] = input_cookie
                    with open('data.json', 'w') as input_2_cookie:
                        change_cookie = json.dump(listcookie1,input_2_cookie,indent=4)
            select_setting = input(text_setting)
            if select_setting == 'y':
                pass
            else :
                input_min_fl = input(Colorate.Horizontal(Colors.blue_to_cyan,'Nhập min follow : '))
                input_max_fl = input(Colorate.Horizontal(Colors.cyan_to_green,'Nhập max follow : '))
                input_min_like = input(Colorate.Horizontal(Colors.blue_to_red,'Nhập min like : '))
                input_max_like = input(Colorate.Horizontal(Colors.red_to_blue,"Nhập max like : "))
                input_bao_nhieu = input(Colorate.Horizontal(Colors.yellow_to_red,'Bao nhiêu lần job thì nghỉ : '))
                input_delay_getJob = input(Colorate.Horizontal(Colors.yellow_to_red,'Nhập delay lấy job : '))
                with open('data.json','r') as setting_1:
                    data12 = json.load(setting_1)
                # thay đổi min max
                data12['setting'][0]['min'] = input_min_fl
                data12['setting'][0]['max'] = input_max_fl
                data12['setting'][1]['min'] = input_min_like
                data12['setting'][1]['max'] = input_max_like
                data12['setting'][2]['maxjob'] = input_bao_nhieu
                data12['setting'][2]['maxjob'] = input_bao_nhieu
                data12['setting'][2]['delay'] = input_delay_getJob
                with open('data.json','w') as change_setting:
                    json.dump(data12,change_setting,indent=4)
        else:
            while True:
                apikey_input_1 = input(Colorate.Horizontal(Colors.green_to_yellow,'Nhập apikey của bạn : '))
                check_apikey = hustmedia(apikey_input_1).danngnhap('instagram')
                if check_apikey == 'failure':
                    print(f'{do} Apikey không đúng !!!')
                    continue
                else: 
                    name = hustmedia(apikey_input_1).get_usernameHutsmedia()
                    print(Colorate.Horizontal(Colors.yellow_to_red,'═══════════════════════════════════════════════════════════\n'))
                    print('name : '+xanhCyan+name,'☵','số dư instagram : '+xanhla+str(check_apikey))
                    print(Colorate.Horizontal(Colors.yellow_to_red,'═══════════════════════════════════════════════════════════\n'))
                    break
            with open('data.json','w') as add_apikey:
                json.dump({'apikey':apikey_input_1},add_apikey,indent=4)
            with open('data.json','r') as get__apikey:
                apikey_check_cookie = json.load(get__apikey)['apikey']
            so_luong_cookie = 1
            arr_cookie = []
            while True :
                cookie_input_1 = input(f'{trang}[{tim}{so_luong_cookie}{trang}] {xanhCyan}Nhập cookie của bạn (nhập out để thoát) : {vang}')
                if cookie_input_1 == 'out':
                    break
                checkCookie = instagram(cookie_input_1).check_live_ig()
                if checkCookie == 'die':
                    print(f'{do} cookie sai !!!')
                    so_luong_cookie += 1
                    continue
                elif checkCookie == 'live':
                    username = instagram(cookie_input_1).ten()
                    if username in hustmedia(apikey_check_cookie).get_list_nick('instagram'):
                        print(tim,'════════════════════════════════════════════════════════════════════════════════\r')
                        print(xanhCyan,username,f'{trang}</>',xanhCyan,f'https://www.instagram.com/{username}/')
                        print(tim,'════════════════════════════════════════════════════════════════════════════════')
                        so_luong_cookie += 1
                        arr_cookie.append({"name":username,"cookie":cookie_input_1})
                    else:
                        so_luong_cookie += 1
                        print(f"nick chưa được thêm vào hệ thống")
                        continue
                with open('data.json','r') as read_file:
                    data_imformation = json.load(read_file)
                list_cookie = {'listcookie':arr_cookie }
                data_imformation.update(list_cookie)
                with open('data.json', 'w') as file:
                    json.dump(data_imformation,file,indent=4) 
            input_min_fl = input(Colorate.Horizontal(Colors.blue_to_cyan,'Nhập min follow : '))
            input_max_fl = input(Colorate.Horizontal(Colors.cyan_to_green,'Nhập max follow : '))
            input_min_like = input(Colorate.Horizontal(Colors.blue_to_red,'Nhập min like : '))
            input_max_like = input(Colorate.Horizontal(Colors.red_to_blue,"Nhập max like : "))
            input_delay_getJob = input(Colorate.Horizontal(Colors.yellow_to_red,'Nhập delay lấy job : '))
            input_bao_nhieu = input(Colorate.Horizontal(Colors.yellow_to_red,'Bao nhiêu lần job thì nghỉ : '))
            with open('data.json','r') as read_setting_file:
                data_setting_1 = json.load(read_setting_file)
            data_setting = {"setting":[{"min":input_min_fl,"max":input_max_fl},{"min":input_min_like,"max":input_max_like},{'maxjob':input_bao_nhieu,'delay':input_delay_getJob}]}
            data_setting_1.update(data_setting)
            with open('data.json', 'w') as add_setting_file:
                json.dump(data_setting_1,add_setting_file,indent=4) 
    def Run_follow_ig(cookie,sojob_dalam = 1):
        sojob = int(sojob_dalam)
        arr_nick_da_follow = []
        with open('data.json','r') as get__apikey:
            data = json.load(get__apikey)
            apikey = data['apikey']
            max_job = data['setting'][2]['maxjob']
        dangnhap = hustmedia(apikey).danngnhap('insa')
        for wait_dangnhap in range(5):
            print(f'{trang}Đang đăng nhập',end="\r")
            time.sleep(1)
        if dangnhap == 'failure':
            print(f'{do}đăng nhập thất bại')
            print(f'{do}vui lòng kiểm tra lại apikey và vào lại tool')
            quit()
        else:
            print(f'{trang}[{xanhla}success{trang}] {vang}đăng nhập thành công',end="\r")
            time.sleep(1)
            min_fl = data['setting'][0]['min']
            max_fl = data['setting'][0]['max']
            delay_getJob = int(data['setting'][2]['delay'])
            for i in range(delay_getJob):
                print(Colorate.Horizontal(Colors.pink,"➤"),Colorate.Horizontal(Colors.red_to_blue,f" Đang lấy job chờ {delay_getJob} s                             "),end="\r")
                time.sleep(1)
            list_job_hustmedia = hustmedia(apikey).getJob("subcheo","insta")['message']
            print( f"{trang}➥{xanhCyan} Đã thấy {len(list_job_hustmedia)} job follow                                             ")                      
            try:
                for lits_job in list_job_hustmedia:
                    if sojob==int(max_job) :
                        for wait in range(40):
                            print(f'đang nghỉ chờ {wait}',end="\r")
                            time.sleep(1)
                        sojob = 1
                        continue
                    else:
                        if len(arr_nick_da_follow) == 6:
                            print(f'{vang}--------------------------------------------------------------------')
                            try :
                                reccive = hustmedia(apikey).receive_money(','.join(arr_nick_da_follow),"subcheo","insta")
                                coin_nhan = reccive["sodu"]
                                for nhan_delay in range(5):
                                    print(f'{xanhCyan}Đang nhận tiền chờ 5s',end="\r")
                                    time.sleep(1)
                                print(f'{trang}[{xanhla}success{trang}] {vang}nhận tiền thành công | {xanhla}+{coin_nhan}')
                                arr_nick_da_follow = []
                                print(f'{vang}--------------------------------------------------------------------')
                                continue
                            
                            except:
                                print(f'{do}lỗi không nhận được tiền')
                                print(f'{vang}--------------------------------------------------------------------')
                                continue
                        else:
                            delay_follow = random.randint(int(min_fl),int(max_fl))
                            idpost = lits_job['idpost']
                            link = str(lits_job['lienket']).split("com/")[1]
                            follow = instagram(cookie).follow(idpost)
                            for wait in range(delay_follow,0,-1):
                                print("➤",Colorate.Horizontal(Colors.red_to_blue,f" Đang follow {wait}/{delay_follow}           "),end="\r")
                                time.sleep(1)
                            if follow:
                                print(f'{trang}[{xanhla}{sojob}/{xanhCyan}{max_job }] {vang}follow thành công >>  {tim}{idpost} {trang}<|> {xanhla}{link}')
                                sojob+= 1
                                arr_nick_da_follow.append(idpost)
                                continue
                            else:
                                print(f'{do}follow thất bại                           ',end="\r")
                                time.sleep(0.5)
                                for lan_bam_followLai in range(3):
                                    for i in range(4):
                                        time.sleep(1)

                                    print(f"Đang bấm follow lần thứ  :  {lan_bam_followLai}",end="\r")
                                    follow_lai = instagram(cookie).follow(idpost)
                                    if follow_lai:
                                        print(f'{trang}[{xanhla}{sojob}/{xanhCyan}{max_job }] {vang}follow thành công >>  {tim}{idpost} {trang}<|> {xanhla}{link}')
                                        arr_nick_da_follow.append(idpost)
                                        sojob += 1
                                        break
                                    else:
                                        if lan_bam_followLai == 2:
                                            print(f'{trang}[{do}{sojob}/{xanhCyan}{max_job }] {do}follow thất bại  / {vang}{link} !!     ')
                                            sojob += 1
                                            break
                                        else:
                                            continue
            except:
                pass
        return sojob
    def Run_like(cookie,so_job_da_lam = 1):
        with open('data.json','r') as file:
            data = json.load(file)
        apikey = data['apikey']
        max_like = data['setting'][1]['max']
        min_like = data['setting'][1]['min']
        max_job = data['setting'][2]['maxjob']
        delay_getJob = data['setting'][2]['delay']
        hustmedia1 = hustmedia(apikey) 
        dang_nhap = hustmedia1.danngnhap("insta")
        if so_job_da_lam == int(max_job):
            for wait in range(40):
                print(f'{trang}Đang nghỉ chờ {wait}',end="\r")
                time.sleep(1)
            so_job_da_lam = 1
        else:
            if dang_nhap == 'failure':
                print(f'{do}đăng nhập thất bại')
                print(f'{do}vui lòng kiểm tra lại apikey và vào lại tool')
                quit()
            else:
                print(f'{xanhla}Đang nhập thành công',end="\r")
                time.sleep(2)
                print(f'{vang}Đang get jop chờ : {delay_getJob} s',end="\r")
                time.sleep(int(delay_getJob))
                get_job = hustmedia1.getJob("timcheo","insta")
                print(f'{tim}Đã thấy {len(get_job["message"])} job                                             ')
                list_job = get_job['message']
                for job in list_job:
                    idpost = job['idpost']
                    link = job['lienket']
                    mediaid = job['mediaid']
                    delay_like = random.randint(int(min_like),int(max_like))
                    for wait1 in range(delay_like,0,-1):
                        print(f'{trang}Đang like {wait1}/{delay_like}                                         ',end="\r")
                        time.sleep(1)
                    like = instagram(cookie).like(mediaid)
                    if like == 'ok':
                        text = Colorate.Horizontal(Colors.green_to_blue,f'like thành công                                          ')
                        print(text,end = "\r")
                        time.sleep(2)
                        reccive = hustmedia1.receive_money(idpost,"timcheo","insta")
                        for wait in range(5):
                            print(f'{vang}Đang {do}nhận {xanhCyan}tiền chờ {wait}',end="\r")
                            time.sleep(1)
                        if "mess" in str(reccive):
                            if 'Thành công' in  reccive['mess']:
                               soDiem = reccive['mess'].split('cộng ')[1].split(' điểm')[0]
                               print(f'{do}[{xanhla}{so_job_da_lam}{do}] {xanhla}|success| {vang}{link} {xanhCyan} + {tim}{soDiem} điểm')
                               so_job_da_lam += 1
                            else:
                                print(f'{do}nhận tiền thất bại',end = "\r")
                                time.sleep(2)
                                print(f'đang thử lại',end="\r")
                                time.sleep(2)
                                unlike = instagram(cookie).unlike(mediaid)
                                time.sleep(2)
                                like = instagram(cookie).like(mediaid)
                                reccive = hustmedia1.receive_money(idpost,"timcheo","insta")
                                if 'Thành công' in  reccive['mess']:
                                    soDiem = reccive['mess'].split('cộng ')[1].split(' điểm')[0]
                                    print(f'{do}[{xanhla}{so_job_da_lam}{do}] {xanhla}|success| {vang}{link} {xanhCyan} + {tim}{soDiem} điểm')
                                    so_job_da_lam += 1
                                else:
                                    print(f'{trang}[{do}{so_job_da_lam}{trang}] {do}|fail| {vang}{link}  ')
                                    so_job_da_lam += 1
                        elif 'error' in str(reccive):
                            print(f'{do}nhận tiền thất bại                          ',end = "\r")
                            time.sleep(2)
                            print(f'đang thử lại                         ',end="\r")
                            time.sleep(2)
                            unlike = instagram(cookie).unlike(mediaid)
                            time.sleep(2)
                            try:
                                like = instagram(cookie).like(mediaid)
                            except:
                                check_live = instagram(cookie).check_live_ig()
                                if check_live == 'live':
                                    continue
                                elif check_live == 'die':
                                    print(f'{do} NICK IG ĐÃ BỊ DIE')
                                    quit()
                            reccive = hustmedia1.receive_money(idpost,"timcheo","insta")
                            if 'mess' in reccive:
                                if 'Thành công' in reccive['mess']:
                                    soDiem = reccive['mess'].split('cộng ')[1].split(' điểm')[0]
                                    print(f'{do}[{xanhla}{so_job_da_lam}{do}] {xanhla}|success| {vang}{link} {xanhCyan} + {tim}{soDiem} điểm')
                                    so_job_da_lam += 1
                                else:
                                    print(f'{trang}[{do}{so_job_da_lam}{trang}] {do}|fail| {vang}{link}  ')
                                    so_job_da_lam += 1
                            else:
                                print(f'{trang}[{do}{so_job_da_lam}{trang}] {do}|fail| {vang}{link}  ')
                                so_job_da_lam += 1
                    else:
                        print(f'{do}like thất bại hoặc link die',end="\r")
                        time.sleep(2)
                        continue
def run():
    hustmedia_instagram.menu()
    print(f'{do}[{trang}1{do}]{xanhCyan} AUTO FOLLOW IG')
    print(f'{do}[{trang}2{do}]{xanhCyan} AUTO LIKE IG')
    while True:
        text = Colorate.Horizontal(Colors.blue_to_green,'>>> Chọn chế độ (vd:1) : ')
        che_do = input(text)
        if che_do == '1' or che_do == '2':
            break
        else:
            print(f'{vang}[{do}??{vang}] lỗi cú pháp .VUI LÒNG NHẬP LẠI')
            continue 
    with open('data.json','r') as file:
        data = json.load(file)
    list_cookie = data['listcookie']
    stttt = 1
    for data_name in list_cookie:
        name = data_name['name']
        print(Colorate.Horizontal(Colors.cyan_to_blue,f"   [{stttt}] {name}"))
        stttt+=1
    chon_nick = input(f'{vang} Chọn nick để chạy (có thể chọn nhiều nick) (vd:123): ').split(" ")
    cookie_chay = []
    for index in chon_nick:
        cookie1 = list_cookie[int(index)-1]['cookie']
        cookie_chay.append(cookie1)
    while True:
        for cookie in cookie_chay:
            if che_do == '1':
                hustmedia_instagram.Run_follow_ig(cookie)
            else :
                hustmedia_instagram.Run_like(cookie)
        
class ADB:
    def __init__(self,handle):
        self.handle = handle
    def screen_capture(self,name):
        os.system(f"adb -s {self.handle} exec-out screencap -p > {name}.png ")
    def click(self,x,y):
        os.system(f"adb -s {self.handle} shell input tap {x} {y}")
    def find(self,img='',template_pic_name=False,threshold=0.99):
        if template_pic_name == False:
            self.screen_capture(self.handle)
            template_pic_name = self.handle+'.png'
        else:
            self.screen_capture(template_pic_name)
        img = cv2.imread(img)
        img2 = cv2.imread(template_pic_name)
        result = cv2.matchTemplate(img,img2,cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        test_data = list(zip(*loc[::-1]))
        return test_data

class golike_instagram:
    def __init__(self,author):
        self.author = author
