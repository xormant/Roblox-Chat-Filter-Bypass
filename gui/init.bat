@echo off
SETLOCAL ENABLEEXTENSIONS

echo [ Checking if a few things are installed... ]

ver | findstr /i "10.0." >nul
if errorlevel 1 (
    echo [[31mERROR[37m! ][0m This script is designed for Windows 10 only.
    exit /b 1
)

where python >nul 2>&1
if errorlevel 1 (
    echo [[31mERROR[37m! ][0m Python is not installed. Please install Python and add it to your PATH.
    exit /b 1
)

where pip >nul 2>&1
if errorlevel 1 (
    echo [[31mERROR[37m! ][0m Pip is not installed. Please install Pip.
    exit /b 1
)

pip show PyQt5 >nul 2>&1
if errorlevel 1 (
    echo [[33mWARNING[37m! ][0m PyQt5 is not installed. Installing PyQt5...
    pip install PyQt5
)

pip show requests >nul 2>&1
if errorlevel 1 (
    echo [[33mWARNING[37m! ][0m requests is not installed. Installing requests...
    pip install requests
)

echo [37m[[32m OK[37m! ][0m
echo [ Running Script! ]
python main.py

ENDLOCAL