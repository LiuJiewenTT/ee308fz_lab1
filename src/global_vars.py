# The special thing is, this file is prepared for loop-referencing varibles.
# That defined once, avoiding importing main.py and resetting values on every import, totally clean environment to defined in.
# Constants are not necessarliy to be here, cause values are always the same.
# Or varibles of same name that sharing memory as well. like mode for different files.
# Classification:
# - 1 : Need further loading
# - 2 : share varible


# Type: 1
global gmode
try:
    gmode = gmode
except:
    gmode = None

# # Type: 2
# global vmode
# try:
#     vmode = vmode
# except:
#     vmode = {}