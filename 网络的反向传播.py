#网络的反向传播
LEARNING_RATE = 0.01  #每次调百分之一
import copy
def network_backward(self,layer_outputs,target_vector):
    backup_network = copy.deepcopy(self) # 备用网络  通过前馈网络再跑一遍 好的话代替 不好舍弃
    preAct_demands = get_final_layer_preAct_demands(layer_outputs[-1],target_vector)
    for i in range(len(self.layers)):#有几层就循环几次
        layer = backeup_network.layers[len(self.layers) - (1+i)] # 倒序 最后一层不去调整 防止过拟合
        if i != 0:
            layer.biasese += LEARNING_RATE * np.mean(preAct_demands,axis=0)#取平均值  竖着取   LEARNING_RATE 常量    炼丹炉开始
            layer.biasese = normalize(layer.biasese)#标准化 更新偏执值
        outputs = layer_outputs[len(self.layers) - (2+i)] #前面一层的输出值
        results_list = layer.layer_backward(outputs,preAct_demands)
        preAct_demands = results_list[0]
        weights_adjust_matrix = results_list[1]
        layer.weights += LEARNING_RATE * weights_adjust_matrix
        layer.weights = normalize(layer.weights)#标准化 更新权重值
  return backup_network
