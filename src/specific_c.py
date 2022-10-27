import global_vars
import common

OINFOHEADER = f'[{__name__}]: '
mode: common.DevMode = global_vars.gmode.utilize()
mode = mode.setMode(common.MODE_DEBUG)
# print(OINFOHEADER + f'mode: {mode}')
# print(OINFOHEADER + f'global_vars.gmode: {global_vars.gmode}')
# print(OINFOHEADER + f'global_vars.gmode.mode: {global_vars.gmode.mode}')

# Conclusion: Can share memory space
# vmode = global_vars.vmode
# vmode[__name__] = '2'
# print(OINFOHEADER, vmode)

# keys = src.main.keys
# strs = src.main.strs
# Optional choice: be set to vars in global_vars.py
keys: list = None
strs: list = None
moreinfo: list = None
wordLocation: list = None
locations: list = None

def entrance(pkeys, pstrs, pmoreinfo=None):
    global keys, strs, moreinfo, wordLocation, mode
    keys = pkeys
    strs = pstrs
    moreinfo = pmoreinfo
    # may change when moreinfo is truly implied.
    wordLocation = moreinfo
    # if mode.isDebug():
    #     print(common.str_2.wordFind.__name__)
    extractWords(pkeys=keys, pstrs=strs, pwordLocation=wordLocation)

    pass


# intend to use iteration function to proceed each group of SwCs
def countSwCs():
    pass


# intend to use binary tree structure
def countIfEs():
    pass

# not only keywords, but also the bracket(Braces{})
def extractWords(pkeys=keys, pstrs=strs, pwordLocation=wordLocation):
    global mode
    if mode.isDebug():
        print(OINFOHEADER + f'pwordLocation: {pwordLocation}')
    braceLocations = []
    tbraceLocations = [[],[]]
    wholeStr = ""
    for i in pstrs:
        wholeStr += i
    # if mode.isDebug():
    #     print(OINFOHEADER + f'wholeStr: {wholeStr}')
    b = 0
    for i in ['{', '}']:
        idi = 0
        for tstr in pstrs:
            a = 0
            while True:
                a = tstr.find(i, a)
                # if mode.isDebug():
                #     print(OINFOHEADER + f'i: {i}, idi: {idi}, a: {a}, tstr: {tstr.strip(chr(10))}')
                if a==-1:
                    break
                tbraceLocations[b].append([idi, a, i])
                a += 1
            idi += 1
        b = 1
    # braceLocations.sort()
    if mode.isDebug():
        print(OINFOHEADER + f'tbraceLocations: {tbraceLocations}')
    braceLocations = insert_sort(tbraceLocations[0], tbraceLocations[1])
    pLocation = pwordLocation
    pLocation.extend(braceLocations)
    pLocation.sort()
    if mode.isDebug():
        print(OINFOHEADER + f'braceLocations: {braceLocations}')
        print(OINFOHEADER + f'pLocations: {pLocation}')
        print(OINFOHEADER + f'pwordLocations: {pwordLocation}')
    pass

def cmp1(a: list, b: list):
    # print(a, b)
    if a[0]>b[0]:
        return True
    elif a[0]<b[0]:
        return False
    else:
        return a[1]>b[1]

def insert_sort(a: list, b: list):
    global mode

    if mode.isDebug():
        print(OINFOHEADER + f'a: {a}')
        print(OINFOHEADER + f'b: {b}')

    i = 0
    j = 0
    i_len = len(a)
    j_len = len(b)
    k = 0
    k_len = i_len + j_len
    dst = []
    flag = 'null'
    while k<k_len:
        val = cmp1(a[i], b[j])
        if val is False:
            dst.append(a[i])
            if i<i_len-1:
                i += 1
            else:
                flag = 'i'
                break
        else:
            dst.append(b[j])
            if j<j_len-1:
                j += 1
            else:
                flag = 'j'
                break
        k += 1
        # if mode.isDebug():
        #     print(OINFOHEADER + f'[{k-1}]: {val}, dst[k]: {dst[k-1]}')
    if flag=='i':
        dst.extend(b[j:])
    elif flag=='j':
        dst.extend(a[i:])
    if mode.isDebug():
        print(OINFOHEADER + f'dst: {dst}')
    return dst



# def temp():
#     print(OINFOHEADER, vmode)

# if mode.isDebug():
#     print(OINFOHEADER + 'hi')
#     entrance([],[])