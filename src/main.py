import os.path as osp
import sys
import global_vars
import common

global_vars.gmode = common.DevMode(common.MODE_GDEBUG)

print(sys.argv)

# Open File
f = None
flag = False
fileName = sys.argv[1]
print(fileName)
# Check ext
fileExt:common.ExtClass = common.ExtClass()
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