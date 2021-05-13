import sys
import os
print("Commit2")
print(sys.argv[1])

import datetime,os,time,sys
import random

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
