# coding: utf-8
# cx_Freeze �p�Z�b�g�A�b�v�t�@�C��

import os
os.environ['TCL_LIBRARY'] = "C:\\Users\\user_name\\AppData\\Local\\Programs\\Python\\Python35\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\user_name\\AppData\\Local\\Programs\\Python\\Python35\\tcl\\tk8.6"


import sys
from cx_Freeze import setup, Executable
 
base = None

# GUI=�L��, CUI=���� �ɂ���
if sys.platform == 'win32' : base = 'Win32GUI'
 
# exe �ɂ����� python �t�@�C�����w��
exe = Executable(script = 'sam1.py',
                 base = base)
 
# �Z�b�g�A�b�v
setup(name = 'sample',
      version = '0.1',
      description = 'converter',
      executables = [exe])