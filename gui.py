import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from utils import *


class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Graph Theory')
        self.root.iconbitmap(f'assets\\logo.ico')
        self.width = 600
        self.height = 400
        self.root.geometry("600x400")

        self.top_frame = tk.Frame(self.root)
        self.graph_frame = tk.Frame(self.root, bd=1, relief=tk.RAISED)

        tk.Label(self.top_frame, font=("Arial", 12), text="请输入有限非负整数序列，用英文逗号分隔").pack(pady=20)

        self.entry = tk.Entry(self.top_frame, font=("Arial", 12), validate="key",
                              validatecommand=(self.top_frame.register(validate_input), "%P"))
        self.entry.pack(side=tk.LEFT, padx=(10, 5), ipady=4)
        but = tk.Button(self.top_frame, text="生成", font=("Arial", 12), command=self.generate)
        but.pack(side=tk.LEFT, padx=(5, 10))

        # 退出toast
        self.root.protocol("WM_DELETE_WINDOW", self.confirm_exit)

        self.top_frame.pack()
        self.graph_frame.pack(fill="both", expand=True, padx=50, pady=20)

    def confirm_exit(self):
        # 显示确认退出的对话框
        if messagebox.askyesno("exit", "是否退出程序？"):
            self.root.destroy()

    def generate(self):
        input_sequence = str2seq(self.entry.get())
        if not is_graphical(input_sequence):
            messagebox.showwarning("否", "该度序列不可图")
            self.clear()
            return
        self.clear()
        graph = nx.havel_hakimi_graph(input_sequence)
        pos = nx.spring_layout(graph)
        fig, ax = plt.subplots(figsize=(6, 6))  # 图形的大小
        nx.draw(graph, pos, with_labels=True, ax=ax, node_size=500, node_color="skyblue", font_size=12,
                font_weight='bold')

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def clear(self):
        self.entry.delete(0, tk.END)
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
