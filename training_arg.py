print("Public repo clonned Successfully")
print("Script training_arg.py")

import sys
import os
from os import path
for i in range(len(sys.argv)):
  print("arg: " ,sys.argv[i])

print("env1: ", os.getenv('env1'))
print("env2: ", os.getenv('env2'))
print("INPUT_PATH: ", os.getenv('INPUT_PATH'))
print("OUTPUT_PATH: ", os.getenv('OUTPUT_PATH'))

print('INPUT_PATH',os.getenv('INPUT_PATH')) 
file1= os.path.join(os.getenv('INPUT_PATH'),'input.csv')
print ("Is data file exists? " + str(path.isfile(file1)))

#print('MODEL_PATH',os.getenv('MODEL_PATH'))
#file2= os.path.join(os.getenv('MODEL_PATH'),'DRS_Model.pl')
#print ("Is model file exists? " + str(path.isfile(file2)))
    
print('OUTPUT_PATH',os.getenv('OUTPUT_PATH'))
#print('CODE_PATH',os.getenv('CODE_PATH'))

f= open(os.getenv('OUTPUT_PATH') + "/DRS_Model.pl","w+")
f.write("1,2,3,4")
f.close()
file3= os.path.join(os.getenv('OUTPUT_PATH'),'DRS_Model.pl')
print ("Is output file exists? " + str(path.isfile(file3)))
print ("output saved in " + os.getenv('OUTPUT_PATH'))
