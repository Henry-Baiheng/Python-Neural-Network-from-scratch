#损失函数越小越好

#交叉熵  cross entropy
#[a,b]  [c,d]   交叉熵   ac+bd   表示结果与标签的相似程度

#损失函数
def precise_lose_function(predicted,real):
    real_matrix = np.zeros((len(real),2))  #定义real行 2列
    real_matrix[:,1] = real
    real_matrix[:,0] = 1 - real
    product = np.sum(predicted*real_matrix,axis=1)  #axis=1  横着相加
    return  1 - product    #越大 越不准
