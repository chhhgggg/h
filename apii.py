import requests
import base64
import dns.resolver
import socket
from tabulate import tabulate
from pystyle import Write
from tabulate import tabulate
from pystyle import Colorate, Colors
from datetime import datetime
import sys
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

class facebook:
    def __init__(self,cookie):
        self.cookie = cookie
        self.session = requests.Session()
        self.session.cookies.update(cookie)
        self.headers = {
    'accept': '*/*',
    'origin': 'https://www.facebook.com',
    'priority': 'u=1, i',
    'referer': 'https://www.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="131.0.6778.265", "Chromium";v="131.0.6778.265", "Not_A Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'x-asbd-id': '129477',
    'x-fb-friendly-name': 'CometUFIFeedbackReactMutation',}
        try:
            params = {'entry_point': 'app_settings',}
            response = self.session.get('https://accountscenter.facebook.com/', params=params, headers=self.headers).text
            id = response.split('"userID":')[1].split(',')[0]
            params = {'id': id,
                      'locale': 'vi_VN',}
            get_token = self.session.get('https://www.facebook.com/profile.php', params=params, headers=self.headers).text
            self.token = get_token.split('{"dtsg":{"token":"')[1].split('",')[0] 
            self.check = 'live'
        except:
            self.check = 'die'
            
    def get_uername_id(self):
        params = {
            'entry_point': 'app_settings',}
        response = self.session.get('https://accountscenter.facebook.com/', params=params, headers=self.headers).text
        name = response.split('"full_name":"')[1].split('"')[0]
        id = response.split('"userID":')[1].split(',')[0]
        a = [name,id]
        return a
    def follow(self,uid):
        data = {
    'av': '61555139777272',
    '__aaid': '0',
    '__user': '61555139777272',
    '__a': '1',
    '__req': '2u',
    '__hs': '20105.HYP:comet_pkg.2.1.0.2.1',
    'dpr': '1',
    '__ccg': 'GOOD',
    '__rev': '1019404516',
    '__hsi': '7460850281227569044',
    #'__dyn': '7xeXzWK1ixt0mUyEqxemh0noeEb8nwgUao4u5QdwSwAyUco5S3O2Saw8i2S1DwUx60GE5O0BU2_CxS320qa2OU7m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewyDwkUe9obrwh8lwUwgojUlDw-wUwxwjFovUaU6a1TxW2-VEbUGdG0HE88cA0z8c84q58jyUaUbGxe6Uak0zU8oC1hxB0qo4e4UcEeE-3WVU-4EdrxG1fBG2-2K2G0JUmw',
    #'__csr': 'gbk54dgH6NYjs9b6slbk8NIZONIJltlb8gn8B8DTGqGOFkybSOSDrZ9vGH9FtAhBBnyelIyn-miUEyhrmBAVdaAqlQZ_zehaGBjDiuVUSHzTzBABXunXQu8BJqCyQ78Gly8NaleUOh7KFoSmql5xC-aGbBWh8pzHCx28AwyCGi5UC6omAABzubxiaxK9jwAyVoy18K4J6Cxa4EbGwkqx6i3m2i4UhxS267U7q16xa78O1xwiojwDwlEG584G2u6UvwoU5Gfw21E1zU0xK2x07ABw47w8Gfw2yU5y08pwbkw2lw2P83Zw5qwkE04UW0o-015ow0bjS0ry5FEvw7sxK16w860bQw7TwTw4jK08Kg0bE405kE0yuEiglP02aU0hhxm06ok0rS027Dwww0xjw12Iw46',
    '__comet_req': '15',
    'locale': 'vi_VN',
    'fb_dtsg': self.token,
    '__spin_r': '1019404516',
    '__spin_b': 'trunk',
    '__spin_t': '1737114573',
    'variables': '''
{
  "input": {
    "attribution_id_v2": null,
    "is_tracking_encrypted": false,
    "subscribe_location": "PROFILE",
    "subscribee_id": '''+uid+''',
    "tracking": null,
    "actor_id": "61555139777272",
    "client_mutation_id": "4"
  },
  "scale": 1
}
    ''',
    'server_timestamps': 'true',
    'doc_id': '28167180839546919',
        }
        response = self.session.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).json()
        return response
    
    def like(self,link,type):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'max-age=0',
            'dpr': '1',
            'priority': 'u=0, i',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'viewport-width': '483',}
  
        uid = requests.get(link,headers=headers,).text.split('"subscription_target_id":"')[1].split('",')[0]
        #string ban đầu
        id  = 'feedback:'+uid
        # Encode the string to bytes, then encode to Base64
        encoded_bytes = base64.b64encode(id.encode('utf-8'))
        encoded_str = encoded_bytes.decode('utf-8')
        if type == "LOVE":
            idtype = '1678524932434102'
        elif type == "CARE":
            idtype = '613557422527858'
        elif type == "WOW":
            idtype = '478547315650144'
        elif type == "LIKE":
            idtype = "1635855486666999"
        elif type == "HAHA":
            idtype = '115940658764963'
        elif type == "ANGRY":
            idtype = "444813342392137"
        elif type == "SAD":
            idtype = '908563459236466'
        # tim :1678524932434102
        # tuc gian = 444813342392137
        # wow 478547315650144 
        # haha 115940658764963
        # thuong thuong 613557422527858
        # buon 908563459236466
        # like 1635855486666999
        data = {
    'av': '61555139777272',
    '__aaid': '0',
    '__user': '61555139777272',
    '__a': '1',
    '__req': '1y',
    '__hs': '20105.HYP:comet_pkg.2.1.0.2.1',
    'dpr': '1',
    '__ccg': 'GOOD',
    '__rev': '1019405004',
    '__s': 'oenrwt:f35s4d:0qde5o',
    '__hsi': '7460860911885816357',
    'fb_dtsg': self.token,
    'lsd': 'KmtLdSkP_LldjESHYmXykh',
    '__spin_r': '1019405004',
    '__spin_b': 'trunk',
    '__spin_t': '1737117048',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
    'variables': '''
{
  "input": {
    "attribution_id_v2": null,
    "feedback_id":"'''+encoded_str+'''",
    "feedback_reaction_id": "'''+idtype+'''",
    "feedback_source": "PROFILE",
    "is_tracking_encrypted": true,
    "tracking":null,
    "session_id": null,
    "actor_id": "61555139777272",
    "client_mutation_id": "1"
  },
  "useDefaultActor": false,
  "__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider": false
}
''',
    'server_timestamps': 'true',
    'doc_id': '8995964513767096',}
        
        response =self.session.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
