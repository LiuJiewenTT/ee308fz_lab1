import os.path as osp
import sys
import global_vars
import common

global_vars.gmode = common.DevMode(common.MODE_GDEBUG)
OINFOHEADER = f'[{__name__}]: '

print(sys.argv)

# Open File
f = None
fileName = sys.argv[1]
print(OINFOHEADER + f'fileName: {fileName}')
programDir = osp.dirname(sys.argv[0])
print(OINFOHEADER + 'programPath: ' + programDir)
dirsep = '\\' if sys.platform=='win32' else '/'
# Check ext
fileExt: common.ExtClass = common.ExtClass()
# fileExt.mode.setMode(common.MODE_DEBUG)
fileExt.extSelect(fileName)
# open
try:
    f = open(fileName)
except FileNotFoundError as fe:
    estr = OINFOHEADER + f'{fe}'
    raise FileNotFoundError(estr)
# open successful

print(OINFOHEADER + f'fext={fileExt.ext, fileExt.exti}')

# read keywords
keys = []
try:
    with open(osp.join(programDir, f'keywords_{fileExt.ext}.txt')) as fkey:
    # with open(programDir + dirsep + f'keywords_{fileExt.ext}.txt') as fkey:
        t = fkey.read()
        keys = t.split()
except FileNotFoundError as fe:
    estr = OINFOHEADER + f'{fe}'
    raise FileNotFoundError(estr)
print(OINFOHEADER + 'keys: ' , keys)

# read file data
strs = f.readlines()

# work of 1st level
keycnt = common.countKw(keys, strs)
print('total num: ', keycnt)

# Close File
if f is not None:
    f.close()
