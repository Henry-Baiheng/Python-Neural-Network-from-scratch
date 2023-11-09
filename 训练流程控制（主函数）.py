#起始网络选择
#多次训练
def main():
    data = cp.creat_data(100) #生成数据
    use_this_network = 'n'  #不用 NO
    while use_this_network != 'Y' and use_this_network != 'y':
          network=Network(NETWORK_SHAPE)
          inputs = data[:(0,1)]
          outputs = self.network_forward(inputs)
          calssification = classsfy(outputs[-1])
          data[:,2] = classification
          cp.plot_data(data,"Before training")
          use_this_network =int(inputs("Use this network? Y to yes, N to no")) 
    do_train = input("Train? Y to yes, N no NO")
    while do_train =='Y' or do_train=='y' or do_rain.isnumeric()==True:
        if do_train.isnumeic() == True:
            n_entries = int(do_train)
        else:
           n_entries = inputs("Enter the number of data entries used to train.\n")
    #演示训练效果
   inputs = data[:(0,1)]
   outputs = self.network_forward(inputs)
   calssification = classsfy(outputs[-1])
   data[:,2] = classification
   cp.plot_data(data,"fter training")
