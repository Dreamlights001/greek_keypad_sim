@echo off
setlocal

REM 检查是否已安装
if not exist "venv" (
    echo [ERROR] Environment not found. Please run 'install_win.bat' first.
    pause
    exit /b
)

REM 激活环境
call venv\Scripts\activate

REM 启动 Python 程序
REM 使用 pythonw.exe 可以隐藏黑色的命令行窗口
echo [INFO] Launching Greek Keypad Simulator...
start "" pythonw greek_keypad_sim.py

exit