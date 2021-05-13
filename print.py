import sys
import os
print("Commit2")
print(sys.argv[1])

print(os.getenv('test'))
print(os.getenv('test1'))

print('DATA_PATH',os.getenv('DATA_PATH')) 
print('MODEL_PATH',os.getenv('MODEL_PATH'))
print('OUTPUT_PATH',os.getenv('OUTPUT_PATH'))
print('CODE_PATH',os.getenv('CODE_PATH'))

f= open(os.getenv('OUTPUT_PATH') + "/output.csv","w+")
f.write("1,2,3,4")
f.close()

import datetime,os,time,sys
import random
import string
print("InferencePublicGit master repository")
print ("Current date and time : ")
a=[]

seconds=int(sys.argv[1])
i = 1
while i < seconds:
  now = datetime.datetime.now()
  a.append(now.strftime("%Y-%m-%d %H:%M:%S"))
  time.sleep(1)
  print(now.strftime("%Y-%m-%d %H:%M:%S"))
  i += 1

if __name__ == "__main__":

    with open(os.path.join(os.environ['OUTPUT_PATH'], 'output.csv'), 'w') as output_fd:
            output_fd.write(str(a))
            output_fd.write('\n')
