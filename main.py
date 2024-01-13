#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox, filedialog

class Notepad:

    def __init__(self) -> None:
        self.current_file = None
        self.root = tk.Tk()
        self.create_menu()
        self.bind_shortcuts()
        self.create_textarea()
        self.root.mainloop()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        menu_file = tk.Menu(menu_bar, tearoff=0)
        menu_file.add_command(label='New...', command=self.new_action)
        menu_file.add_command(label='Save...', command=self.save_action)
        menu_file.add_command(label='Open...', command=self.open_action)
        menu_file.add_command(label='Close', command=self.close_action)
        menu_file.add_command(label='Exit', command=self.exit_action)

        menu_about = tk.Menu(menu_bar, tearoff=0)
        menu_about.add_command(label='Version', command=self.about_action)

        menu_bar.add_cascade(label="File", menu=menu_file)
        menu_bar.add_cascade(label='About', menu=menu_about)

        self.root.config(menu=menu_bar)

    def bind_shortcuts(self):
        self.root.bind("<Control-s>", self.save_action)
        self.root.bind("<Control-o>", self.open_action)
        self.root.bind("<Control-h>", self.about_action)
        self.root.bind("<Control-q>", self.close_action)
        self.root.bind("<Control-n>", self.new_action)
        self.root.bind("<Alt-F4>", self.exit_action)

    def create_textarea(self):
        self.textarea = tk.Text(self.root, width=100, height=100, padx=5, pady=5)
        self.textarea.pack(fill=tk.BOTH, expand=1)

    def exit_action(self, event = None):
        if messagebox.askokcancel("Exit", "Are you sure to quit?"):
            self.root.destroy()

    def new_action(self, event = None):
        self.close_action()

    def save_action(self, event = None):
        if not self.current_file:
            self.current_file = filedialog.asksaveasfilename(defaultextension=".txt")
            
        with open(self.current_file, "w") as file:
            file.write(self.textarea.get("1.0", tk.END))

            
    def close_action(self, event = None):
        self.current_file = None
        self.textarea.delete("1.0", tk.END)

    def open_action(self, event = None):
        file_path = filedialog.askopenfilename()

        if file_path:
            with open(file_path, "r") as file:
                self.close_action()
                self.textarea.insert("1.0", file.read())
                self.current_file = file_path

    def about_action(self, event = None):
        messagebox.showinfo("About", "TKNotepad v1.0")

if __name__ == "__main__":
    Notepad()

