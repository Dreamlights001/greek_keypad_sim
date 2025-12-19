@echo off
setlocal
title Installing Greek Keypad Simulator...

echo ===================================================
echo   Greek Keypad Simulator - Environment Setup
echo ===================================================

REM 1. 检查是否安装了 Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python from python.org first.
    pause
    exit /b
)

REM 2. 创建虚拟环境 (文件夹名为 venv)
if not exist "venv" (
    echo [INFO] Creating virtual environment...
    python -m venv venv
) else (
    echo [INFO] Virtual environment already exists.
)

REM 3. 激活环境并安装依赖
echo [INFO] Activating virtual environment...
call venv\Scripts\activate

echo [INFO] Installing dependencies (pyperclip)...
pip install pyperclip

echo.
echo ===================================================
echo   [SUCCESS] Installation Complete!
echo   You can now run 'start_win.bat' to launch the app.
echo ===================================================
echo.
pause