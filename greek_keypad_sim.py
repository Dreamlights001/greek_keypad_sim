import tkinter as tk
from tkinter import ttk, messagebox
import sys  # [新增] 用于强制退出进程
import pyperclip  # 如果没有安装这个库，代码里做了降级处理

class GreekKeypadSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("硬件仿真: 希腊字母小键盘")
        self.root.geometry("400x550")
        self.root.resizable(False, False)

        # [新增] 绑定窗口关闭事件：当用户点击右上角X时，执行 self.on_closing
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # --- 状态变量 ---
        self.is_latex_mode = False  # False=Unicode, True=LaTeX
        self.is_shift_mode = False  # 大小写锁定
        
        # --- 数据定义 ---
        # 希腊字母表 (名字, Unicode小, Unicode大, Latex小, Latex大)
        self.greek_data = [
            ('alpha', 'α', 'Α', r'\alpha', 'A'),
            ('beta', 'β', 'Β', r'\beta', 'B'),
            ('gamma', 'γ', 'Γ', r'\gamma', r'\Gamma'),
            ('delta', 'δ', 'Δ', r'\delta', r'\Delta'),
            ('epsilon', 'ε', 'Ε', r'\epsilon', 'E'),
            ('zeta', 'ζ', 'Ζ', r'\zeta', 'Z'),
            ('eta', 'η', 'Η', r'\eta', 'H'),
            ('theta', 'θ', 'Θ', r'\theta', r'\Theta'),
            ('iota', 'ι', 'Ι', r'\iota', 'I'),
            ('kappa', 'κ', 'Κ', r'\kappa', 'K'),
            ('lambda', 'λ', 'Λ', r'\lambda', r'\Lambda'),
            ('mu', 'μ', 'Μ', r'\mu', 'M'),
            ('nu', 'ν', 'Ν', r'\nu', 'N'),
            ('xi', 'ξ', 'Ξ', r'\xi', r'\Xi'),
            ('omicron', 'ο', 'Ο', 'o', 'O'),
            ('pi', 'π', 'Π', r'\pi', r'\Pi'),
            ('rho', 'ρ', 'Ρ', r'\rho', 'P'),
            ('sigma', 'σ', 'Σ', r'\sigma', r'\Sigma'),
            ('tau', 'τ', 'Τ', r'\tau', 'T'),
            ('upsilon', 'υ', 'Υ', r'\upsilon', r'\Upsilon'),
            ('phi', 'φ', 'Φ', r'\phi', r'\Phi'),
            ('chi', 'χ', 'Χ', r'\chi', 'X'),
            ('psi', 'ψ', 'Ψ', r'\psi', r'\Psi'),
            ('omega', 'ω', 'Ω', r'\omega', r'\Omega'),
        ]
        
        self.setup_output_window()
        self.setup_keypad_ui()
        self.update_key_labels()

    def setup_output_window(self):
        """创建第二个窗口：模拟电脑屏幕的输出"""
        self.out_win = tk.Toplevel(self.root)
        self.out_win.title("模拟输出结果 (可复制)")
        self.out_win.geometry("500x200+420+0")
        
        # [新增] 如果用户把输出窗口关了，也视为退出程序，防止主程序卡死
        self.out_win.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        lbl = ttk.Label(self.out_win, text="电脑屏幕 / 编辑器输入流：", font=("Arial", 10))
        lbl.pack(pady=5, padx=10, anchor='w')
        
        self.output_text = tk.Text(self.out_win, height=5, font=("Consolas", 14))
        self.output_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        btn_frame = ttk.Frame(self.out_win)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(btn_frame, text="清空屏幕", command=self.clear_text).pack(side=tk.LEFT)
        ttk.Button(btn_frame, text="复制全部", command=self.copy_to_clipboard).pack(side=tk.RIGHT)

    def on_closing(self):
        """[核心优化] 安全退出机制"""
        try:
            # 1. 销毁所有 GUI 组件
            self.root.destroy()
        except:
            pass
        finally:
            # 2. 强制终止 Python 进程，释放内存
            sys.exit(0)

    def setup_keypad_ui(self):
        """创建主窗口：模拟键盘硬件"""
        status_frame = tk.Frame(self.root, bg="#333", height=40)
        status_frame.pack(fill=tk.X)
        
        self.mode_indicator = tk.Label(status_frame, text="UNICODE MODE", fg="#0f0", bg="#333", font=("Arial", 10, "bold"))
        self.mode_indicator.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.shift_indicator = tk.Label(status_frame, text="SHIFT: OFF", fg="#666", bg="#333", font=("Arial", 10))
        self.shift_indicator.pack(side=tk.RIGHT, padx=10, pady=10)

        keypad_frame = ttk.Frame(self.root, padding=10)
        keypad_frame.pack(fill=tk.BOTH, expand=True)

        self.buttons = [] 

        # Row 1: 功能键
        self.create_func_btn(keypad_frame, "MODE\nSwitch", 0, 0, self.toggle_mode, "orange")
        self.create_func_btn(keypad_frame, "SHIFT", 0, 1, self.toggle_shift, "lightblue")
        self.create_func_btn(keypad_frame, "← Back", 0, 2, self.backspace)
        self.create_func_btn(keypad_frame, "Space", 0, 3, lambda: self.type_char(" "))
        self.create_func_btn(keypad_frame, "Enter", 0, 4, lambda: self.type_char("\n"))
        self.create_func_btn(keypad_frame, "∂ / ∇", 0, 5, self.type_symbol_extra)

        # Row 2-5: 希腊字母
        for i, data in enumerate(self.greek_data):
            row = (i // 6) + 1
            col = i % 6
            btn = tk.Button(keypad_frame, text="?", width=6, height=3, font=("Arial", 12),
                            command=lambda d=data: self.type_greek(d))
            btn.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
            self.buttons.append((btn, data))

        for i in range(6): keypad_frame.columnconfigure(i, weight=1)
        for i in range(6): keypad_frame.rowconfigure(i, weight=1)

    def create_func_btn(self, parent, text, r, c, cmd, bg_color="#e1e1e1"):
        btn = tk.Button(parent, text=text, bg=bg_color, command=cmd, font=("Arial", 9, "bold"))
        btn.grid(row=r, column=c, padx=3, pady=3, sticky="nsew")
        return btn

    def update_key_labels(self):
        bg_color = "#e8f0fe" if self.is_latex_mode else "#f0f0f0"
        
        if self.is_latex_mode:
            self.mode_indicator.config(text="LaTeX MODE", fg="#00ffff")
        else:
            self.mode_indicator.config(text="UNICODE MODE", fg="#0f0")
            
        shift_txt = "SHIFT: ON" if self.is_shift_mode else "SHIFT: OFF"
        shift_color = "#fff" if self.is_shift_mode else "#666"
        self.shift_indicator.config(text=shift_txt, fg=shift_color)

        for btn, data in self.buttons:
            if not self.is_latex_mode:
                label = data[2] if self.is_shift_mode else data[1]
                btn.config(text=label, fg="black", bg="#fff")
            else:
                code = data[4] if self.is_shift_mode else data[3]
                btn.config(text=code, fg="blue", bg="#e8f0fe", font=("Consolas", 10))

    def toggle_mode(self):
        self.is_latex_mode = not self.is_latex_mode
        self.update_key_labels()

    def toggle_shift(self):
        self.is_shift_mode = not self.is_shift_mode
        self.update_key_labels()

    def type_greek(self, data):
        char_to_type = ""
        if not self.is_latex_mode:
            char_to_type = data[2] if self.is_shift_mode else data[1]
        else:
            char_to_type = data[4] if self.is_shift_mode else data[3]
        self.insert_text(char_to_type)

    def type_symbol_extra(self):
        if self.is_latex_mode:
            self.insert_text(r"\partial")
        else:
            self.insert_text("∂")

    def type_char(self, char):
        self.insert_text(char)

    def backspace(self):
        self.output_text.delete("end-2c", "end-1c")

    def clear_text(self):
        self.output_text.delete("1.0", tk.END)

    def insert_text(self, text):
        self.output_text.insert(tk.END, text)
        self.output_text.see(tk.END)

    def copy_to_clipboard(self):
        content = self.output_text.get("1.0", "end-1c")
        try:
            pyperclip.copy(content)
        except:
            self.root.clipboard_clear()
            self.root.clipboard_append(content)
        messagebox.showinfo("成功", "内容已复制到剪贴板！")

if __name__ == "__main__":
    root = tk.Tk()
    app = GreekKeypadSimulator(root)
    root.mainloop()