# tim :1678524932434102
# tuc gian = 444813342392137
# wow 478547315650144 
# haha 115940658764963
# thuong thuong 613557422527858
# buon 908563459236466
# like 1635855486666999
        return(response)
    def comment(self,uid,noidung):
        id  = 'feedback:'+uid
        # Encode the string to bytes, then encode to Base64
        encoded_bytes = base64.b64encode(id.encode('utf-8'))
        feedback_id = encoded_bytes.decode('utf-8')

        data = {
                        
    'av': '61555139777272',
    '__aaid': '741100624818922',
    '__user': '61555139777272',
    '__a': '1',
    '__req': '5e',
    '__hs': '20105.HYP:comet_pkg.2.1.0.2.1',
    'dpr': '1',
    '__ccg': 'GOOD',
    '__rev': '1019405004',
    '__s': 't45smd:f35s4d:8s5iax',
    '__hsi': '7460880564757961757',
    '__dyn': '7xeXzWK1ixt0mUyEqxemh0noeEb8nwgUaqwh8ngS3q2ibwyzE5S3O2Saw8i2S1ixi3y4o2Gwn82nwb-q7oc81EE-7bwto88422y11wBz83WwgEcEhwGxu782lwv89kbxS1FwIw9i1awkovwRwlE-U2exi4UaEW2au1jwUBwJK14xm3y11xfxmu3W3y261eBx_wHwoE7u7EbXCwLyESE2KwwwOg2cwMwhEkxebwHwKG4UrwFg2fwxyo566k1FwgUjwOwWzUfHDzUiwRK6E4-mEbUaUaE2TzU',
    '__csr': 'gbY4Q5c4lNsRPTfsn2kG2qkG4l48W2dOOhdrtvjmB9dHqcy8ABLFidjjWAiimOaCgJiZRFn-LV5JviAGluZpnHltHqABppFC-aGhKHSK9zeEybF2bARhl-uq8VrCHnAAiKi_VUS49EyfKuuKE-mmmXWF4K9xheq499VqXV9A9J2FWKaK6rF1zz-8KEO7FUyEK4pHgOexuEdpUO4u2et6AVpqKcyocebwyKi2edypQ4paCxS5rxW22eDxOcy7xCawNxWEmwhEGEhDw-xC7EOm7EhwIUugjzWxO1eDzU9VE4e58aoS9wAw4VG0zUkwiES2y5A3RwhohwmUxVUswmaxe3a10wfZ1idCu0TU3lwno11U17oO1VwNyokwTxq1fK2tBz8Ki0jOu3VU0Qa0aMwb-Ua82UwzgaEaeu03LC3m0nW1Oo04ou01_sw0goE0Ra0ju08mCw3tE6m05BE2Mgy1Tg5S0l_c0DU6O0zo08Go0hcw1Mu03Vu08Fw6KK59U0_e07CUlw5Uw1Cq0M2o0Hu0GO0s92mCEF6gnbw',
    '__comet_req': '15',
    'fb_dtsg': 'NAcPY2zhOLVVM5Lm2bW2yweOmDYEiS2WFncJjn9gYgmc9DLX8Ng6kiA:38:1725172609',
    'jazoest': '25423',
    'lsd': 'UsY_wlj8FX6H8Dff4IbGtI',
    '__spin_r': '1019405004',
    '__spin_b': 'trunk',
    '__spin_t': '1737121624',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'useCometUFICreateCommentMutation',
    'variables': '{"feedLocation":"TIMELINE","feedbackSource":0,"groupID":null,"input":{"client_mutation_id":"2","actor_id":"61555139777272","attachments":null,"feedback_id":"ZmVlZGJhY2s6OTI1NzIwNDM5Njk0MjM5","formatting_style":null,"message":{"ranges":[],"text":"89kihj78ik"},"reply_target_clicked":false,"attribution_id_v2":"FriendingCometRoot.react,comet.friending,via_notification,1737121798084,727463,2356318349,,","vod_video_timestamp":null,"is_tracking_encrypted":true,"tracking":["{\\"alert_id\\":\\"1736905391871959\\",\\"notif_source\\":\\"notif_tab\\",\\"notif_type\\":\\"friend_confirmed\\"}","AZUTH8Nbqj5dx5rlRDIX0favTkQU9OvsVlJtKT9nTsw1-jEMHqAfDJItj5653XrkfvrLY7p6LGEi79S25yD7wekjRYOtV3pX4XjTMcJa5IYW5AA-jBxGlL4ZafM11YuV5pfQLd4CcfRicgS6R2RvV__gLGe9-qVUrSUbkVra0A3YT3f_Q_reR_SmtkFVap_G1of8iBgNpNwU6YWp-tFx7-H2DPm55_JZYjybCR4VX9Ax7Z3xX0zUIwFX6Eqz1igI8BFVLFgXsFTwE5Bcdj6zsc5pdCIbsytv7zXSl4dXgN-fThiqaaAmmAdO61h_A7DBeIzitx2cKGXxTOuKC49SWimsWxLPyya6QUK_Et_fBYE_3E_bjL4olhuG_xZIwOfVY2zMbpLrALo1ze4L3vXFVHeXjDSUoKoNIDE9ieJrnIq3GvsMefflCLT80dTINXX_dxGUE6f5ZtcdeVXQ4O8S-3SnjV67LhgdibsTVQV8nftUr7vHktHfKe4nUp1FuLEFvGXFgeKRftlYSGn0ajTdCj0Fj7c6XmwMQoPSy2TNIsaVOYz2dIoh1LOpDfzpjYqlVNO_UcWa9Q0ug1dIvYvAzolfbYjJvp8XPVKOOvWlMc33jbeadNbopbTlH1uPl0hepyUQcR5yzX0TNlSxEHXJgIQT68Z3R1IlWh9unghLruM-nBHZTga9EdEwu0xyW7OBpDzqkm3TWbPhARhs8wVzVrg2Apt8U7aBRzwnr5KcUiC-mtSAtCxCq3ISE0iJOYdL9r5vqxQokhcX2ngMEA3dt3G0pZATObjsXfli6ZflPhEAo6qpl0KqymKcms4wc-4jWVXmTw0o4c_54tV8XzsO0AEscaJEwuHE6EA4bh75gIdRAgJ0ThLakMUc4HnQMHXWJMk4DwlxuVEX8sq0akrLsF61swD7xKSgWpfKvotMbzKmD7ntwgGKlHLgEGMDHUWQyBeoEcZS5-V1XaL3vObmjaiEa-cKVi1cvyZW1ttklrYlfoMy2PyQvBr8dVf_Z8Co9B6c6EVoX44Z89F68PJ872-8Mfex0Pm7sWK_7T2_Pb6smnSiEnFgTFiXPL59cHGcKFwSy7EkjLk4H_9ogVIDX2yL__4eyAbEFW07Nkh5kiva1ERMZRSax1dmwhnzBUOMmXiIYWqAD19tvG9W4UVl6QDpYfqoEMyN3XmPLrj4ajGgNZM6rorqAAZN9jhGLtPA8SW7Z0QkMX3goaxmbc68kk18BSxSCW4MAXTRT7IKLml7vbkgVu9ggOxZ0xnGdJ-QuorXTlYBbPJZYDVGQ9JNNLBuKfeR6WmYszi1kW0XWO7WPQNpprhKp3ws7BrrVb_LI-A2lYPhmU27QYYSBihyt9XI5XBJB16QVdNx7BBV7xIogBHhImXtf98rkurCc6FAcsWXkRQgaCsm8EIekdrIyqRgDsWZl52eg-A5cpWIpoCftLiU4rTzntbNWoGBuLneLdaaCLKJJU_8DodubdmGaWgLKfeUg6d0B8wQP4PG2VWV5rg2Rg0hFZ69PCLpNKJZglKJZ6vZmla6zl37GS9viiCStH1dQNcarXYghmCRMhbskLTkXBnxUB5d8MAqBRpjy1lT77ZzuH-d1jNEjEngz_cWnHs7CwWp2huTcVhwjwGQsJpY4lvzIAYAVvphJef7MnMXfvuMJ7FfGD8hzP9DGIT4BfG_NMPV3VTEtkX9L7jWgPl9N_DoZPnRBRiJgYbF83LeI9ApyHpuhzLpJCkU-Pg1CvyqMRXkEVAGrTsDY3azxWuKiDwn0YC2iTBuk5E6JMvvzjNI18ZYdAoYVAHDdQfo1rEm_fLrHuGl4afL175kdqi_xV38VhS0H7ASOXSE7Jn097pKHm6aZTQCRYwsqp4Hv9CRqeCuite7nbfGSklDL54_fSQFmGbLeFAB_7Gb5k4","{\\"assistant_caller\\":\\"comet_above_composer\\",\\"conversation_guide_session_id\\":null,\\"conversation_guide_shown\\":null}"],"feedback_source":"PROFILE","idempotence_token":"client:13a16549-303d-49ee-8930-6416c0b79fd1","session_id":"ee957097-bb1f-4f3a-b723-f41fd25c145b"},"inviteShortLinkKey":null,"renderLocation":null,"scale":1,"useDefaultActor":false,"focusCommentID":null,"__relay_internal__pv__IsWorkUserrelayprovider":false}',
    'server_timestamps': 'true',
    'doc_id': '9847180558630401',

        }
        response = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
        return response
    def check_live_fb(self):
        if self.check == 'die' :
           check_live_cookie = 'die'
        elif self.check == 'live' :
           check_live_cookie = 'live'
        return check_live_cookie
