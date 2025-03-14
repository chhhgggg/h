import os
import requests
import sys
import json
from datetime import datetime, timedelta
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad
import hmac
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
import dns.resolver
import socket
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from colorama import Fore, Style, init
from rich.progress import Progress
import time
import random
import threading
import psutil
import signal

console = Console()
init(autoreset=True)

# Xóa file "requests.py" nếu tồn tại
current_directory = os.getcwd()
file_path = os.path.join(current_directory, "requests.py")
if os.path.exists(file_path):
    try:
        os.remove(file_path)
    except OSError:
        pass

# Hàm kiểm tra và vô hiệu hóa proxy
def check_http_toolkit():
    if os.environ.get("HTTP_TOOLKIT_ACTIVE") == "true":
        return True
    for ev in ["SSL_CERT_FILE", "NODE_EXTRA_CA_CERTS", "PATH"]:
        if ev in os.environ and "httptoolkit" in os.environ[ev].lower():
            return True
    for px in ["HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"]:
        if px in os.environ and "127.0.0.1:8000" in os.environ[px]:
            return True
    try:
        h = requests.get("https://example.com", timeout=5).headers
        if any("HTTP-Toolkit" in h.get(x, "") for x in ["Server", "Via", "X-Powered-By"]):
            return True
    except:
        pass
    return False

def is_mitmproxy_or_httptoolkit_running():
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            process_name = process.info['name']
            cmdline = ' '.join(process.info['cmdline'] or [])
            if 'proxy' in process_name.lower() or 'mitmproxy' in process_name.lower() or 'mitmweb' in process_name.lower() or 'mitmdump' in cmdline.lower():
                return process.info['pid'], 'Mitmproxy'
            if 'httptoolkit' in process_name.lower() or 'httptoolkit' in cmdline.lower():
                return process.info['pid'], 'HTTP Toolkit'
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return None, None

def kill_process(pid, process_name):
    try:
        os.kill(pid, signal.SIGTERM)
    except Exception:
        pass

def check_mitmproxy_and_httptoolkit():
    max_attempts = 3
    attempt = 0
    while attempt < max_attempts:
        pid, process_name = is_mitmproxy_or_httptoolkit_running()
        if pid:
            kill_process(pid, process_name)
            time.sleep(2)
        else:
            break
        attempt += 1

# Cấu hình DNS Resolver
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

TOKEN_LINK4M = "1f06c470cc45a0d11ef440cb959c716466487b6b46c78b099fe7d1804e573235"
KEY_GITHUB_URL = "https://raw.githubusercontent.com/QuyKedo/key/refs/heads/main/key.txt"
KEY_FILE = "datavlk.enc"
SECRET_KEY = b'KEDO_SECRET_2023_16BYTE_KEY!!!!!'
HMAC_KEY = b'KEDO_HMAC_KEY_2023'

def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        return response.json().get('ip', 'Unknown')
    except requests.ConnectionError:
        console.print(Panel("[red]Không thể lấy địa chỉ IP! Kiểm tra kết nối mạng.[/red]", title="Lỗi"))
        sys.exit()

def generate_daily_key(ip_address):
    date = datetime.now()
    ip_numbers = ''.join(filter(str.isdigit, ip_address))
    nonce = get_random_bytes(8).hex()
    key_base = f"KEDOTOL{ip_numbers}{date.day}{date.month}{date.year}{nonce}"
    key = hashlib.sha256(key_base.encode()).hexdigest()
    return key, nonce

