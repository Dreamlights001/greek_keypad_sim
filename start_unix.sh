#!/bin/bash

# 获取脚本所在目录，防止在其他路径运行出错
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

# 检查环境
if [ ! -d "venv" ]; then
    echo "[ERROR] Environment not found. Please run './install_unix.sh' first."
    exit 1
fi

# 激活环境并运行
source venv/bin/activate
echo "[INFO] Launching Greek Keypad Simulator..."
python3 greek_keypad_sim.py