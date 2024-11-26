import tkinter as tk
import analizadores.analizador_lexico as lexical
import analizadores.analizador_sintactico as syntax
import sys

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
        lexical.lexer.input(text_input)
        for token in lexical.lexer:
            print(token)
        lexical.lexer.lineno = 1
        syntax.parser.parse(text_input)
        lexical.lexer.lineno = 1
    except Exception as e:
        print(f"Error: {e}")
    sys.stdout = sys.__stdout__
    text_console.config(state=tk.DISABLED)

def on_run():
    input_text_content = text_code.get(1.0, tk.END)
    run_ruby(input_text_content)

root = tk.Tk()
root.title("Analizador de ruby")

frame_code = tk.Frame(root, bg="darkgrey")
frame_console = tk.Frame(root, bg="darkgrey")

frame_code.grid(row=0, column=0, sticky="nsew")
frame_console.grid(row=0, column=1, sticky="nsew")

root.grid_columnconfigure(0, weight=3)
root.grid_columnconfigure(1, weight=2)
root.grid_rowconfigure(0, weight=1)

button_run = tk.Button(frame_code, text="Run", bg="red", fg="white", command=on_run, width=8, height=2)
button_run.place(relx=0.5, rely=0, anchor="n")

text_code = tk.Text(frame_code, wrap=tk.WORD, bg="lightgrey", fg="black")
text_code.place(relx=0.5, rely=0.1, anchor="n", relwidth=0.9, relheight=0.9)

label_console = tk.Label(frame_console, text="Console", bg="darkgrey", fg="black")
label_console.place(relx=0.5, rely=0.05, anchor="n")

text_console = tk.Text(frame_console, wrap=tk.WORD, bg="lightgrey", fg="black", state=tk.DISABLED)
text_console.place(relx=0.5, rely=0.15, anchor="n", relwidth=0.9, relheight=0.8)

root.mainloop()
