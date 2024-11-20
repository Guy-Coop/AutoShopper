import tkinter as tk


class IngredientDisplay(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        label = tk.Label(self, text="Ingredient Display", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(
            self,
            text="Go to Start Page",
            command=lambda: controller.show_frame("StartPage"),
        )
        button.pack()