class hustmedia:
    def __init__(self,apikey):
        self.apikey = apikey
        self.headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'origin': 'https://hust.media',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        }
    def getJob(self,theloai='',social=''):
        json_data = {
        'key': self.apikey,
        'chedo': 'getjop',
        'theloai': theloai,
        'social': social,}
        response = requests.post('https://hust.media/insta/profile.php', headers=self.headers, json=json_data).json() 
        return response
    def danngnhap(self,social):
        json_data = {
                'key': self.apikey,
                'chedo': 'kiemtradangnhap',
                'social': social,}
        login = requests.post('https://hust.media/insta/profile.php',headers=self.headers,json=json_data).json()
        if 'message' in login:
            sodiem = login['sodiem']
            return sodiem
        else:
            return 'failure'
    def get_list_nick(self,social):
        loi = 0
        json_data = {
                    'key': self.apikey,
                    'chedo': 'listcauhinh',
                    'social': social,}
        response = requests.post('https://hust.media/insta/profile.php', headers=self.headers, json=json_data).json()
        listname = []
        for i in response["listcauhinh"]:
                    listname.append(i["tenfb"])
        return listname

    def nickConfiguration(self,tenfb,social,idfb):
        json_data = {
                    'key': self.apikey,
                    'idfacebook': idfb,
                    'chedo': 'choncauhinh',
                    'chedokiemxu': 1,
                    'social': social,
                    'tenfb': tenfb,}

        response = requests.post('https://hust.media/insta/profile.php',headers=self.headers, json=json_data).text
        return response
    def receive_money(self,idpost,theloai,social):
        data = {
            'key':  self.apikey,
            'idpost':idpost,
            'theloai': theloai,
            'social':social, }   
        a = requests.post('https://hust.media/insta/nhantien.php', headers=self.headers,json = data).json()
        return a
    def get_usernameHutsmedia(self):
        json_data = {
    'apikey': self.apikey,
    'chedo': 'profile',
    'option': 'showusername',
    'lienketchay': '',}

        response = requests.post('https://hust.media/api/profile/profile.php', headers=self.headers, json=json_data).json()
        return response['message']
