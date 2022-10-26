# The special thing is, this file is prepared for loop-referencing varibles.
# That defined once, avoiding importing main.py and resetting values on every import, totally clean environment to defined in.
# Constants are not necessarliy to be here, cause values are always the same.

try:
    gmode = gmode
except:
    gmode = None