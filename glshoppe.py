import requests
import zipfile
import io

# Danh sách URL ZIP từ GitHub
zip_urls = [
    "https://github.com/chhhgggg/h/blob/main/ToolGolikeShoppe.zip",
    "https://github.com/user/repo2/archive/refs/heads/main.zip"
]

# Lặp qua từng URL để tải và giải nén
for i, zip_url in enumerate(zip_urls, start=1):
    response = requests.get(zip_url, stream=True)

    if response.status_code == 200:
        folder_name = f"repo_{i}"  # Tạo tên thư mục riêng cho từng repo
        with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_ref:
            zip_ref.extractall(folder_name)
        print(f"Tải và giải nén {zip_url} thành công vào thư mục {folder_name}!")
    else:
        print(f"Lỗi khi tải {zip_url}!"
