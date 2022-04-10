import subprocess,time


subprocess.call('adb shell input keyevent KEYCODE_POWER')
time.sleep(0.01)
subprocess.call('adb shell input swipe 540 1800 540 0')
time.sleep(0.01)
subprocess.call('adb shell input swipe 500 0 500 1000')
time.sleep(0.01)
subprocess.call('adb shell input swipe 500 0 500 1000')
time.sleep(0.01)
subprocess.call("adb shell input tap 960 1400")
time.sleep(0.01)
subprocess.call("adb shell input tap 930 600")
time.sleep(0.01)
subprocess.call('adb shell input tap 960 1000')
time.sleep(0.01)
subprocess.call('adb shell input tap 960 655')
time.sleep(2)
subprocess.call('adb shell input tap 860 1910')
time.sleep(0.01)
subprocess.call('adb shell input swipe 540 1200 540 0')
time.sleep(0.01)
subprocess.call('adb shell input tap 510 1910')
time.sleep(0.01)
subprocess.call('adb shell input keyevent KEYCODE_POWER')


