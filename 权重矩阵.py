#权重矩阵
-------------------------------------------------------------------------------------------------------------------
#第一层神经网络
import numpy as np
inputs = np.array([a1,a2,a3])#此处可多批次输入  即batch（只要保持列数不变就可以一直进行矩阵运算）

#权重一组
w11=0.8
w21=-0,4
w31=0

#权重二组
w12=0.8
w22=-0,4
w32=0

weights=np.array([w11,w12],[w21,w22],[w31,w32])    #权重矩阵

b1=0.6 #偏执值     也可以是数组  b1=np.array([0.1,0.7])    两个不同形状的数组也是可以相加的

sum1=np.dot(inputs,weights)+b1     #矩阵相乘
-----------------------------------------------------------------------------------------------------------------------
#   自动生成权重矩阵  无需手输入（权重生成函数）
def create_weihts(n_inputs,n_neurouns):           #n  number   neurouns  神经元     n个输入值，m个神经元
   return np.random.randn(n_inputs,n_neurouns)
-----------------------------------------------------------------------------------------------------------------------
#   自动生成偏执值  无需手输入
def create_biases(n_neurouns):           #有几个神经元 生成几个偏执值
   return np.random.randn(n_neurouns)
    

