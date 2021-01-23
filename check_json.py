import json
from 运行辅助 import *
import os
import time

## Json file check
# with open('./json/词_数表.json', 'rb') as f:
#     data = json.load(f)
#     print(data)
# with open('./json/数_词表.json', 'rb') as f:
#     data = json.load(f)
#     print(data)
# with open('./json/名称_编号.json', 'rb') as f:
#     data = json.load(f)
#     print(data)
with open('./json/名称_操作.json', 'rb') as f:
    data = json.load(f)
    print(data)


## On-sereen Pointer Visualization
# _DEVICE_ID = 'db5fece5'
# 窗口名称="MIX 2S"
# 设备 = MyMNTDevice(_DEVICE_ID)
# 设备.发送('d 0 1860 930 100\nc\nu 0\nc\n')
# print('Button pressed.')
# while True:
#     设备.发送('d 1 1000 2100 100\nc\nu 0\nc\n')
#     # 设备.发送('d 0 1860 930 100\nc\nu 0\nc\n')
#     time.sleep(1)


## Establish a local json file for the local cell phone layout in game
## d <contact> <x> <y> <pressure>
## m <contact> <x> <y> <pressure>
## see more touch commands in minitouch repo: https://github.com/openstf/minitouch
dict_layout = {
    # coordination in Android adb: (X,Y)
    # '攻击': 'd 0 1860 930 100\nc\nu 0\nc\n',
    # '补刀': 'd 0 1687 988 100\nc\nu 0\nc\n',
    # '推塔': 'd 0 1950 775 100\nc\nu 0\nc\n',
    #
    # '一技能': 'd 0 1532 952 100\nc\nu 0\nc\n',
    # '二技能': 'd 0 1673 761 100\nc\nu 0\nc\n',
    # '三技能': 'd 0 1857 645 100\nc\nu 0\nc\n',
    # '召唤师技能': 'd 0 1373 965 100\nc\nu 0\nc\n',
    #
    # '回城': 'd 0 1090 962 100\nc\nu 0\nc\n',
    #
    # '发起进攻': 'd 0 2099 155 100\nc\nu 0\nc\n',
    # '发起撤退': 'd 0 2108 245 100\nc\nu 0\nc\n',
    # '发起集合': 'd 0 2100 338 100\nc\nu 0\nc\n',
    #
    # '上移': 'd 1 430 840 300\nc\nm 1 430 710 100\nc\n',  # controller center -> moving end point
    # '右移': 'd 1 430 840 300\nc\nm 1 560 840 100\nc\n',
    # '下移': 'd 1 430 840 300\nc\nm 1 430 970 100\nc\n',
    # '左移': 'd 1 430 840 300\nc\nm 1 300 840 100\nc\n',
    # '左上移': 'd 1 430 840 300\nc\nm 1 330 740 100\nc\n',
    # '左下移': 'd 1 430 840 300\nc\nm 1 330 940 100\nc\n',
    # '右下移': 'd 1 430 840 300\nc\nm 1 530 940 100\nc\n',
    # '右上移': 'd 1 430 840 300\nc\nm 1 530 740 100\nc\n',
    #
    # '移动停': 'u 1\nc\n',
    # '恢复': 'd 0 1225 985 100\nc\nu 0\nc\n',
    #############################################
    # coordination in minitouch (X,Y) -> (1080-Y,X)
    '攻击': 'd 0 150 1860 100\nc\nu 0\nc\n',  # 930(150)  Y(1080-Y, i.e. new 'X')
    '补刀': 'd 0 92 1687 100\nc\nu 0\nc\n',  # 988(92)
    '推塔': 'd 0 305 1950 100\nc\nu 0\nc\n',  # 775(305)

    '一技能': 'd 0 128 1532 100\nc\nu 0\nc\n',  # 952(128)
    '二技能': 'd 0 319 1673 100\nc\nu 0\nc\n',  # 761(319)
    '三技能': 'd 0 435 1857 100\nc\nu 0\nc\n',  # 645(435)
    '召唤师技能': 'd 0 115 1373 100\nc\nu 0\nc\n',  # 965(115)

    '回城': 'd 0 118 1090 100\nc\nu 0\nc\n',  # 962(118)

    '发起进攻': 'd 0 925 2099 100\nc\nu 0\nc\n',  # 155(925)
    '发起撤退': 'd 0 835 2108 100\nc\nu 0\nc\n',  # 245(835)
    '发起集合': 'd 0 742 2100 100\nc\nu 0\nc\n',  # 338(742)

    '上移': 'd 1 240 430 300\nc\nm 1 370 430 100\nc\n',  # controller center -> moving end point  # 840(240) 710(370)
    '右移': 'd 1 240 430 300\nc\nm 1 240 560 100\nc\n',  # 840 840(240)
    '下移': 'd 1 240 430 300\nc\nm 1 110 430 100\nc\n',  # 840 970(110)
    '左移': 'd 1 240 430 300\nc\nm 1 240 300 100\nc\n',  # 840 840(240)
    '左上移': 'd 1 240 430 300\nc\nm 1 340 330 100\nc\n',  # 840 740(340)
    '左下移': 'd 1 240 430 300\nc\nm 1 140 330 100\nc\n',  # 840 940(140)
    '右下移': 'd 1 240 430 300\nc\nm 1 140 530 100\nc\n',  # 840 940(140)
    '右上移': 'd 1 240 430 300\nc\nm 1 340 530 100\nc\n',  # 840 740(340)

    '移动停': 'u 1\nc\n',  # 930
    '恢复': 'd 0 1225 985 100\nc\nu 0\nc\n'  # 930
}

# test button press
# while True:
#     设备.发送('d 1 240 430 100\nc\nu 0\nc\n')
#     # 设备.发送('d 1 240 430 300\nc\nm 1 370 430 100\nc\n')
#     time.sleep(1)

with open('./json/local_layout.json', 'w') as json_file:
    json.dump(dict_layout, json_file)

with open('./json/local_layout.json', 'rb') as f:
    data = json.load(f)
    print(data)


