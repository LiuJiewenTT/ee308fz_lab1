import os.path as osp
import sys
# import heartrate

import global_vars
import common

# heartrate.trace(browser=True)

OINFOHEADER = f'[{__name__}]: '
# global_vars.gmode = common.DevMode(common.MODE_GDEBUG)
global_vars.gmode = common.DevMode(common.MODE_COMMON)
# global_vars.gmode = common.DevMode(common.MODE_DEBUG)
gmode = global_vars.gmode.utilize()
# print(mode)
# print(global_vars.gmode)
# print(OINFOHEADER + f'mode: {mode}')
# print(OINFOHEADER + f'global_vars.gmode: {global_vars.gmode}')
# print(OINFOHEADER + f'global_vars.gmode.mode: {global_vars.gmode.mode}')

# Conclusion: Can share memory space
# vmode = global_vars.vmode
# vmode[__name__] = '1'
# print(OINFOHEADER, vmode)

import specific_c
import specific_cpp

# vmode[__name__] = '3'




def mainfunc(file=None):
    global gmode
    mode = gmode
    # mode = gmode.setMode(common.MODE_DEBUG)

    if mode.isDebug():
        print(sys.argv)

    # Open File
    f = None

    if file is None:
        try:
            fileName = sys.argv[1]
        except IndexError as ie:
            estr = OINFOHEADER + f'No file input, no first parameter given. {ie}'
            raise IndexError(estr)
    else:
        fileName = file
    # programDir = osp.dirname(sys.argv[0])
    programDir = osp.dirname(__file__)
    if mode.isDebug():
        print(OINFOHEADER + f'__file__: {__file__}')
        print(OINFOHEADER + f'programDir: {programDir}')
    dirsep = '\\' if sys.platform=='win32' else '/'
    fileName = osp.abspath(fileName)
    # fileName = osp.join(programDir, fileName)

    if mode.isDebug():
        print(OINFOHEADER + f'fileName: {fileName}')
        print(OINFOHEADER + 'programDir: ' + programDir)

    # Check ext
    fileExt: common.ExtClass = common.ExtClass()
    # fileExt.mode = fileExt.mode.setMode(common.MODE_DEBUG)
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
    keycnt, moreinfo = common.countKw(keys, strs)
    prStr = 'total num: {}'.format(keycnt)
    global_vars.answerCollection.append(prStr)
    # print('total num: ', keycnt)


    speMStr = f'specific_{fileExt.ext}'
    # __import__(speMStr)
    # speMDic = {
    #     'c': specific_c,
    #     'cpp': specific_cpp
    # }

    speMEStr = speMStr + '.entrance(keys, strs, moreinfo)'
    # # may have a change when moreinfo is truly implemented.
    # wordLocations = moreinfo
    # speMDic[fileExt.ext].entrance(keys, strs, moreinfo)
    exec(speMEStr)

    # specific_c.temp()

    # print collected answers
    global_vars.answerCollection: list
    prAnsCollection = ''
    ansClt_length = len(global_vars.answerCollection)
    for i in range(0, ansClt_length):
        prAnsCollection += global_vars.answerCollection[i]
        i += 1
        if i < ansClt_length:
            prAnsCollection += '\n'
    print(prAnsCollection)

    # Close File
    if f is not None:
        f.close()

    # heartrate.trace(browser=True)

    return prAnsCollection

if __name__ == '__main__':
    mainfunc()