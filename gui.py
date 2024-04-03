import tkinter as tk
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

class GUI:
    def __init__(self, title):
        self.app = tk.Tk()
        self.app.title(title)
        self.app.mainloop()