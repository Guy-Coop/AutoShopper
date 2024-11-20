import tkinter as tk
from .recipe_selector import RecipeSelector
from .ingredient_display import IngredientDisplay

class StartPage(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        recipe_selector_page = RecipeSelector(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)

        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        recipe_selector_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        button1 = tk.Button(buttonframe, text="Recipe Selector", command=recipe_selector_page.show)

        button1.pack(side="left")

        recipe_selector_page.show()
