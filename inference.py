print("Public repo clonned Successfully")

import sys
import os
from os import path

print(os.getenv('env1'))
print(os.getenv('env2'))

print('MODEL_PATH',os.getenv('MODEL_PATH'))
file2= os.path.join(os.getenv('MODEL_PATH'),'DRS_Model.pl')
print ("Is model file exists? " + str(path.isfile(file2)))
    
print('OUTPUT_PATH',os.getenv('OUTPUT_PATH'))
print('CODE_PATH',os.getenv('CODE_PATH'))

f= open(os.getenv('OUTPUT_PATH') + "/output.csv","w+")
f.write("1,2,3,4")
f.close()

file3= os.path.join(os.getenv('OUTPUT_PATH'),'output.csv')
print ("Is output file exists? " + str(path.isfile(file3)))
    
print ("output saved in " + os.getenv('OUTPUT_PATH'))
