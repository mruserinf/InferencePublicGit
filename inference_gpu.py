import subprocess
import sys
import os
from os import path
os.system("nvidia-smi")
os.system("nvcc --version")
subprocess.check_call([sys.executable, "-m", "pip", "install", "torch"])

import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)
print(torch.cuda.get_device_name(0))


import torch.nn as nn
dev = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
t1 = torch.randn(1,2)
t2 = torch.randn(1,2).to(dev)
print(t1)  # tensor([[-0.2678,  1.9252]])
print(t2)  # tensor([[ 0.5117, -3.6247]], device='cuda:0')
t1.to(dev) 
print(t1)  # tensor([[-0.2678,  1.9252]]) 
print(t1.is_cuda) # False
t1 = t1.to(dev)
print(t1)  # tensor([[-0.2678,  1.9252]], device='cuda:0') 
print(t1.is_cuda) # True

class M(nn.Module):
    def __init__(self):        
        super().__init__()        
        self.l1 = nn.Linear(1,2)

    def forward(self, x):                      
        x = self.l1(x)
        return x
model = M()   # not on cuda
model.to(dev) # is on cuda (all parameters)
print(next(model.parameters()).is_cuda) # True

print(os.getenv('OUTPUT_PATH'))
f= open(os.getenv('OUTPUT_PATH') + "/output.csv","w+")
f.write("1,2,3,4")
f.close()
file3= os.path.join(os.getenv('OUTPUT_PATH'),'output.csv')
print ("Is output file exists? " + str(path.isfile(file3)))
print ("output saved in " + os.getenv('OUTPUT_PATH'))

#import tensorflow as tf
#if tf.test.gpu_device_name():
 #   print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
#else:
 #   print("Please install GPU version of TF")
