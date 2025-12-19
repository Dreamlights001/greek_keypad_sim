#!/bin/bash

echo "==================================================="
echo "  Greek Keypad Simulator - Environment Setup"
echo "==================================================="

# 1. 检查 Python3
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] python3 could not be found. Please install it first."
    exit 1
fi

# 2. 创建虚拟环境
if [ ! -d "venv" ]; then
    echo "[INFO] Creating virtual environment..."
    python3 -m venv venv
else
    echo "[INFO] Virtual environment already exists."
fi

# 3. 激活环境并安装依赖
echo "[INFO] Installing dependencies..."
source venv/bin/activate
pip install pyperclip

# 4. 授予启动脚本执行权限
chmod +x start_unix.sh

echo ""
echo "==================================================="
echo "  [SUCCESS] Installation Complete!"
echo "  Run './start_unix.sh' to launch the app."
echo "==================================================="