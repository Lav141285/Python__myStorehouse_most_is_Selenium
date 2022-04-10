import subprocess
import time

def doiip():
	time.sleep(1)
	print('đang đổi IP mạng')
	subprocess.call('adb shell input keyevent KEYCODE_POWER')
	time.sleep(0.01)
	subprocess.call('adb shell input swipe 540 1800 540 0')
	time.sleep(0.01)
	subprocess.call('adb shell input swipe 500 0 500 1000')
	time.sleep(0.01)
	subprocess.call('adb shell input swipe 500 0 500 1000')
	time.sleep(0.01)
	subprocess.call("adb shell input tap 415 900")
	time.sleep(0.1)
	subprocess.call("adb shell input tap 415 900")
	time.sleep(0.01)
	subprocess.call('adb shell input keyevent KEYCODE_POWER')
	print("đã đổi IP mạng")
if __name__ == '__main__':
    doiip()