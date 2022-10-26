import os.path as osp
import sys
from global_vars import *
import common

gmode = common.DevMode(common.MODE_GDEBUG)

print(sys.argv)

# Open File
f = None
flag = False
fileName = sys.argv[1]
print(fileName)
# Check ext
fileExt:common.ExtClass = common.ExtClass(gmode)
# fileExt.mode.setMode(common.MODE_COMMON)
fileExt.extSelect(fileName)
# open
try:
    f = open(fileName)
    flag = True
except FileNotFoundError as fe:
    print(fe)
# open successful

print(f'fext={fileExt.ext, fileExt.exti}')

# read file data
if flag is True:
    strs = f.readlines()


# Close File
if f is not None:
    f.close()