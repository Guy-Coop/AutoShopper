import tkinter as tk
from ..common_components.title_bar import TitleBar
class IngredientDisplay(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        # create a home button with a home icon stored in ./assets/home.png
        title_bar = TitleBar(self, controller, "Ingredient Display", show_home_button=True)
        title_bar.pack(side="top", fill="x")

        label = tk.Label(self, text="Create a new recipe", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
