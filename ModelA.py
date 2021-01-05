import torch
import torch.nn as nn 
from Layers import  DecoderLayer
from Embed import Embedder, PositionalEncoder
from Sublayers import Norm, 全连接层
import copy
import os.path
import torchvision
def get_clones(module, N):
    return nn.ModuleList([copy.deepcopy(module) for i in range(N)])


    
class Decoder(nn.Module):
    def __init__(self, vocab_size, d_model, N, heads, dropout, 最大长度=1024):
        super().__init__()
        self.N = N
        self.embed = Embedder(vocab_size, d_model)
        self.embedP = Embedder(最大长度, d_model)
       # self.pe = PositionalEncoder(d_model, dropout=dropout)
        self.layers = get_clones(DecoderLayer(d_model, heads, dropout), N)
        self.norm = Norm(d_model)
    def forward(self,图向量,操作 ,trg_mask):
        position = torch.arange(0, 图向量.size(1), dtype=torch.long,
                                    device=图向量.device)


        x = 图向量+self.embedP(position)+self.embed(操作)*0



        for i in range(self.N):
            x = self.layers[i](x,  trg_mask)
        return self.norm(x)

class Transformer(nn.Module):
    def __init__(self,  trg_vocab, d_model, N, heads, dropout,图向量尺寸=6*6*2048):
        super().__init__()
        self.图转= 全连接层(图向量尺寸,d_model)



        self.decoder = Decoder(trg_vocab, d_model, N, heads, dropout)
        self.out = 全连接层(d_model, trg_vocab)

    def forward(self, 图向量 ,操作, trg_mask):
        图向量=self.图转(图向量)

        d_output = self.decoder(图向量,操作 , trg_mask)
        output = self.out(d_output)
        return output

class RESNET_Transformer(nn.Module):
    def __init__(self,  trg_vocab, d_model, N, heads, dropout,图向量尺寸=1000):
        super().__init__()
        self.图转= 全连接层(图向量尺寸,d_model)

        self.resnet = torchvision.models.resnet18(pretrained=False).eval().requires_grad_(True)

        self.decoder = Decoder(trg_vocab, d_model, N, heads, dropout)
        self.out = 全连接层(d_model, trg_vocab)

    def forward(self, 图向量 , trg_mask):
        x=self.resnet(图向量).unsqueeze(0)
        图向量=self.图转(x)

        d_output = self.decoder(图向量,  trg_mask)
        output = self.out(d_output)
        output=output[:,-1,:]
        return output
def get_model(opt,  trg_vocab,model_weights='model_weights'):
    
    assert opt.d_model % opt.heads == 0
    assert opt.dropout < 1

    model = Transformer( trg_vocab, opt.d_model, opt.n_layers, opt.heads, opt.dropout)
       
    if opt.load_weights is not None and os.path.isfile(opt.load_weights+'/'+model_weights):
        print("loading pretrained weights...")
        model.load_state_dict(torch.load(f'{opt.load_weights}/'+model_weights))
    else:
        量 = 0
        for p in model.parameters():
            if p.dim() > 1:
                #nn.init.xavier_uniform_(p)
                a=0
            长 = len(p.shape)
            点数 = 1
            for j in range(长):
                点数 = p.shape[j] * 点数

            量 += 点数
        print('使用参数:{}百万'.format(量/1000000))
    return model


def get_modelB(opt, trg_vocab):
    assert opt.d_model % opt.heads == 0
    assert opt.dropout < 1

    model = RESNET_Transformer(trg_vocab, opt.d_model, opt.n_layers, opt.heads, opt.dropout)

    if opt.load_weights is not None and os.path.isfile(opt.load_weights + '/model_weightsB'):
        print("loading pretrained weights...")
        model.load_state_dict(torch.load(f'{opt.load_weights}/model_weightsB'))
    else:
        量 = 0
        for p in model.parameters():
            if p.dim() > 1:
                # nn.init.xavier_uniform_(p)
                a = 0
            长 = len(p.shape)
            点数 = 1
            for j in range(长):
                点数 = p.shape[j] * 点数

            量 += 点数
        print('使用参数:{}百万'.format(量 / 1000000))
    return model