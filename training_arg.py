print("Public repo clonned Successfully")
print("Script training_arg.py")

import sys
import os
from os import path
for i in range(len(sys.argv)):
  print("arg: " ,sys.argv[i])

print("env1: ", os.getenv('env1'))
print("env2: ", os.getenv('env2'))

print("DATA_PATH: ", os.getenv('DATA_PATH'))
print("MODEL_PATH: ", os.getenv('MODEL_PATH'))
print("HYPERPARAM_PATH: ", os.getenv('HYPERPARAM_PATH'))

print('DATA_PATH',os.getenv('DATA_PATH')) 
file1= os.path.join(os.getenv('DATA_PATH'),'input.csv')
print ("Is data file exists? " + str(path.isfile(file1)))

print('HYPERPARAM_PATH',os.getenv('HYPERPARAM_PATH'))
file2= os.getenv('HYPERPARAM_PATH')
print ("Is HYPERPARAM_PATH file exists? " + str(path.isfile(file2)))
    
#print('OUTPUT_PATH',os.getenv('OUTPUT_PATH'))
print('CODE_PATH',os.getenv('CODE_PATH'))

f= open(os.getenv('MODEL_PATH') + "/DRS_Model.pl","w+")
f.write("1,2,3,4")
f.close()
file3= os.path.join(os.getenv('MODEL_PATH'),'DRS_Model.pl')
print ("Is output file exists? " + str(path.isfile(file3)))
print ("output saved in " + os.getenv('MODEL_PATH'))
