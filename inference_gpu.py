import subprocess
import sys
import os
os.system("nvidia-smi")
os.system("nvcc --version")
subprocess.check_call([sys.executable, "-m", "pip", "install", "tensorflow"])

import tensorflow as tf
if tf.test.gpu_device_name():
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
else:
    print("Please install GPU version of TF")
