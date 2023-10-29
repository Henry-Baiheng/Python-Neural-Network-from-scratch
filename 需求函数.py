#反向传播算法的起点
#定义最后一层函数值怎么变           需要怎么变 减小 不变 增大
#                                           -1    0   1

#需求函数
#最后一层
def get_final_layer_preAct_damands(predicted_values,target_vector):
    target = np.zeros((len(target_vectir),2))
    target = [:,1] = target_vector
    target = [:,0] = 1 - target_vector
    for i in range(len(target_vector)):
      if np.dot(target[i],predicted_values[i]) > 0.5:
          target[i] = np.array([0,0])
      else:
          target[i] = (target[i] - 0.5) * 2
    return  target

