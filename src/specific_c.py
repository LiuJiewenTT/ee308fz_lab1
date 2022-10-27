import global_vars
import common

OINFOHEADER = f'[{__name__}]: '
mode: common.DevMode = global_vars.gmode.utilize()
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
# Optional choice: be set to vars in global_vars.py
keys: list = None
strs: list = None
moreinfo: list = None
wordLocation: list = None
locations: list = None
SwCnt_Group = []

def entrance(pkeys, pstrs, pmoreinfo=None):
    global keys, strs, moreinfo, wordLocation, locations, SwCnt_Group, mode
    keys = pkeys
    strs = pstrs
    moreinfo = pmoreinfo
    # may change when moreinfo is truly implied.
    wordLocation = moreinfo
    # if mode.isDebug():
    #     print(common.str_2.wordFind.__name__)
    locations = extractWordsBraces(strs, wordLocation)
    locations_SwCsBraces = extractSwCsBraces(locations)
    if mode.isDebug():
        print(OINFOHEADER + f'locations_SwCsBraces: {locations_SwCsBraces}')
    SwCnt_Group = countSwCs(locations_SwCsBraces)

    # output SwCs
    print(f'switch num: ', SwCnt_Group.__len__())
    print('case num: ', end='')
    for i in SwCnt_Group:
        print(i, end=' ')
    print('')




# intend to use iteration function to proceed each group of SwCs
def countSwCs(ploctions_SwCsBraces):
    global mode

    if mode.isDebug():
        print(OINFOHEADER + f'plocations_SwCsBraces: {ploctions_SwCsBraces}')

    SwCnt_Group = []
    intervals = []
    length = ploctions_SwCsBraces.__len__()
    flag = False
    CsCnt = 0

    i = 0
    while i < length:
        if ploctions_SwCsBraces[i][2]=='switch':
            endBrace = i+2
            bcnt = 0
            j = i+1
            while j<length:
                try:
                    if ploctions_SwCsBraces[j][2] == '{':
                        bcnt += 1
                    elif ploctions_SwCsBraces[j][2] == '}':
                        bcnt -= 1
                    if bcnt==0:
                        break
                    j += 1
                except IndexError as ie:
                    estr = OINFOHEADER + f'j/length: {j, length}'
                    raise IndexError(estr)
            if bcnt==0:
                endBrace = j
            else:
                estr = OINFOHEADER + f'file content has a problem: braces not match.'
                raise RuntimeError(estr)
            interval = [i, endBrace+1]
            intervals.append(interval)
            CsCntItr = countSwCs(ploctions_SwCsBraces[i+1:endBrace+1])
            SwCnt_Group.extend(CsCntItr)
            # print(SwCnt_Group)
            i = endBrace
        i += 1

    if mode.isDebug():
        print(OINFOHEADER + f'intervals: {intervals}')

    i = 0
    while i < length:
        flag = False
        # print(CsCnt)
        for j in intervals:
            x, y = j
            # print(x, y, j)
            if i in range(x, y):
                i = y
                flag = True
        if flag == True:
            continue
        if ploctions_SwCsBraces[i][2]=='case':
            CsCnt += 1
        i += 1
    if CsCnt!=0:
        SwCnt_Group.append(CsCnt)
    return SwCnt_Group


# intend to use binary tree structure
def countIfEs():
    pass

# not only keywords, but also the bracket(Braces{})
def extractWordsBraces(pstrs, pwordLocation):
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
    braceLocations = common.insert_sort(tbraceLocations[0], tbraceLocations[1], func=common.cmp_moreinfo_Loc)
    pLocation = pwordLocation
    pLocation.extend(braceLocations)
    pLocation.sort()
    if mode.isDebug():
        print(OINFOHEADER + f'braceLocations: {braceLocations}')
        print(OINFOHEADER + f'pwordLocations: {pwordLocation}')
        print(OINFOHEADER + f'pLocations: {pLocation}')
    return pLocation

def extractSwCsBraces(pLocation):
    ret = []
    for i in pLocation:
        for j in ['switch', 'case', '{', '}']:
            if i[2]==j:
                ret.append(i)
                break
    return ret

# def temp():
#     print(OINFOHEADER, vmode)

# if mode.isDebug():
#     print(OINFOHEADER + 'hi')
#     entrance([],[])