def get_shortened_link_link4m(url):
    try:
        api_url = f"https://yeumoney.com/QL_api.php?token={TOKEN_LINK4M}&format=json&url={url}"
        params = {"api": TOKEN_LINK4M, "url": url}
        response = requests.get(api_url, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success":
                return data.get("shortenedUrl")
    except Exception:
        console.print(Panel("[red]Lỗi khi rút gọn link![/red]", title="Lỗi"))
    return None

def get_keys_from_github():
    try:
        response = requests.get(KEY_GITHUB_URL, timeout=5)
        if response.status_code == 200:
            lines = response.text.strip().split("\n")
            keys = {}
            for line in lines:
                parts = line.split("-")
                if len(parts) == 3 and parts[2].strip() == "KEDO":
                    key_name = parts[0].strip()  # Key1, Key2, ...
                    date_str = parts[1].strip()  # ngày/tháng/năm
                    try:
                        # Chuyển định dạng ngày/tháng/năm thành datetime
                        expiration_date = datetime.strptime(date_str, "%d/%m/%Y")
                        # Tạo key dạng hash từ thông tin
                        key_base = f"KEDOTOL{key_name}{expiration_date.day}{expiration_date.month}{expiration_date.year}"
                        hashed_key = hashlib.sha256(key_base.encode()).hexdigest()
                        keys[hashed_key] = expiration_date.isoformat()
                    except ValueError:
                        continue
            return keys
    except requests.ConnectionError:
        console.print(Panel("[red]Kiểm tra kết nối mạng.[/red]", title="Lỗi"))
    return {}

def encrypt_data(data):
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC)
    data_str = json.dumps(data).encode('utf-8')
    ct_bytes = cipher.encrypt(pad(data_str, AES.block_size))
    iv = cipher.iv
    hmac_value = hmac.new(HMAC_KEY, ct_bytes, hashlib.sha256).digest()
    return iv + ct_bytes + hmac_value

def decrypt_data(encrypted_data):
    try:
        iv = encrypted_data[:16]
        ct = encrypted_data[16:-32]
        hmac_value = encrypted_data[-32:]
        computed_hmac = hmac.new(HMAC_KEY, ct, hashlib.sha256).digest()
        if not hmac.compare_digest(hmac_value, computed_hmac):
            return None
        cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return json.loads(pt.decode('utf-8'))
    except Exception:
        return None

def save_key_locally(key, ip_address, nonce):
    date = datetime.now()
    data = {
        "key": key,
        "ip_address": ip_address,
        "created_at": date.isoformat(),
        "nonce": nonce
    }
    encrypted_data = encrypt_data(data)
    with open(KEY_FILE, "wb") as file:
        file.write(encrypted_data)

def load_key_locally(ip_address, github_keys):
    if os.path.exists(KEY_FILE):
        try:
            with open(KEY_FILE, "rb") as file:
                encrypted_data = file.read()
            data = decrypt_data(encrypted_data)
            if data is None:
                console.print(Panel("[red]File key đã bị thay đổi trái phép hoặc lỗi![/red]", title="Cảnh báo"))
                return None, None
            
            stored_key = data.get("key")
            stored_ip = data.get("ip_address")
            created_at = datetime.fromisoformat(data.get("created_at"))
            nonce = data.get("nonce")

            if stored_ip != ip_address:
                console.print(Panel("[red]File key không hợp lệ với thiết bị này![/red]", title="Cảnh báo"))
                return None, None

            date = datetime.now()
            daily_key = hashlib.sha256(f"KEDOTOL{''.join(filter(str.isdigit, ip_address))}{created_at.day}{created_at.month}{created_at.year}{nonce}".encode()).hexdigest()
            if stored_key == daily_key:
                if (date - created_at).total_seconds() < 86400:  # Hết hạn sau 24h
                    return stored_key, "Hết hạn 12h đêm nay"

            if stored_key in github_keys:
                expiration_date = datetime.fromisoformat(github_keys[stored_key])
                if date < expiration_date:
                    remaining_time = expiration_date - date
                    hours = remaining_time.total_seconds() // 3600
                    minutes = (remaining_time.total_seconds() % 3600) // 60
                    return stored_key, f"Hết hạn lúc {expiration_date.strftime('%H:%M:%S %d/%m/%Y')} (còn {int(hours)} giờ {int(minutes)} phút)"

        except Exception as e:
            console.print(Panel(f"[red]Lỗi khi đọc file key: {str(e)}[/red]", title="Cảnh báo"))
    return None, None

