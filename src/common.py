from global_vars import *

# Constants
MODE_COMMON = 0
MODE_DEBUG = 1
MODE_GDEBUG = 2

class DevMode:
    mode = MODE_COMMON

    def __init__(self, ModeValue):
        self.mode = ModeValue

    def setMode(self, ModeValue):
        self.mode = ModeValue

    def isDebug(self):
        return self.mode==MODE_DEBUG

    def isGDebug(self):
        return self.mode==MODE_GDEBUG

    def utilize(self):
        return _modeUtilize(self)

sampleModeCommon = DevMode(MODE_COMMON)
sampleModeDebug = DevMode(MODE_DEBUG)

def _modeUtilize(self:DevMode):
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

    def __init__(self, mode=gmode):
        self.mode = mode.utilize()

    def extSelect(self, fileName:str=''):
        # debug code
        if self.mode.isDebug():
            print(f'str: {fileName}')

        t1 = fileName.rsplit(sep='.', maxsplit=3)
        self.ext = t1[-1]

        try:
            self.exti = extMap[self.ext]
        except KeyError as ke:
            estr = f'No matching ext.{self.ext}: {ke}'
            raise KeyError(estr)

        if self.ext == '' or len(t1) == 1:
            estr = f'Error: ext={self.ext}. No ext or value error.'
            self.ext = None
            self.exti = 0
            raise ValueError(estr)



def countKw(keys, strs:list):
    pass