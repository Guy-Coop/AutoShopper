# a tkinter interface that allows the user to interact with the program to select recipes, and generate a shopping list.

import tkinter as tk
from tkinter import font

from .pages import StartPage, RecipeSelector, IngredientDisplay


class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title_font = font.Font(
            family="Helvetica", size=18, weight="bold", slant="italic"
        )
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.wm_geometry("500x1000")

        self.pages = {}

        for F in (StartPage, RecipeSelector, IngredientDisplay):
            page_name = F.__name__
            page = F(container, self)
            self.pages[page_name] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        page = self.pages[page_name]
        page.tkraise()


def run_interface():
    root = Interface()
    root.mainloop()