class instagram:
    def __init__(self,cookie):
        try:
            self.cookie = cookie
            self.session = requests.Session()
            self.session.cookies.update(cookie)
            self.headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': self.cookie,
        'origin': 'https://www.instagram.com',
        'priority': 'u=1, i',
        'referer': 'https://www.instagram.com/p/DBHIlVQyw8s/?utm_source=ig_web_copy_link',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="129.0.6668.60", "Not=A?Brand";v="8.0.0.0", "Chromium";v="129.0.6668.60"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'x-asbd-id': '129477',
        'x-bloks-version-id': '1fbbc4a302825e0a86a865a39546a4fa9f0b70d85f967657fb4bb32422a40f5c',
        'x-csrftoken': self.cookie.split('csrftoken=')[1].split(';')[0],}
            response = self.session.get('https://www.instagram.com/', headers=self.headers).text
            self.tenig = response.split('"username":"')[1].split('"')[0]
            self.dtsg = self.session.get(f'https://www.instagram.com/{self.tenig}/', headers=self.headers).text.split('"dtsg":{"token":"')[1].split('",')[0]
            self.check = 'live'
        except :
            self.check = 'die'
    def like(self,id):
        data = {
        'av': '17841463976553652',
        '__d': 'www',
        '__user': '0',
        '__a': '1',
        '__req': 'p',
        '__hs': '20011.HYP:instagram_web_pkg.2.1..0.1',
        'dpr': '1',
        '__ccg': 'GOOD',
        '__rev': '1017345987',
        '__s': 'b499oe:jq6ibt:qj8c7j',
        '__hsi': '7425956412009585319',
        '__dyn': '7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0k24o1DU2_CwjE1xoswaq0yE462mcw5Mx62G5UswoEcE7O2l0Fwqo31w9O1TwQzXwae4UaEW2G0AEco5G0zK5o4q3y1Sx-0lKq2-azqwt8d-2u2J0bS1LwTwKG1pg2fwxyo6O1FwlEcUed6goK2O4UrAwHxW1oCz8rwHwrE5SEy9w',
        '__csr': 'gD7gqhIavkaN9y48HlhBZbqHAkBrWFqJ5FllaKCAGDV9Wh9FFr-Ftat2J6z7zFJaTBy5ACqyVpf8m8y8yUlBAoSbz8yu8ze8DKaxp2pByV8G-EG4UG4Kh29kpuit4BCzUV3XwJyUG8Gi4U01euU2Nwik0hi2O0kaqt2FE1pde3tw5pw1CK0u0zwdl2E1iU0AxqwQxAEkwm8zB5wko7i0ii1fqgK2h2A6RfeV27wbxsUHg5u0myq0OE5q0Q8co3Owgk02xC01m-w2C8',
        '__comet_req': '7',
        'fb_dtsg': self.dtsg,
        'jazoest': '26352',
        'lsd': 'X75RNmje5WVfzVL-Ea0r-t',
        '__spin_r': '1017345987',
        '__spin_b': 'trunk',
        '__spin_t': '1728990211',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'usePolarisLikeMediaLikeMutation',
        'variables': '''

            {
            "media_id": "'''+id+'''",
            "container_module": null,
            "inventory_source": null,
            "ranking_info_token": null,
            "nav_chain": null
            }

            ''',
        'server_timestamps': 'true',
        'doc_id': '8552604541488484',
            }
        a = self.session.post('https://www.instagram.com/graphql/query',headers=self.headers,data=data)
        return a.json()['status']
    def unlike(self,id):
        data = {
                'av': '17841463976553652',
                '__d': 'www',
                '__user': '0',
                '__a': '1',
                '__req': 'w',
                '__hs': '20067.HYP:instagram_web_pkg.2.1.0.0.1',
                'dpr': '1',
                '__ccg': 'GOOD',
                '__rev': '1018751871',
                '__s': 'z8aele:imtjcp:fq6vw9',
                '__hsi': '7446692498273804459',
                '__dyn': '7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0k24o1DU2_CwjE1EE2Cw8G11wBz81s8hwGxu786a3a1YwBgao6C0Mo2swtUd8-U2zxe2GewGw9a361qw8Xxm16wUwtE1uVEbUGdG1QwTU9UaQ0Lo6-3u2WE5B08-269wr86C1mwPwUQp1yUb8jK5V8aUuwm9EO6UaUaE4e1tG8BK4o',
                '__csr': 'gnglNk5DsSIAoRilGIysgAZajirS_t5jmVlBQmH-iq8hsxbyFUhGmAHQAmdXX-jVu5aDtrKdpuiUCnyoHy48gycyV8ObhWh5xJ5yqKSHDLVEhyHQehQq9x2FHyWUgyoTAeBiCo8Aq8yo01g-U4te08hzqwrU6K0Lk0CU3IwdS2Svo1Lo6JyE0ye0eFwbyVnw129rDBig9okyEGO0l16tVWiw28EZ4cClr6zQ12A8mdQ1OwTF9ixCl0iE5W1jCkM7C5Hxt7xy0SUaoe83uwZ2wCYwk5o2dwBy8Ghw0zXhFQ01luw1fy0fZw1US',
                '__comet_req': '7',
                'fb_dtsg': self.dtsg,
                'jazoest': '26219',
                'lsd': 'Ftl-_viq8yWO_q6ijJJZzp',
                '__spin_r': '1018751871',
                '__spin_b': 'trunk',
                '__spin_t': '1733818207',
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'usePolarisLikeMediaUnlikeMutation',
                'variables': '''
{
  "media_id": '''+id+''',
  "container_module": "single_post",
  "inventory_source": null,
  "ranking_info_token": null,
  "nav_chain": "null"
}
            ''',
                'server_timestamps': 'true',
                'doc_id': '8525474704176507',
            }
        un = self.session.post('https://www.instagram.com/graphql/query',headers=self.headers,data=data).text
        return un
    def follow(self,target_user_id):
        data = {
                '__d': 'www',
                '__user': '0',
                '__a': '1',
                '__req': '27',
                '__hs': '20018.HYP:instagram_web_pkg.2.1..0.1',
                'dpr': '1',
                '__ccg': 'UNKNOWN',
                '__rev': '1017538317',
                '__s': 'cyi8q2:kpt43i:qi9c9v',
                '__hsi': '7428485612332142635',
                '__dyn': '7xeUjG1mxu1syaxG4Vp41twpUnwgU7SbzEdF8aUco2qwJyEiw9-1DwUx60p-0LVE4W0om78c87m0yE462mcw5Mx62G5UswoEcE7O2l0Fwqo31w9a9waOfK0zEkxe2GewGw9a3614xm0zK5o4q3y261kx-0lKq2-azqwt8d-2u2J08O321LwTwKG1pg2fwxyo6O1FwlEcUed6goK3ibxKi2qiUqwm9EO6UaU3cG8BK4o',
                '__csr': '8Yr22SJZsSYZcZPECy9sOEJFv8x9e_WpdF22JvRKAQV9vAaiFAJkl4Bh9dGn8iWp8ymhpp5mmSit7AjmETByQaKUjy9pUBqVEOiu8AxuaZaKh394teGBDGvAAG8GXzooK5ESvmvxbzopyoSfyFEzUox6U06yV00diGOUe96EhBzZw2_QGG0gu2cODgSHw968gjwE80Aagx163qkm1gwpUdp7g0I6yG4k4U1bU4ne0Fo2-xC8w72gcLjDz2AzA0xqxq5-cCy8W1QQ481L0C4k4YUcU2Cw9l0Rw8N0z28-m1cg4W4K9o5lhUNw92OyE7y4EhBhE2EG363mm13w7QaFR2awAg9QgAUnyQ1-wtE0zmrBwbeUlwLo0Yqu1mxaQm0gC1fBx-axe2aZo2wyFE7y9o0aNU09r-it2aTwrU0JWK2pxK0BVQaw7Cz80y1zqwai2O0kLw-wRw',
                '__comet_req': '7',
                'fb_dtsg': self.dtsg,
                'jazoest': '26179',
                'lsd': 'tP8SLtrdcEQZFS6mkwuP-9',
                '__spin_r': '1017538317',
                '__spin_b': 'trunk',
                '__spin_t': '1729579086',
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'usePolarisFollowMutation',
                'variables': '''{
                            "target_user_id": "'''+target_user_id+'''",
                            "container_module": "profile",
                            "nav_chain": "PolarisFeedRoot:feedPage:2:topnav-link,PolarisProfilePostsTabRoot:profilePage:3:unexpected,PolarisProfilePostsTabRoot:profilePage:4:unexpected"
                            }''',
                'server_timestamps': 'true',
                'doc_id': '7275591572570580',}
        
        follow = self.session.post('https://www.instagram.com/graphql/query',headers=self.headers,data=data).json()
        try:
            return follow['data']['xdt_create_friendship']['friendship_status']['following']
        except TypeError:    
            with open('tetx.txt','w') as f:
                f.write(str(follow))
    def ten(self):
        response = self.session.get('https://www.instagram.com/', headers=self.headers).text
        ten = response.split('"username":"')[1].split('"')[0]
        return ten
    def check_live_ig(self):
        return self.check
