import numpy as np
import math
import random
import matplotlib.pyplot as plt  #生成图像

NUM_OF_DATA = 10

def tag_entry(x,y):#打标函数
    if x**2 + y**2 < 1:
      tag=0
    else:
      tag=1
    return tag
def creat_data(num_of_data):
    entry_list = [] #数据条目的列表
    for i in range(num_of_data):
      x = random.uniform(-2,2)
      y = random.uniform(-2,2)
      tag = entry(x,y)
      entry = [x,y,tag]#生成的时候打标也打好了
      entry_list.append(entry)

    return np.array(entry_list)
#-----------可视化--------------
def plpt_data(data,title):
    color = []
  for i in data[:,2]:    #2指第三个元素
      if i == 0:
        color.append("orange")
      else:
          color.append("blue")
  plt.scatter(data[:,0],data[:,1],c=color)
  plt.title(title)
  plt.show()
#---------------------------------------------
 if __name__=="__main__":
   
