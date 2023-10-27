#尽管面向对象的层很方便 但碰到百层一样麻烦
#---->定义网络的类
NETWORK_SHAPE = [2,3,4,2]
class Layer:
  def _init_(self,n_inputs,n_neurons):
    self.weights = np.random.randn(n_inputs,n_neurons)
    self.biases = np.random.randn(n_neurons)
class Network:
     def_init_(self,network_shape):  #shape用列表存储每个神经元
       self.layers = []
       self.shape = network_shape
       for i in range(len(network_shape)-1)  #因为权重矩阵比神经元层数少1
            layer = Layer(network_shape[i],network_shape[i+1])
            self.layers.append(layer)
      def network_forward(self,inputs):#前馈运算函数
        outputs = [inputs]
        for i in range(len(self.layers)):
          layer_output = self.layers[i].layer_forward(outputs[i])
          outputs.append(layer_outputs)
        return outputs
