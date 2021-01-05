import json
import numpy as np
def 读取训练数据(路径):
    输入表单 = []
    输出表单 = []
    with open(路径, encoding='utf-8') as f:
        while True:
            行 = f.readline()
            if not 行:
                break
            json_行 = json.loads(行)

            内容 = json_行['内容______']
            内容_输入 = 内容['输入______']
            内容_输出 = 内容['输出______']
            #这里的数据还得进行分割先暂时分割成16份吧
            单元长度 = len(内容_输入)//16
            for i in range(16):
                #print(内容_输入[i*单元长度:(i+1)*单元长度])
                输入表单.append(内容_输入[i*单元长度:(i+1)*单元长度])
                输出表单.append(内容_输出[i*单元长度:(i+1)*单元长度])
    return 输入表单, 输出表单

def 写出词标号引索(总词表,  词_数表路径, 数_词表路径):
    print("正在写出词的标号引索数据可能需要较长时间")
    标号_到_字符 = {}
    字符_到_标号 = {}
    标号_字符 = []

    # 标号_到_字符 = list(set(总表单))
    i = 0
    j = 0
    for 词表 in 总词表:
        j = j + 1
        for 字符 in 词表:


            if 字符 not in 标号_字符:
                标号_字符.append(字符)
                字符_到_标号[字符] = i
                标号_到_字符[i] = 字符
                i = i + 1
        if j % 10000 == 0:
            print(i, 标号_到_字符[i - 1],  j/len(总词表))

    #print(标号_到_字符[1], 标号_到_字符[111], len(标号_到_字符))
    with open(词_数表路径, 'w', encoding='utf-8') as f:
        json.dump(字符_到_标号, f, ensure_ascii=False)
    with open(数_词表路径, 'w', encoding='utf-8') as f:
        json.dump(标号_到_字符, f, ensure_ascii=False)

def 读出引索(词_数表路径, 数_词表路径):
    with open(词_数表路径, encoding='utf-8') as f:
        词_数表= json.load(f)

    with open(数_词表路径, encoding='utf-8') as f:
        数_词表 = json.load(f)
    return 词_数表, 数_词表

def 生成训练用numpy数组(输入表单, 词_数表, numpy数组路径):
    表_1 = []

    表_2 = []

    i = 0
    临 = ''
    for 表单 in 输入表单:
        表_3 = []
        for 字符 in 表单:
            if (u'\u0041' <= 字符 <= u'\u005a') or (u'\u0061' <= 字符 <= u'\u007a'):
                if 临 == '':

                    临 = 字符
                else:
                    临 = 临 + 字符
            else:

                if 临 == '':

                    if 字符.lower() in 词_数表:

                         表_3.append(词_数表[字符.lower()])
                    else:
                        表_3.append(14999)
                else:
                    if 临.lower() in 词_数表:

                        表_3.append(词_数表[临.lower()])
                    else:
                        表_3.append(14999)
                    临 = ''
                    if 字符.lower() in 词_数表:

                        表_3.append(词_数表[字符.lower()])
                    else:
                        表_3.append(14999)
        if 临 != '':
            if 临.lower() in 词_数表:

                表_3.append(词_数表[临.lower()])
            else:
                表_3.append(14999)
            临 = ''

        if len(表_3) != 667:
            # 表_1.append(np.array(表_3[0:-1]))
            # 表_2.append(np.array(表_3[1:]))
            print(表_3)
        else:

            表_1.append(np.array(表_3[0:-1]))
            表_2.append(np.array(表_3[1:]))
        if i % 1000 == 0:
            print("数据转化为numpy数组完成度百分比{}".format(i / len(输入表单) * 100))
        i = i + 1
    print("数据转化为numpy数组完成。")

    输入np = np.array(表_1)
    输出np = np.array(表_2)
    np.savez(numpy数组路径, 输出np=输出np, 输入np=输入np)


def 生成测试用numpy数组(输入表单, 词_数表):
    表_1 = []

    for 字符 in 输入表单:
        if 字符.lower() in 词_数表:
            表_1.append(词_数表[字符])
        else:
            表_1.append(14999)
    输入np = np.array(表_1)
    return (输入np)
def 生成训练用numpy数组_A(输入表单,  词_数表, numpy数组路径):
    表_1 = []

    表_2 = []

    i=0
    临=''
    for 表单 in 输入表单:
        表_3=[]
        for 字符 in 表单:
            if (u'\u0041' <= 字符 <= u'\u005a') or (u'\u0061' <= 字符 <= u'\u007a'):
                if 临 == '':

                    临 = 字符
                else:
                    临 = 临 + 字符
            else:

                if 临 == '':

                    if 字符.lower() in 词_数表:
                        if 字符 != ' ':
                            表_3.append(词_数表[字符.lower()])
                    else:
                        表_3.append(14999)
                else:
                    if 临.lower() in 词_数表:
                        if 临 != ' ':
                            表_3.append(词_数表[临.lower() ])
                    else:
                        表_3.append(14999)
                    临=''
                    if 字符.lower() in 词_数表:
                        if 字符 != ' ':
                            表_3.append(词_数表[字符.lower() ])
                    else:
                        表_3.append(14999)
        if 临!='':
            if 临.lower() in 词_数表:
                if 字符 != ' ':
                    表_3.append(词_数表[临.lower() ])
            else:
                表_3.append(14999)
            临 = ''


        if len(表_3)!=667:
            #表_1.append(np.array(表_3[0:-1]))
            #表_2.append(np.array(表_3[1:]))
            print(表_3)
        else:

            表_1.append(np.array(表_3[0:-1]))
            表_2.append(np.array(表_3[1:]))
        if i % 1000 == 0:
            print("数据转化为numpy数组完成度百分比{}".format(i/len(输入表单)*100))
        i = i + 1
    print("数据转化为numpy数组完成。")


    输入np = np.array(表_1)
    输出np = np.array(表_2)
    np.savez(numpy数组路径, 输出np=输出np, 输入np=输入np)


def 读取训练数据_A(路径):
    输入表单 = []
    with open(路径, encoding='utf-8') as f:
        while True:
            行 = f.readline()
            if not 行:
                break
            json_行 = json.loads(行)

            内容 = json_行['input']
            输入表单.append(内容)

    return 输入表单
def 生成测试用numpy数组_A(输入表单, 词_数表):
    表_3 = []
    临 = ''

    for 字符 in 输入表单:
        if 字符.lower() in 词_数表:
            if (u'\u0041' <= 字符 <= u'\u005a') or (u'\u0061' <= 字符 <= u'\u007a'):
                if 临 == '':

                    临 = 字符
                else:
                    临 = 临 + 字符
            else:

                if 临 == '':

                    if 字符.lower() in 词_数表:
                        if 字符.lower() != ' ':
                            表_3.append(词_数表[字符.lower()])
                    else:
                        表_3.append(14999)
                else:
                    if 临.lower() in 词_数表:
                        if 临.lower() != ' ':

                            表_3.append(词_数表[临.lower()])
                    else:
                        表_3.append(14999)
                    临 = ''
                    if 字符.lower() in 词_数表:
                        if 字符.lower() != ' ':

                            表_3.append(词_数表[字符.lower()])
                    else:
                        表_3.append(14999)
    输入np = np.array(表_3)
    return (输入np)