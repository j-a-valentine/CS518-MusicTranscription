import tkinter as tk
from tkinter import ttk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1000x400")
        self.root.option_add("*Font", ("Arial", 16))
        self.root.title("Music Transcription Tool")

    def run(self):
        self.root.mainloop()

    def stop(self):
        self.root.destroy()

    def load_window(self, prediction, submit_callback, audio_callback):
        for widget in self.root.winfo_children():
            widget.destroy()
        frame = ttk.Frame(self.root)
        frame.grid(row=0, column=0, padx=50, pady=50, sticky="nsew")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        ai_label = ttk.Label(frame, text="Predicted Lyrics", font=('Arial', 20, 'bold'))
        ai_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        ai_text = ttk.Label(frame, text=prediction, wraplength=950, justify='left', font=('Arial', 16), foreground='#333333')
        ai_text.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        input_label = ttk.Label(frame, text="Enter the lyrics you hear:", font=('Arial', 20, 'bold'))
        input_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        input_box = ttk.Entry(frame, width=80, font=('Arial', 16))
        input_box.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        input_box.insert(0, prediction)
        submit_button = ttk.Button(frame, text="Submit", command=lambda: submit_callback(input_box.get()))
        submit_button.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        play_button = ttk.Button(frame, text="Play Audio", command=audio_callback)
        play_button.grid(row=4, column=0, padx=10, pady=10, sticky="w")
