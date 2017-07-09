#! /bin/env python3

import tkinter as tk
import fiche_perso
from tinydb import TinyDB, Query

jdr_name = "JDR_test"

class ConfigMenu(tk.Frame):
    def __init__(self, master=None):
        self.master = master
        super().__init__(master)
        self.pack()
        self.master.title("Options")
        self.create_widgets()

    def create_widgets(self):
        self.text = tk.Button(self, text="Plop")
        self.text.pack(side="top")
        self.back_main = tk.Button(self, text="Menu Principal", command=self.back_menu)
        self.back_main.pack(side="top")

    def back_menu(self):
        app = init_menu(self)


class MainMenu(tk.Frame):
    def __init__(self, master=None):
        self.master = master
        super().__init__(master)
        self.pack()
        self.master.title("Menu Principal")
        self.create_widgets()

    def create_widgets(self):
        self.fiches = tk.Button(self, text="Fiches Personnages", command = self.list_fiches)
        self.fiches.pack(side="top")
        self.config = tk.Button(self, text="Options", command = self.show_config)
        self.config.pack(side="top")
        self.quit = tk.Button(self, text="QUITTER", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def show_config(self):
        self.destroy()
        app = ConfigMenu(master=root)

    def list_fiches(self):
        self.destroy()
        app = fiche_perso.ListeFiches(init_menu,jdr_name, master=root)



root = tk.Tk()

def init_menu(arg = None):
    if arg: arg.destroy()
    return MainMenu(master=root)

app = init_menu()
app.mainloop()
