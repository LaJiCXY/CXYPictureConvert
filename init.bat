@echo off
pip install pillow
if %errorlevel%==1 echo PIL is exist or You don't have python!
pip install tkinter
if %errorlevel%==1 echo tkinter is exist or You don't have python!
pip install json
if %errorlevel%==1 echo is exist or You don't have python!
start ./CXYConverts.py
if %errorlevel%==1 Run unsuccessfully , You don't have python! (or something is wrong)