#softmax激活函数
#防止指数爆炸
def activation_softmax(inputs)
    max_values = np.max(inputs,axis=1,keepdims=true)     #find max values and make them in line
    slided_inputs=inputs - max_values
    exp_values = np.exp(slided_inputs) # 用指数 e 
    norm_base = np.sum(exp_values,axis-=1,keepdims=true) # 标准化 
    norm_values = exp_values/nor_base
    return norm_values 
