# ReadMe: Project Introduction

This project is to count keywords of files in some levels. The sample test file given is `test/testfile.c`. For more information about subject, see website: [Link](https://bbs.csdn.net/topics/608734907)

## Highlights

### Debug Mode in Codes for Developers

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
> The project is a good example for you.