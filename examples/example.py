#!/usr/bin/env python
""" This example demonstrates that you need to run
'pip install .' in the main directory, before you
can do 'import empty_python' in a Python program

The from __future__ import below is to make this
code compatible with both Python 2 and 3
"""
from __future__ import print_function

try:
    import empty_python
    print("Succesfully imported empty_python!")
except ImportError:
    print("Could not import empty_python! Maybe you forgot to run 'pip install'")
