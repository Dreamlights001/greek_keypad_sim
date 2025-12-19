# 希腊字母科研键盘仿真器 (Greek Keypad Simulator)

这是一个用于验证科研/数学输入需求的**软件原型**。它模拟了一个独立的 5x6 机械小键盘，旨在解决 Word 公式录入和 LaTeX 代码编写中的希腊字母输入痛点。
```
MyGreekKeypad/
├── greek_keypad_sim.py  (主程序)
├── install_win.bat      (Windows安装脚本)
├── start_win.bat        (Windows启动脚本)
├── install_unix.sh      (Mac/Linux安装脚本)
├── start_unix.sh        (Mac/Linux启动脚本)
└── README.md            (说明文档)
```
## ✨ 主要功能

1.  **双模切换 (Dual Mode)**：
    * **Unicode Mode (绿色)**：直接输出 `α`, `β`, `γ` 等字符。适用于微信、网页、Word。
    * **LaTeX Mode (青色)**：输出 `\alpha`, `\beta`, `\gamma` 等代码。适用于 Overleaf, VS Code, Markdown。
2.  **可视化反馈**：按下 "Mode Switch" 键，界面上的键帽文字会实时改变，模拟 E-Ink 键盘或侧刻提示效果。
3.  **Shift 逻辑**：完美复刻 LaTeX 的大小写逻辑（例如：Shift+δ -> `\Delta`, Shift+α -> `A`）。
4.  **一键复制**：所有输入内容显示在模拟屏幕上，支持一键复制。

## 🚀 快速开始

### 前置要求
- 你的电脑上需要安装 Python 3.x。

### Windows 用户
1.  双击运行 `install_win.bat` (仅需运行一次，用于安装依赖)。
2.  双击运行 `start_win.bat` 启动程序。

### macOS / Linux 用户
1.  打开终端，进入本文件夹。
2.  赋予安装脚本权限：`chmod +x install_unix.sh`
3.  运行安装脚本：`./install_unix.sh`
4.  启动程序：`./start_unix.sh`

## 🛠️ 文件结构说明
- `greek_keypad_sim.py`: 核心 Python 源代码 (基于 Tkinter)。
- `venv/`: 自动生成的 Python 虚拟环境 (包含 python 解释器和依赖库)。

## ⚠️ 常见问题
**Q: Linux 下报错 `ModuleNotFoundError: No module named 'tkinter'`**
A: 某些轻量级 Linux 发行版（如 Ubuntu）默认不带 Tkinter。请运行以下命令安装：
`sudo apt-get install python3-tk`

---
*Created for Research Workflow Optimization.*