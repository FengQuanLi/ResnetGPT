from torch.autograd import Variable
import torch
import numpy as np
def 打印抽样数据(数_词表,数据, 输出_分):
    临 = 数据[0]
    欲打印=[数_词表[str(临[i,0])] for i in range(0,临.shape[0])]
    临 = 输出_分.cpu().numpy()
    欲打印2 = [数_词表[str(临[i])] for i in range(0,临.shape[0])]
    print("抽样输出",欲打印)
    print("目标输出", 欲打印2)
    # for i in range(16):
    #     print(数_词表[str(临[i, 0])])

def nopeak_mask(size, device):
    np_mask = np.triu(np.ones((1, size, size)),
    k=1).astype('uint8')
    np_mask =  Variable(torch.from_numpy(np_mask) == 0)

    np_mask = np_mask.cuda(device)
    return np_mask
def 打印测试数据(数_词表,数据, 输人_分,标签):
    临 = 数据[0]
    欲打印=[数_词表[str(临[i])] for i in range(临.size)]
    打印=""
    for i in range(len(欲打印)):
        打印=打印+欲打印[i]



    临 = 输人_分.cpu().numpy()[0]
    欲打印2 = [数_词表[str(临[i])]for i in range(输人_分.size(1))]
    # 欲打印2=str(欲打印2)
    # print("输入：", 欲打印2)
    if 标签==打印:
        return True
    else:
        print(打印)
        return False



    print("输出：",打印)

    # for i in range(16):
    #     print(数_词表[str(临[i, 0])])
def 打印测试数据_A(数_词表,数据, 输人_分):
    if 数据.shape[0]!=0:

        临 = 数据[0]
        欲打印=[数_词表[str(临[i])] for i in range(临.size)]
        打印=""
        for i in range(len(欲打印)):
            打印=打印+欲打印[i]



        临 = 输人_分.cpu().numpy()[0]
        欲打印2 = [数_词表[str(临[i])]for i in range(输人_分.size(1))]
        欲打印2=str(欲打印2)
        #print("输入：", 欲打印2)
        print("输出：",打印)