class theader:
    pass
     
# a = hustmedia('3XLCuoYOXYU6r3MeSxPuNPR3hFHIDRL9kRAo7rm88rzzMzd').receive_money('46891830529,71214280199,42443313904,70893240913,71583300225,71658272231,55935506353 ',"subcheo","insta")
# # a = facebook('datr=cgvUZhSZqs0CGV-ohLz83ZPh; sb=eAvUZlHieH3Rj03R7SZ8rx1C; ps_l=1; ps_n=1; c_user=61555139777272; fr=1qvlXBf08TEShdiM7.AWWnHY7VRJkgppIoT0ay6xxcbrc.Bnk0Hl..AAA.0.0.Bnk0Hl.AWWEO7-h2wg; xs=1%3A4UIaqdxLuodDRQ%3A2%3A1737552272%3A-1%3A6491%3A%3AAcUyDw-OH_YAJYxThnlONdVFG2NAI1uDq3CUDhP2sA; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1737703909334%2C%22v%22%3A1%7D; wd=508x641').check_live_fb()
# # print(a)
# #datr=cgvUZhSZqs0CGV-ohLz83ZPh; sb=eAvUZlHieH3Rj03R7SZ8rx1C; ps_l=1; ps_n=1; c_user=61555139777272; fr=1c1LZgXV2LFez93Vz.AWWKiWRTAganvmcOnMuTfOinMGE.Bnjhn7..AAA.0.0.Bnjhn7.AWVN88EwLb8; xs=34%3A3rxiBIQH8O5T2A%3A2%3A1737355317%3A-1%3A13846%3A%3AAcWjbKBbs8x0YdCwYtQQ2Lhp9IVsiEoeNgm2CeJVbQ; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1737366014128%2C%22v%22%3A1%7D; wd=508x641
# # a = hustmedia('3XLCuoYOXYU6r3MeSxPuNPR3hFHIDRL9kRAo7rm88rzzMzd').get_list_nick('insa')
# # print(a)
# a= instagram('datr=9GoKZ5rIT1HkOopHKnC4-W04; ig_did=70247F56-0D4D-426B-9B66-A0CC7C7495A8; ig_nrcb=1; ps_l=1; ps_n=1; fbm_124024574287414=base_domain=.instagram.com; mid=Z3o16gALAAHOuAlJETD4CIwUSJg-; csrftoken=PK14AKooINBRiWEV6CEZuKWmo1UAFTnJ; ds_user_id=72286038150; sessionid=72286038150%3AXpluo5XsUHu9IO%3A12%3AAYdHlu5TaHi-Vc7lsqN5UJVERpFz6jS8iUz-scJJEA; wd=720x641; rur="CCO\05472286038150\0541770819724:01f70f2b2c0b6c97f14ff3151bc327528c53b0c70e71b4abbc5d72304738ff047ff648ea"').like('3556869286549662554')
# print(a)
