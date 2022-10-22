import os.path as osp
import sys

print(sys.argv)

# Open File
f = None
flag = False
try:
    f = open(sys.argv[1])
    flag = True
except FileNotFoundError as fe:
    print(fe)

if flag is True:
    strs = f.readlines()

# Close File
if f is not None:
    f.close()