import torch
import torch.nn as nn
import torch.nn.functional as F
import math
import numpy as np
def gelu(x):
    return 0.5 * x * (1 + torch.tanh(math.sqrt(2 / math.pi) * (x + 0.044715 * torch.pow(x, 3))))
class Norm(nn.Module):
    def __init__(self, d_model, eps = 1e-6):
        super().__init__()
    
        self.size = d_model
        
        # create two learnable parameters to calibrate normalisation
        self.alpha = nn.Parameter(torch.ones(self.size))
        self.bias = nn.Parameter(torch.zeros(self.size))
        
        self.eps = eps
    
    def forward(self, x):
        norm = self.alpha * (x - x.mean(dim=-1, keepdim=True)) \
        / (x.std(dim=-1, keepdim=True) + self.eps) + self.bias
        return norm

def attention(q, k, v, d_k, mask=None, dropout=None):
    
    scores = torch.matmul(q, k.transpose(-2, -1)) /  math.sqrt(d_k)
    
    if mask is not None:
        mask = mask.unsqueeze(1)
        scores = scores.masked_fill(mask == 0, -1e9)
    
    scores = F.softmax(scores, dim=-1)
    
    if dropout is not None:
        scores = dropout(scores)
        
    output = torch.matmul(scores, v)
    return output

class MultiHeadAttention(nn.Module):
    def __init__(self, heads, d_model, dropout = 0.1):
        super().__init__()
        
        self.d_model = d_model
        self.d_k = d_model // heads
        self.h = heads
        
        self.q_linear = 全连接层(d_model, d_model)
        self.v_linear = 全连接层(d_model, d_model)
        self.k_linear = 全连接层(d_model, d_model)
        
        self.dropout = nn.Dropout(dropout)
        self.out = 全连接层(d_model, d_model)
    
    def forward(self, q, k, v, mask=None):
        
        bs = q.size(0)
        
        # perform linear operation and split into N heads
        k = self.k_linear(k).view(bs, -1, self.h, self.d_k)
        q = self.q_linear(q).view(bs, -1, self.h, self.d_k)
        v = self.v_linear(v).view(bs, -1, self.h, self.d_k)
        
        # transpose to get dimensions bs * N * sl * d_model
        k = k.transpose(1,2)
        q = q.transpose(1,2)
        v = v.transpose(1,2)
        

        # calculate attention using function we will define next
        scores = attention(q, k, v, self.d_k, mask, self.dropout)
        # concatenate heads and put through final linear layer
        concat = scores.transpose(1,2).contiguous()\
        .view(bs, -1, self.d_model)
        output = self.out(concat)
    
        return output

class FeedForward(nn.Module):
    def __init__(self, d_model, d_ff=2048, dropout = 0.1):
        super().__init__() 
    
        # We set d_ff as a default to 2048
        self.linear_1 = 全连接层(d_model, d_ff)
        self.dropout = nn.Dropout(dropout)
        self.linear_2 = 全连接层(d_ff, d_model)
    
    def forward(self, x):
        x = self.dropout(gelu(self.linear_1(x)))
        x = self.linear_2(x)
        return x
class 全连接层(nn.Module):
    def __init__(self,输入_接口, 输出_接口):
        super().__init__()
        np.random.seed(1)
        self.weight = nn.Parameter(torch.FloatTensor(np.random.uniform(-1/np.sqrt(输入_接口), 1/np.sqrt(输入_接口), (输入_接口, 输出_接口))))
        self.bias = nn.Parameter(torch.FloatTensor(np.random.uniform(-1/np.sqrt(输入_接口), 1/np.sqrt(输入_接口), 输出_接口)))


    def forward(self, x):
        输出=torch.matmul(x,self.weight)
        输出=输出+self.bias
        return 输出