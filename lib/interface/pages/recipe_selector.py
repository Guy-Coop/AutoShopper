from ._page import Page
import tkinter as tk
class RecipeSelector(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        label = tk.Label(self, text="Recipe Selector")
        label.pack(side="top", fill="both", expand=True)

