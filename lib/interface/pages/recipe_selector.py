import tkinter as tk


class RecipeSelector(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        label = tk.Label(self, text="Recipe Selector", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button_home = tk.Button(
            self,
            text="Go to Start Page",
            command=lambda: controller.show_frame("StartPage"),
        )
        button_home.pack()

        button_ingredient = tk.Button(
            self,
            text="Go to Ingredient Display",
            command=lambda: controller.show_frame("IngredientDisplay"),
        )
        button_ingredient.pack()
