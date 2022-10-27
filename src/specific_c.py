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
    
    # process switch-case
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
    
    # process if-else, if-elseif-else
    # these codes are only designed for cases with entire braces attached to keywords.
    locations_IfEsBraces = extractIfEsBraces(locations)
    if mode.isDebug():
        print(OINFOHEADER + f'locations_IfEsBraces: {locations_IfEsBraces}')
    cnt_IfEs, cnt_IfEsifEs = countIfEs(locations_IfEsBraces)

    # output IFES
    print(f'if-else num: ', cnt_IfEs)
    print(f'if-elseif-else num: ', cnt_IfEsifEs)



# intend to use iteration function to proceed each group of SwCs
def countSwCs(plocations_SwCsBraces):
    global mode

    if mode.isDebug():
        print(OINFOHEADER + f'plocations_SwCsBraces: {plocations_SwCsBraces}')

    SwCnt_Group = []
    intervals = []
    length = plocations_SwCsBraces.__len__()
    flag = False
    CsCnt = 0

    i = 0
    while i < length:
        if plocations_SwCsBraces[i][2]=='switch':
            endBrace = i+2
            bcnt = 0
            j = i+1
            while j<length:
                try:
                    if plocations_SwCsBraces[j][2] == '{':
                        bcnt += 1
                    elif plocations_SwCsBraces[j][2] == '}':
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
            CsCntItr = countSwCs(plocations_SwCsBraces[i+1:endBrace+1])
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
        if plocations_SwCsBraces[i][2]=='case':
            CsCnt += 1
        i += 1
    if CsCnt!=0:
        SwCnt_Group.append(CsCnt)
    return SwCnt_Group


# intend to use binary tree structure
def countIfEs(plocations_IfEsBraces):
    global mode

    cnt_IfEs = 0
    cnt_IfEsifEs = 0
    cntIFES = [cnt_IfEs, cnt_IfEsifEs]
    length = plocations_IfEsBraces.__len__()
    intervals = []
    i = 0
    while i < length:
        if plocations_IfEsBraces[i][2] == 'if' or \
                (plocations_IfEsBraces[i][2] == 'else' and plocations_IfEsBraces[i+1 if i+1 <length else i][2] != 'if'):
            endBrace = i + 2
            bcnt = 0
            j = i + 1
            while j < length:
                try:
                    if plocations_IfEsBraces[j][2] == '{':
                        bcnt += 1
                    elif plocations_IfEsBraces[j][2] == '}':
                        bcnt -= 1
                    if bcnt == 0:
                        break
                    j += 1
                except IndexError as ie:
                    estr = OINFOHEADER + f'j/length: {j, length}'
                    raise IndexError(estr)
            if bcnt == 0:
                endBrace = j
            else:
                estr = OINFOHEADER + f'file content has a problem: braces not match.'
                raise RuntimeError(estr)
            interval = [i + 2, endBrace]
            intervals.append(interval)
            retv = countIfEs(plocations_IfEsBraces[i + 1:endBrace + 1])
            if mode.isDebug():
                if retv!=[0, 0]:
                    print(OINFOHEADER + f'retv: {retv}')
            cnt_IfEs += retv[0]
            cnt_IfEsifEs += retv[1]
            i = endBrace
        i += 1

    # if mode.isDebug():
    #     print(OINFOHEADER + f'intervals: {intervals}')

    tpifesloclist = []
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
        tpifesloclist.append(plocations_IfEsBraces[i])
        i += 1

    if mode.isDebug():
        common.printLocContent(tpifesloclist, text='tpifesloclist', contextHeader=OINFOHEADER)

    i = 0
    tlength = tpifesloclist.__len__()
    while i < tlength:
        if tpifesloclist[i][2] == 'else':
            if tpifesloclist[i+1 if i+1<tlength else i][2] == 'if':
                cnt_IfEsifEs += 1
                while i < tlength:
                    if tpifesloclist[i][2] == 'else' and tpifesloclist[i+1 if i+1<tlength else i][2] != 'if':
                        break
                    i += 1
            elif tpifesloclist[i+1 if i+1<tlength else i][2] == '{':
                cnt_IfEs += 1
        i += 1
    cntIFES = [cnt_IfEs, cnt_IfEsifEs]
    return cntIFES

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
    ret = common.extractSpecificLocations(pLocation, ['switch', 'case', '{', '}'])
    return ret

def extractIfEsBraces(pLocation):
    ret = common.extractSpecificLocations(pLocation, ['if', 'else', '{', '}'])
    return ret

# def temp():
#     print(OINFOHEADER, vmode)

# if mode.isDebug():
#     print(OINFOHEADER + 'hi')
#     entrance([],[])