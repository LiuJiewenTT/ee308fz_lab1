import global_vars
import amusingCodes3rd

OINFOHEADER = f'[{__name__}]: '

# Constants
MODE_COMMON = 0
MODE_DEBUG = 1
MODE_GDEBUG = 2

class DevMode:
    mode = MODE_COMMON
    ifConst = False

    def __init__(self, ModeValue=mode, beConst=False):
        self.mode = ModeValue
        self.ifConst = beConst

    def setMode(self, ModeValue):
        if self.ifConst is False:
            # This writing is the same with putting self.mode=ModeValue here, but I'm letting you avoiding that thought.
            ret = self
            ret.mode = ModeValue
        else:
            if self.isDebug():
                wstr = OINFOHEADER + f'Warning! You''re trying to change value of constant!'
                print(wstr)
            else:
                # print(self, self.ifConst)
                pass
            ret = self.dupeInstance()
            ret.mode = ModeValue
        return ret

    def isDebug(self):
        # print(self)
        return self.mode==MODE_DEBUG

    def isGDebug(self):
        return self.mode==MODE_GDEBUG

    def utilize(self):
        return modeUtilize(self)

    def dupeInstance(self):
        temp = DevMode(self.mode)
        return temp

sampleModeCommon = DevMode(MODE_COMMON, beConst=True)
sampleModeDebug = DevMode(MODE_DEBUG, beConst=True)

def modeUtilize(self: DevMode):
    if self.isDebug():
        return sampleModeDebug
    else:
        return sampleModeCommon

# Constants
EXT_C = 1
EXT_CPP = 2
EXT_JAVA = 3
EXT_PY = 4
extMap = {
    '': None,
    'c': EXT_C,
    'cpp': EXT_CPP,
    'java': EXT_JAVA,
    'py': EXT_PY
}

class ExtClass():

    ext = None
    exti = 0
    mode: DevMode = sampleModeCommon

    def __init__(self, mode: DevMode=None):
        # This case should write like this, or the parameter will be None value.
        if mode is None:
            mode = global_vars.gmode
        # print(global_vars.gmode)              # good
        # print(global_vars.gmode is None)      # False, good
        # print(mode)                           # None, when is written in parameter list.

        self.mode = mode.utilize()
        # print(self.mode)

    def extSelect(self, fileName:str=''):
        # debug code
        if self.mode.isDebug():
            print(OINFOHEADER + f'str: {fileName}')

        t1 = fileName.rsplit(sep='.', maxsplit=3)
        self.ext = t1[-1]

        try:
            self.exti = extMap[self.ext]
        except KeyError as ke:
            estr = OINFOHEADER + f'No matching ext.{self.ext}: {ke}'
            raise KeyError(estr)

        if self.ext == '' or len(t1) == 1:
            estr = OINFOHEADER + f'Error: ext={self.ext}. No ext or value error.'
            self.ext = None
            self.exti = 0
            raise ValueError(estr)



def countKw(keys, strs:list):
    mode: DevMode
    mode = global_vars.gmode
    mode = mode.utilize()
    # print(mode)
    # print(global_vars.gmode)
    # mode.setMode(MODE_DEBUG)

    cnt1 = 0
    cnt2 = 0
    keylength = {}
    for i in keys:
        keylength[i] = len(i)
    for i in strs:
        cnt1 = 0
        for j in keys:
            i: str
            # k = i.count(j)
            a = k = 0
            while True:
                # break
                a = i.find(j,a)
                if a == -1:
                    break
                a += keylength[j]
                if i[a].isalpha() is False:
                    k += 1
            cnt1 += k
            if mode.isDebug():
                if cnt1 != 0 and k != 0:
                    print(OINFOHEADER + f'[{cnt2}->{cnt2 + cnt1}][{j} + {k}] - {i.strip(chr(10))}')
        cnt2 += cnt1
    return cnt2


class str_2(str):
    # @amusingCodes3rd.method_register(str)
    def wordFind(self, str, startIndex=0):
        a = self.find(str, startIndex)
        while True:
            if a == -1:
                return -1
            b = a + len(str)
            if str[b].isalpha() is False:
                return a
            else:
                a = b
    # countKw() can use this function. but for performance consideration, i'm not using it.