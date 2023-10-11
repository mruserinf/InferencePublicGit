import datetime,os,time,sys
import random
import string

print("Public repo with branch Test_Inference_EKS clonned Successfully")
print ("Current date and time : ")
a=[]
print(sys.argv[1])
seconds=int(sys.argv[1])
i = 1
while i < seconds:
  now = datetime.datetime.now()
  a.append(now.strftime("%Y-%m-%d %H:%M:%S"))
  time.sleep(1)
  print(now.strftime("%Y-%m-%d %H:%M:%S"))
  print("\n")
  chars = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(999)])  # 1
  print(chars)
  i += 1

if __name__ == "__main__":
  print("Running inference.py program")
    # with open(os.path.join(os.environ['OUTPUT_PATH'], 'output.csv'), 'w') as output_fd:
    #         output_fd.write(str(a))
    #         output_fd.write('\n')
