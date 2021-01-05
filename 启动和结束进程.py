
import os

os.system('taskkill /IM scrcpy.exe /F')
os.system('taskkill /IM adb.exe /F')
os.system("scrcpy --max-size 960")