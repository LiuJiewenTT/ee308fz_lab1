import os.path as osp
import sys
import global_vars
import common

OINFOHEADER = f'[{__name__}]: '
global_vars.gmode = common.DevMode(common.MODE_GDEBUG)
mode = global_vars.gmode.utilize()
# print(mode)
# print(global_vars.gmode)

if mode.isDebug():
    print(sys.argv)

# Open File
f = None
try:
    fileName = sys.argv[1]
except IndexError as ie:
    estr = OINFOHEADER + f'No file input, no first parameter given. {ie}'
    raise IndexError(estr)
programDir = osp.dirname(sys.argv[0])
dirsep = '\\' if sys.platform=='win32' else '/'

if mode.isDebug():
    print(OINFOHEADER + f'fileName: {fileName}')
    print(OINFOHEADER + 'programPath: ' + programDir)

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

if mode.isDebug():
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
if mode.isDebug():
    print(OINFOHEADER + 'keys: ' , keys)

# read file data
strs = f.readlines()

# work of 1st level
keycnt = common.countKw(keys, strs)
print('total num: ', keycnt)

# Close File
if f is not None:
    f.close()
