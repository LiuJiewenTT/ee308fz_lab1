# ReadMe: Project Introduction

This project is to count keywords of files in some levels. The sample test file given is `test/testfile.c`. For more information about subject, see website: [Link](https://bbs.csdn.net/topics/608734907)

## More md

1. [introduce.md](./introduce.md)
2. [development blog.md](./development%20blog.md)

## Highlights

1. Technique: Debug Mode in Codes for Developers
2. deeply processing the paths info.
3. high flexibility: support addons for more languages

### Debug Mode in Codes for Developers

(This section is temporary. It will be replaced by former webpage in the future.)

With this technique applied to your project, you can easily choose exactly which parts of debug info should be printed out. And it has **a general switch**, `global_vars.gmode`. 

The action is described as:

| Value | Effect |
| -------:| --------- |
| MODE_COMMON | No debug codes will be run |
| MODE_DEBUG | All debug codes will be run |
| MODE_GDEBUG | Only selected debug codes will be run |

> 1. MODE_GDEBUG is designed for gmode.
> 2. Effects is real only when mode variable of contexts is derived from gmode, which means leading relation.
>
> The project,  ee308fz_lab1, is a good example for you.

Also, DebugInfoOutputHeader is recommended. Like `OINFOHEADER` with set-value expression `OINFOHEADER = f'[{__name__}]: ' `.

``` python
if mode.isDebug():
	print(OINFOHEADER + [...])
    # tip: [...] can be f-string
```

#### The necessary parts to apply

1. global_vars.gmode
2. Class DevMode

For entrance file:

```python
global_vars.gmode = common.DevMode(common.MODE_COMMON)
# global_vars.gmode = common.DevMode(common.MODE_DEBUG)
# global_vars.gmode = common.DevMode(common.MODE_GDEBUG)
```

For each file:

`gmode = global_vars.gmode.utilize()`

`OINFOHEADER = f'[{__name__}]: ' `

For each function:

``` python
global gmode
mode = gmode
# mode.setMode([common].MODE_DEBUG)
```

or

``` python
mode = global_vars.gmode
mode = mode.utilize()
# mode.setMode([common].MODE_DEBUG)
```

For each class:

let `__init__` has an optional argument to receive mode, set default value to None.

``` python
    def __init__(self, mode: DevMode=None):
        # This case should write like this, or the parameter will be None value.
        if mode is None:
            mode = global_vars.gmode
```

For each method:

Use `self.mode`

#### Write addons for languages

You should define `entrance(pkeys, pstrs, pmoreinfo=None)`

