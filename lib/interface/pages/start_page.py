import tkinter as tk


class StartPage(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller

        label = tk.Label(self, text="Start Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(
            self,
            text="Go to Recipe Selector",
            command=lambda: controller.show_frame("RecipeSelector"),
        )
        button2 = tk.Button(
            self,
            text="Go to Ingredient Display",
            command=lambda: controller.show_frame("IngredientDisplay"),
        )

        button1.pack()
        button2.pack()
