#神经网络老死  强制更新（不理会损失函数）
#随机更新 不管损失函数 随机更新
#通过计数 更改的个数以及不更改的个数   通过比例判断是否开启强制更新/随机更新

def random_update(self):#随机更新
    random_network = Network(NETWORK_SHAPE)#网络彻底死了  重新生成
    for i in range(len(self.layers)):#神经网络所有层进行更新
        weights_change = random_network.layers[i].weights
        biases_change = random_network.layers[i].biases
        self.layers[i].weights += weights_change
        self.layers[i].weights += biases_change
      
