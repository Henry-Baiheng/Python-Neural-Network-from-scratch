def layer_backward(self,preWeights_values,afterWeights_demands):
    preWeights_demands = np.dot(afterWeights_demands,self.weights.T)

    condition = (preWeights_values > 0) # 大于零 =1   不大于0 =0  算的激活函数的导数
    value_derivatives = np.where(condition,1,0)
    preActs_demands =   value_derivatives  *  preWeights_demands    #激活函数之前的需求值
    norm_preActs_demands = normalize(preActs_demands)#标准化
    weight_adjust_matrix = self.get_weight_adjust_matrix( preActs_demands,afterWeights_demands)
    norm_weight_adjust_matrix = normalize(weight_adjust_matrix)
    return (norm_preActs_demands,norm_weight_adjust_matrix)
