import global_vars
import common

OINFOHEADER = f'[{__name__}]: '
mode = global_vars.gmode.utilize()
# mode = mode.setMode(common.MODE_DEBUG)
# print(OINFOHEADER + f'mode: {mode}')
# print(OINFOHEADER + f'global_vars.gmode: {global_vars.gmode}')
# print(OINFOHEADER + f'global_vars.gmode.mode: {global_vars.gmode.mode}')

# Conclusion: Can share memory space
# vmode = global_vars.vmode
# vmode[__name__] = '2'
# print(OINFOHEADER, vmode)

# keys = src.main.keys
# strs = src.main.strs
keys: list = None
strs: list = None

def entrance(pkeys, pstrs):
    global keys, strs
    keys = pkeys
    strs = pstrs
    print(common.str_2.wordFind.__name__)
    pass

def countSwCs():
    pass

def countIfEs():
    pass

def extractWords():
    pass

# def temp():
#     print(OINFOHEADER, vmode)

if mode.isDebug():
    print(OINFOHEADER + 'hi')
    entrance([],[])