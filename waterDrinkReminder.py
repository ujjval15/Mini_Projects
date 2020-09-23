import time
from plyer import notification

if __name__ == "__main__":
    while True:
    
        notification.notify(
            title = "please drink water",
            message = "Madam It's time to ship some water.😜",
            app_icon ="D:\Python_pro\icon.ico",
            timeout=10
        )
        time.sleep(60*60)