def validate_key(input_key, ip_address, github_keys):
    date = datetime.now()
    daily_key, nonce = generate_daily_key(ip_address)
    if input_key == daily_key:
        return True, "Hết hạn 12h đêm nay", nonce
    
    if input_key in github_keys:
        expiration_date = datetime.fromisoformat(github_keys[input_key])
        if date < expiration_date:
            remaining_time = expiration_date - date
            hours = remaining_time.total_seconds() // 3600
            minutes = (remaining_time.total_seconds() % 3600) // 60
            return True, f"Hết hạn lúc {expiration_date.strftime('%H:%M:%S %d/%m/%Y')} (còn {int(hours)} giờ {int(minutes)} phút)", None
    
    return False, None, None

def xac_thuc_va_chay_tool():
    console.print(Panel("[bold green]Đang khởi động hệ thống xác thực...[/bold green]", title="KEDO Tool", border_style="cyan"))
    ip_address = get_ip_address()
    
    daily_key, nonce = generate_daily_key(ip_address)
    url = f'https://kedotool.github.io/kedotool/?key={daily_key}'
    link4m_short_url = get_shortened_link_link4m(url)
    github_keys = get_keys_from_github()
    
    stored_key, expiration_info = load_key_locally(ip_address, github_keys)
    if stored_key:
        console.print(Panel(f"[bold green]Đã tìm thấy key hợp lệ đã lưu![/bold green]\n{expiration_info}", title="Xác thực", border_style="green"))
        run_tool_menu()
        return
    
    console.print(Panel("[bold yellow]Nhập Key Để Dùng Tool[/bold yellow]", title="Yêu cầu", border_style="yellow"))
    console.print(f"[cyan]Vượt link để lấy key ngày:[/cyan] [bold magenta]{link4m_short_url}[/bold magenta]")
    console.print("[yellow]Key ngày sẽ hết hạn sau 12h đêm hôm nay.[/yellow]")
    console.print("[yellow]Nếu bạn có key VIP, nhập vào để sử dụng.[/yellow]")

    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        try:
            keynhap = console.input("[bold cyan]Nhập Key: [/bold cyan]").strip()
            attempts += 1
            
            is_valid, expiration_info, nonce = validate_key(keynhap, ip_address, github_keys)
            if is_valid:
                console.print(Panel(f"[bold green]Key hợp lệ![/bold green]\n{expiration_info}", title="Thành công", border_style="green"))
                save_key_locally(keynhap, ip_address, nonce)
                break
            else:
                remaining = max_attempts - attempts
                if remaining > 0:
                    console.print(Panel(f"[red]Key sai! Còn {remaining} lần thử.[/red]", title="Lỗi", border_style="red"))
                else:
                    console.print(Panel("[red]Đã vượt quá số lần thử. Vui lòng thử lại sau.[/red]", title="Lỗi", border_style="red"))
                    sys.exit(1)
                    
        except KeyboardInterrupt:
            console.print(Panel("[red]Đã hủy quá trình xác thực.[/red]", title="Hủy", border_style="red"))
            sys.exit(1)
    
    if attempts >= max_attempts:
        console.print(Panel("[red]Không thể xác thực key. Vui lòng thử lại sau.[/red]", title="Lỗi", border_style="red"))
        sys.exit(1)

    

