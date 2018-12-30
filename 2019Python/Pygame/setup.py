# coding: utf-8
# cx_Freeze 用セットアップファイル

import os
os.environ['TCL_LIBRARY'] = "C:\\Users\\user_name\\AppData\\Local\\Programs\\Python\\Python35\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\user_name\\AppData\\Local\\Programs\\Python\\Python35\\tcl\\tk8.6"


import sys
from cx_Freeze import setup, Executable
 
base = None

# GUI=有効, CUI=無効 にする
if sys.platform == 'win32' : base = 'Win32GUI'
 
# exe にしたい python ファイルを指定
exe = Executable(script = 'sam1.py',
                 base = base)
 
# セットアップ
setup(name = 'sample',
      version = '0.1',
      description = 'converter',
      executables = [exe])
