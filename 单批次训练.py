#单批次训练
def one_batch_train(self,batch):
    inputs = batch[:,(0,1)]
    targets = copy.deepcopy(batch[:,2]).astype(int)
    #先正向传播
    outputs = self.network_forward(inputs)#输出值
    precise_loss = precise_loss_function( outputs[-1],targets )#损失函数
    if np.mean( precise_loss) <= 0.1:      #取平均值  这个是随便写的
      print("无需训练")#因为损失函数比较小 比较准 不用训练
    else:
      backup_network = self.network_backward(outputs,targets)
      backup_outputs = backup_network.network_forward(inputs)#前馈运算
      backup_precise_loss = precise_loss_function( backup_outputs[-1],targets )#备用网络的损失函数
      if np.mean(precise_loss) >= np.mean(backup_precise_loss):#训练成功
         for i in range(len(self.layers)):
             self.layers[i].weights = backup_network.layers[i].weights.copy()
             self.layers[i].biases = backup_network.layers[i].biases.copy()
             
