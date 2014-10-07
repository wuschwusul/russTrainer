import sys
from os.path import join,dirname

sys.path.append(join(dirname(dirname(__file__)),"lib"))
sys.path.append(join(dirname(dirname(__file__)),"lib","wurscht"))
print sys.path

import wurscht
print("hiui")

print sys.path