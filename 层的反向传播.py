# 调整矩阵    如何调整权重矩阵

def get_weight_adjust_matrix(self,preWeights_values,afrWeights_demands):#生成权重的调整矩阵
    plain_weights = np.full(self.weights.shape,1)
    weights_adjust_matrix = np.full(self.weights.shape,0)
    plain_weights_T = plain_weights.T  #转置
    for i in range(BATCH_SIZE):  #大写为常量  一批数据的个数
        weights_adjust_matrix +=(plain_weights_T*preWeights_values[i,:]).T*aftWeights_demands[i.:]  #所有行相加的结果
    weights_adjust_matrix = weights_adjust_matrix/BATCH_SIZE
    return weights_adjust_matrix 
