import tkinter as tk
from PIL import Image, ImageTk

import analizadores.analizador_lexico as lexical
import analizadores.analizador_sintactico as syntax
import sys
import threading


class TextComponent:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)
        self.text_widget.config(state=tk.DISABLED)


def run_ruby(text_input):
    text_console.config(state=tk.NORMAL)
    text_console.delete(1.0, tk.END)
    sys.stdout = TextComponent(text_console)
    try:
        # Resetea el lexer sin modificar el número de línea
        lexical.lexer.input(text_input)
        for token in lexical.lexer:
            print(token)
        syntax.parser.parse(text_input)
    except Exception as e:
        print(f"Error: {e}")
    sys.stdout = sys.__stdout__
    text_console.config(state=tk.DISABLED)


def run_ruby_threaded(text_input):
    def task():
        run_ruby(text_input)

    threading.Thread(target=task).start()


def on_run():
    input_text_content = text_code.get(1.0, tk.END)
    run_ruby(input_text_content)

root = tk.Tk()
root.title("Ruby Analyzer")
root.geometry("800x600")
root.resizable(True, True)

frame_code = tk.Frame(root, bg="#2D2D2D")
frame_console = tk.Frame(root, bg="#2D2D2D")

frame_code.grid(row=0, column=0, sticky="nsew")
frame_console.grid(row=0, column=1, sticky="nsew")

root.grid_columnconfigure(0, weight=3)
root.grid_columnconfigure(1, weight=2)
root.grid_rowconfigure(0, weight=1)

button_run = tk.Button(frame_code, text="Run", bg="red", fg="white", command=on_run, width=8, height=2)
button_run.place(relx=0.5, rely=0, anchor="n")
button_run.config(relief=tk.RAISED)

text_code = tk.Text(frame_code, wrap=tk.WORD, font=("Consolas", 12), fg="#FFFFFF", bg="#1E1E1E")
text_code.place(relx=0.05, rely=0.05, relwidth=0.4, relheight=0.9)

label_console = tk.Label(frame_console, text="Console", bg="#2D2D2D", fg="#FFFFFF")
label_console.place(relx=0.5, rely=0.05, anchor="n")

text_console = tk.Text(frame_console, wrap=tk.WORD, font=("Consolas", 12), fg="#FFFFFF", bg="#1E1E1E", state=tk.DISABLED)
text_console.place(relx=0.55, rely=0.05, relwidth=0.4, relheight=0.9)
text_console.config(fg="#DDDDDD")

try:
    ruby_icon = Image.open("../src/ruby_icon.png")
    ruby_icon = ruby_icon.resize((48, 48), resample=Image.BILINEAR)
    ruby_icon = ImageTk.PhotoImage(ruby_icon)
    label_icon = tk.Label(frame_code, image=ruby_icon)
    label_icon.place(relx=0.85, rely=0.05)
except FileNotFoundError:
    print("Icono Ruby no encontrado.")

def clear_console():
    text_console.config(state=tk.NORMAL)
    text_console.delete(1.0, tk.END)
    text_console.config(state=tk.DISABLED)

button_clear = tk.Button(frame_console, text="Clear Console", command=clear_console)
button_clear.place(relx=0.5, rely=0.9)



frame_code.config(highlightthickness=1, highlightbackground="#555555", highlightcolor="#555555", borderwidth=0)
frame_console.config(highlightthickness=1, highlightbackground="#555555", highlightcolor="#555555", borderwidth=0)
root.mainloop()
