#softmax激活函数
#防止指数爆炸
def activation_softmax(inputs)
    max_values = np.max(inputs,axis=1,keepdims=true)     #find max values and make them in line
    slided_inputs=inputs - max_values
    exp_values = np.exp(slided_inputs) # 用指数 e 
    norm_base = np.sum(exp_values,axis-=1,keepdims=true) # 标准化 
    norm_values = exp_values/nor_base
    return norm_values
    
#标准化  让输出值永远在0～1范围内
#聚集的数分散  分散的数聚集
#防止一层一层传播造成梯度爆炸 数据丢失等情况
#思路： 
# 找到每一行最大值（绝对值后的最大）
#把最大值变成1/-1  其他的按比例缩小(除以最大值的绝对值）
#[5,-6] -> [5/6,-1]
#如果最大值是0 保持0不变/变成1
#找到变化比率（通过rate*max=1）rate = 1/max    （此为 16行实现方式）
