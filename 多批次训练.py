#多批次训练
impor math
def train(self,n_entries):
    n_batches = math.ceil(n_entries/BATCH_SIZE)#天花板除   5/2 =3  地板除 5/2=2 其实是上取整
    for i in range(n_batches):
        batch = cp.creat_data(BATCH_SIZE)
        self.one_batch_train(batch)
    data = cp.creat_data(100)    
    cp.plot_data(data,"Right Classification")
    inputs = data[:,(0,1)]
    outputs = self.net_forward(inputs)
    classification = classify(outputs[-1])
    data[:,2] = classification
  cp.plot_data(data,"After training")
