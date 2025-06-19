import sys
import os

# 确保当前文件夹加入模块搜索路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui import Gui

if __name__ == "__main__":
    gui = Gui()
    gui.root.mainloop()
