print("Public Repo cloned successfully")
   
import sys
import os
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(os.getenv('env1'))
print(os.getenv('env2'))

print('OUTPUT_PATH',os.getenv('OUTPUT_PATH'))
print('CODE_PATH',os.getenv('CODE_PATH'))

f= open(os.getenv('OUTPUT_PATH') + "/output_729082.csv","w+")
f.write("1,2,3,4")
f.close()
