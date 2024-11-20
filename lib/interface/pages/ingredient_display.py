from ._page import Page
import tkinter as tk
class IngredientDisplay(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        label = tk.Label(self, text="Ingredient Display")
        label.pack(side="top", fill="both", expand=True)

