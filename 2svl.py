import time
import subprocess
import os
from datetime import datetime
from PIL import Image

sz=1
def capture_image():
    try:
        current_time = datetime.now().strftime("%d-%m-%y_%H-%M-%S")  # Lấy thời gian hiện tại với định dạng "dd-mm-yy:hh-mm-ss"
        filename = f"photos/image_{current_time}.jpg"  # Tên tệp ảnh với thời gian chụp và đường dẫn thư mục
        subprocess.run(["termux-camera-photo", filename], capture_output=True, check=True)  # Gọi lệnh termux-camera-photo để chụp ảnh và lưu vào tệp với tên đã định dạng

        # Mở ảnh bằng Pillow
        image = Image.open(filename)

        # Diều chỉnh chất lượng và kích thước ảnh
        image = image.resize((640*sz, 480*sz))  # Điều chỉnh kích thước ảnh
        image.save(filename, "JPEG", quality=50)  # Lưu ảnh lại với chất lượng 50 (giảm chất lượng để nén mạnh hơn)

#        # Chuyển đổi ảnh sang định dạng WebP
#        webp_filename = f"photos/image_{current_time}.webp"  # Tên tệp ảnh WebP với đường dẫn thư mục
#        image.save(webp_filename, "WebP", quality=10)  # Cài đặt chất lượng ảnh WebP
#
#        # Nén ảnh để có kích thước tệp chỉ còn 5KB
#        subprocess.run(["cwebp", "-q", "10", webp_filename, "-o", "photos/compressed.webp"])  # Sử dụng công cụ cwebp để nén ảnh với đường dẫn thư mục
#
#        # Xóa tệp JPG
#        os.remove(filename)
#
        print("Đã chụp và nén ảnh thành công")
    except subprocess.CalledProcessError as e:
        print("Lỗi khi chụp ảnh:", e.stderr.decode())
    except Exception as e:
        print("Lỗi khi lưu ảnh:", str(e))
        time.sleep(5)
while True:
    capture_image()
    time.sleep(5)  # Chờ 1 giây trước khi chụp ảnh tiếp theo
