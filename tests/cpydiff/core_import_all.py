"""
categories: Core,import
description: __all__ is unsupported in device.py in MicroPython.
cause: Not implemented.
workaround: Manually import the sub-modules directly in device.py using ``from . import foo, bar``.
"""
from modules3 import *

foo.hello()
