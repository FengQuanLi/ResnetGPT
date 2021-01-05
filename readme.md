# 基于pytorch框架用resnet101加GPT搭建AI玩王者荣耀
   本源码模型主要用了[SamLynnEvans Transformer](https://github.com/SamLynnEvans/Transformer) 的源码的解码部分。以及pytorch自带的预训练模型"resnet101-5d3b4d8f.pth"

# 注意运行本代码需要注意以下几点 注意！！！！！
1、目前这个模型在用后裔100多局对战数据下训练出来后，对局表现出各种送人头之类的问题，以及代码本身各种不规范，请多原谅。  
2、本代码本来只是我试验模型能否玩王者荣耀，B站朋友强烈要求开源。仓促开源估计问题很多，请多原谅。  
三、运行环境win10；win7未测试，估计是可以。  需要一张6G或以上显存的英伟达显卡，虽然4G的1050ti勉强也可以。  
四、需要一台打开安卓调试并能玩王者荣耀的手机，虚拟机没有试过，理论上应该可行。  
五、需要下载[scrcpy](https://github.com/Genymobile/scrcpy/blob/master/README.zh-Hans.md)  的windows版本。 把所有文件解压到项目根目录即可（这是我的笨办法） 。  
位置如图  
![scrcpy](image/scrcpy.png)  
六、需要在手机安装[minitouch](https://github.com/openstf/minitouch) ，比较麻烦，如有困难请多多百度。  
七、本人用的手机分辨率是1080*2160的，本代码并没有针不同的手机做优化。不同的手机minitouch命令中所描述的位置会有差异，需要对代码做出相应调整，请务必注意。  
八、注意游戏的布局，务必要一样。布局可参考B站视频或者我上传的训练用截图。如图。  
![布局图](image/85.jpg)  
九、游戏更新以后可能会导致无法预料的后果，因此并不能保证此代码玩王者荣耀的长期有效性。  
我之后可能出视频教程，同时讲讲我的设计思路。部分地区截图不可见，可下载项目在pycharm下打开readme.md即可见。

# 运行与生成训练数据
需要的库  
torch  
torchvision    
pynput  
pyminitouch  
可能还有其它库


## 运行
如果前面的工作做好了就可以把模型跑起来了，这里再次声明这个模型还是试验性质的，水平很低，青铜人机都未必能打过。
一、首先下载模型 你可以从[google云盘](https://drive.google.com/file/d/1HaDIMeVNixbGWViuBqvZr6uicyAUiyYT/view?usp=sharing) 下载模型，也可以百度网盘下载 
链接：https://pan.baidu.com/s/1Bt7BXukDDCpc1aWFI2iKxg   
提取码：5c1k  
后放入weights文件夹下  
二、先运行 “启动和结束进程.py” 启动scrcpy
把“训练数据截取_A.py” 中的两项改成你的  
![启动和结束进程.py](image/说明.png)  
三、启动王者荣耀进入5v5人机对战    运行 “训练数据截取_A.py” 即可。
## 生成训练数据
运行 “训练数据截取_A.py” 时可以通过按键操控角色，这时就可以生成训练用的数据，如果没有操控则会生成一个空文件夹和空json文件。  
按"i"键则结束或则是重新运行  
按键'w' 's ' 'a' 'd'控制方向  左、下、右箭头对应是1、2、3技能，上箭头长按则攻击。其它按键请参考源码。   
每次获取训练图片最好不要超过5000张  

你也可以下载训练数据样本（只是样本，数据量不大，不能指望两局对战数据就有效果，我估计这个模型现有参数可以吃下上万场的对战数据）  
百度网盘
链接：https://pan.baidu.com/s/1Ak1sLcSRimMWRgagXGahTg 
提取码：t4k3   
[google云盘](https://drive.google.com/file/d/1plN4xDaGgdRGiy6LT4qHG9O7US2I7_oS/view?usp=sharing)  
解压后注意存放位置，请参考源码。
# 如何训练
一、数据预处理  
将图片用resnet101预处理后再和对应操作数据一起处理后用numpy数组储存备用。  
具体要做的就是运行 “处理训练数据5.py”   
二、训练  
预处理完成以后运行 “训练_B.py”即可。


