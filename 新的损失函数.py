def loss_function(predicted,real):
    condition = (predicte > 0.5)
    binary_predicted = np.where(condition,1,0)#四舍五入
    real_matrix = np.zeros(len(real),2)
    real_matrix[:,1] = real
    real_matrix[:,1] = 1-real
    product = np.sum(predicted*real_matrix,axis=1)
    return 1 - product
