print("Public repo clonned Successfully")

import sys
import os
from os import path
for i in range(len(sys.argv)):
  print(sys.argv[i])

print(os.getenv('test'))
print(os.getenv('test1'))

print('DATA_PATH',os.getenv('DATA_PATH')) 
file1= os.path.join(os.getenv('DATA_PATH'),'input.csv')
print ("Is data file exists? " + str(path.isfile(file1)))

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
