@echo off

echo Installing required packages...
pip install requests
pip install zipfile
echo Done!
start backuper.py
pause
