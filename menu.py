import os
import requests
import sys
import json
import base64
from datetime import datetime
from rich.console import Console
from rich.table import Table
# File lưu key
KEY_FILE = "datavlkey.txt"
console = Console()

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
        return False, "⚠️ Lỗi khi đọc file key!", "", 0

# Kiểm tra key
is_valid, message, key, days_left = check_saved_key()
hidden_key = key[:3] + "..." if key else "Không có key"
console.print(f"[bold yellow]{message}[/bold yellow]")
if not is_valid:
    console.print("\n[bold red]Yêu cầu nhập key mới![/bold red]")
    exit()

# Hiển thị banner
def banner():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Lấy thời gian hiện tại
    expiration_time = (datetime.now() + timedelta(days=days_left)).strftime("%Y-%m-%d %H:%M:%S") if days_left > 0 else "Hết hạn"
    
    console.print("    [bold cyan]----------------------------------------[/bold cyan]")
    console.print("    [bold green]Chào mừng bạn đến với Tool![/bold green]")
    console.print("    [bold cyan]----------------------------------------[/bold cyan]")
    console.print("    [bold green]Admin : 0367742346/0348865758[/bold green]")
    console.print("    [bold green]Chat support: https://zalo.me/g/uaahwq871[/bold green]")
    console.print("    [bold cyan]----------------------------------------[/bold cyan]")
    console.print(f"   [bold white]Key của bạn:[/bold white] {hidden_key}")
    console.print(f"   [bold white]Thời hạn còn lại:[/bold white] {days_left} ngày nữa")
    console.print("    [bold cyan]----------------------------------------[/bold cyan]")

banner()

# Danh sách tool
tools = {
    "Auto Golike": [
        ("1", "Auto TikTok ADB"),
        ("1.1", "TikTok Không Auto Click"),
        ("1.2", "Auto Facebook [PC]"),
        ("1.3", "Auto Instagram"),
        ("1.4", "Auto LinkedIn"),
        ("1.5", "Auto X (Twitter)"),
        ("1.6", "Auto Threads"),
        ("1.7", "Facebook Auto Captcha"),
        ("1.8", "Auto YouTube"),
    ],
    "Auto Hustmedia": [
        ("7", "Auto Facebook, Instagram"),
    ],
    "Trao Đổi Sub": [
        ("2", "TDS TikTok ADB"),
        ("2.1", "Auto Facebook [PC]"),
        ("2.2", "Auto Facebook [PC+Mobile]"),
        ("2.3", "Auto Instagram"),
    ],
    "Tương Tác Chéo": [
        ("3", "TTC Facebook"),
        ("3.1", "TTC Facebook Untiblock"),
    ],
    "Nuôi Facebook VIP": [
        ("4", "Nuôi Facebook [PC]"),
    ],
    "Tiện Ích": [
        ("5", "Reg Profile Facebook"),
        ("5.2", "Unlock Follow TikTok"),
        ("5.3", "Reg Facebook Novery"),
        ("5.4", "Reg Facebook Full Proxy"),
    ],
    "Airdrop Auto": [
        ("6", "Midas No Proxy"),
        ("6.1", "Midas Proxy"),
    ],
}

# Hiển thị menu dạng bảng
def display_menu():
    for category, items in tools.items():
        table = Table(title=f"[bold cyan]{category}[/bold cyan]", header_style="bold white", style="bold blue")
        table.add_column("Lựa Chọn", justify="center", style="bold yellow", width=10)
        table.add_column("Chức Năng", justify="left", style="white")

        for item in items:
            table.add_row(item[0], item[1])

        console.print(table)

display_menu()

# Nhập lựa chọn từ người dùng
chon = str(console.input("[bold magenta]Nhập số:[/bold magenta] "))

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
    console.print("[bold red]⚠️ Sai lựa chọn![/bold red]")
    exit()
