@echo off
setlocal

pip install pyinstaller pywebview requests
pyinstaller --onefile --windowed --name RigbyLauncher --add-data "rigby_launcher;rigby_launcher" ..\rigby_launcher\__main__.py

echo Build complete: dist\RigbyLauncher.exe
