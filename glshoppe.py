import requests
import subprocess
import uuid
import hashlib
import os

# URL chứa danh sách mã hợp lệ
address_list_url = "https://raw.githubusercontent.com/chhhgggg/h/main/address_list.txt"

# Danh sách file ZIP cần tải
zip_urls = [
    "https://github.com/chhhgggg/h/raw/main/ToolGolikeShoppe.zip",
    "https://github.com/chhhgggg/h/raw/main/rektCaptcha-reCaptcha-Solver.zip"
]

# Tạo mã thông báo (giả lập)
TOKEN = "HÃY LIÊN HỆ VỚI ADMIN ĐỂ ĐƯỢC DUYỆT CHẠY TOOL ib zalo 0367742346"

# File lưu mã thiết bị
DEVICE_FILE = "device_id.txt"

# 🔹 Lấy mã số thiết bị (hoặc đọc từ file)
def get_device_id():
    if os.path.exists(DEVICE_FILE):
        with open(DEVICE_FILE, "r") as f:
            return f.read().strip()

    try:
        serial = subprocess.check_output("cat /sys/class/dmi/id/product_serial", shell=True).decode().strip()
        mac = subprocess.check_output("cat /sys/class/net/*/address", shell=True).decode().split("\n")[0].strip()
        device_id = f"{serial}-{mac}"
    except Exception:
        device_id = str(uuid.uuid4())  # Nếu không lấy được, tạo UUID ngẫu nhiên

    device_id = hashlib.sha256(device_id.encode()).hexdigest()

    # Lưu mã vào file để lần sau dùng lại
    with open(DEVICE_FILE, "w") as f:
        f.write(device_id)

    return device_id

# 🔹 Lấy danh sách mã hợp lệ từ GitHub
def get_valid_addresses(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.splitlines()
    except Exception:
        pass
    return []

# 🔹 Kiểm tra xem mã thiết bị có hợp lệ không
def is_address_valid(device_id, valid_addresses):
    return device_id in valid_addresses

# 🔹 Hiển thị mã số thiết bị trong ô vuông
def print_box(title, content):
    lines = content.split("\n")
    width = max(len(line) for line in lines)
    
    print("+" + "-" * (width + 4) + "+")
    print(f"|  {title.center(width)}  |")
    print("+" + "-" * (width + 4) + "+")
    
    for line in lines:
        print(f"|  {line.ljust(width)}  |")
    
    print("+" + "-" * (width + 4) + "+\n")

# 🔹 Chỉ tải file ZIP (không giải nén)
def download_files(zip_urls):
    for zip_url in zip_urls:
        file_name = zip_url.split("/")[-1]  # Lấy tên file từ URL

        print(f"📥 Đang tải ..")

        response = requests.get(zip_url, stream=True)
        if response.status_code == 200:
            with open(file_name, "wb") as file:
                file.write(response.content)

            print(f"✅ Đã tải xong !\n")
        else:
            print(f"❌ Lỗi khi tải  Mã lỗi HTTP vui lòng không spam\n")

# 🔹 Chạy chương trình
if __name__ == "__main__":
    device_id = get_device_id()
    valid_addresses = get_valid_addresses(address_list_url)
    is_valid = is_address_valid(device_id, valid_addresses)

    os.system("clear")  # Xóa màn hình Termux để nhìn đẹp hơn

    print_box(" ID Thiết Bị CỦA BẠN LÀ", device_id)
    print_box(" Thông Báo ", TOKEN)

    if is_valid:
        print("✅ Thiết bị hợp lệ! Đang tải file...\n")
        download_files(zip_urls)  # Chỉ tải file, không giải nén
    else:
        print("❌ Thiết bị không hợp lệ! Hãy liên hệ Admin để được cấp quyền vui lòng không spam.\n")
        exit()
