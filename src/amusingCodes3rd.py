# Amusing codes that they offered.

# class method decorator / method_register
# Source: https://www.jianshu.com/p/5c0083eb76fe
# Modification: None

from functools import wraps
from inspect import getattr_static

def method_register(cls):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            return func(self, *args, **kwargs)
        if getattr_static(cls, func.__name__, None):
            msg = 'Error method name REPEAT, {} has exist'.format(func.__name__)
            raise NameError(msg)
        else:
            setattr(cls, func.__name__, wrapper)
        return func
    return decorator