def run_tool_menu():
    console.print(Panel(
        Text("Chào mừng bạn đến với KEDO-Tool!\n"
             "Admin: 0367742346/0348865758\n"
             "Chat support: https://zalo.me/g/uaahwq871\n"
             "Key ngày hết hạn 12h đêm\n"
             "Nếu bạn cần mua key VIP ib ngay 0367742346\n"
             "Giá key: 10k/tuần - 40k/tháng\n"
             "Code được anti crack By Bảo Ngọc\n"
             "Chúng tôi là KEDO - nhóm 3 thành viên thích code tool", style="bold green"),
        title="KEDO Tool", border_style="cyan"
    ))
    
    tools = {
        "Auto Golike": [
            ("1",   "TikTok ADB[Giả lập+Mobile]"),
            ("1.1", "TikTok Không Auto Click"),
            ("0.1", "Tiktok Auto Cookie(PC)"),
            ("1.2", "Facebook [PC]"),
            ("1.3", "Instagram[Giả lập+Mobile]"),
            ("1.4", "LinkedIn[Giả lập+Mobile]"),
            ("1.5", "X [Giả lập+Mobile]"),
            ("1.6", "Threads[Giả lập+Mobile]"),
            ("1.7", "Facebook Auto Captcha[PC]"),
            ("1.8", "YouTube[Giả lập+Mobile]"),
            ("1.9", "Shoppe [All]"),
            ("0", "Snapchat ADB"),
            ("0.2", "Snapchat Không Auto Click"),
        ],
        "Auto Hustmedia": [
            ("7", "Facebook, Instagram[App Lỏ Tool sẽ up tt]"),
        ],
        "Trao Đổi Sub": [
            ("2", "TDS TikTok ADB"),
            ("2.4", "Tiktok Auto Cookie (PC)"),
            ("2.1", "Auto Facebook Sele[PC]"),
            ("2.2", "Facebook [PC+Mobile]"),
            ("2.3", "Auto Instagram[PC+Mobile]"),
        ],
        "Tương Tác Chéo": [
            ("3", "TTC Facebook[PC+Mobile]"),
            ("3.1", "TTC Facebook Sele[PC]"),
            ("3.2", "TTC Facebook Sele Crack[PC]"),
        ],
        "Nuôi Facebook VIP": [
            ("4", "Nuôi Facebook [PC]"),
        ],
        "Tiện Ích": [
            ("5", "Reg Profile Facebook"),
            ("5.1", "Buff View Zefoy [PC]"), 
            ("5.2", "Unlock Follow TikTok[Selenium-PC]"),
            ("5.3", "Reg Facebook Novery"),
            ("5.4", "Reg Facebook Full Proxy"),
            ("5.5", "Spam SMS (CÓ API XỊN NHỚ SHARE)"),
            ("5.6", "DDOS WEB (CÓ API XỊN NHỚ SHARE)"),
        ],
        "Airdrop Auto": [
            ("6", "Midas No Proxy"),
            ("6.1", "Midas Proxy"),
        ],
    }

    def display_menu():
        for category, items in tools.items():
            table = Table(title=f"[bold cyan]{category}[/bold cyan]", header_style="bold white", style="bold blue")
            table.add_column("Lựa Chọn", justify="center", style="bold yellow", width=10)
            table.add_column("Chức Năng", justify="left", style="white")
            for item in items:
                table.add_row(item[0], item[1])
            console.print(table)

    display_menu()

    chon = console.input("[bold magenta]Nhập số: [/bold magenta]")

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
        '7': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/menuhust.py',
        '1.9': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/glshoppe.py',
        '0': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/glsnap.py',
        '0.1': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/gl_ttck.py',
        '0.2': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/glsnapnoclick.py',
        '2.4': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/tds_ttck.py',
        '5.5': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/spamsms.py',
        '5.6': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/ddos.py',
        '5.1': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/zefoy.py',
        '3.2': 'https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/ttccrack.py'
    }
    
    if chon in script_urls:
        exec(requests.get(script_urls[chon]).text)
    else:
        console.print(Panel("[red]⚠️ Sai lựa chọn![/red]", title="Lỗi", border_style="red"))
        sys.exit()

if __name__ == '__main__':
    xac_thuc_chay_tool()
    tool_menu()