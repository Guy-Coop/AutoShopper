import tkinter as tk
from ..common_components.title_bar import TitleBar

class StartPage(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller

        title_bar = TitleBar(self, controller, "Start Page", show_home_button=False)
        title_bar.pack(side="top", fill="x")

        button1 = tk.Button(
            self,
            text="Go to Recipe Selector",
            command=lambda: controller.show_frame("RecipeSelector"),
        )
        button1.pack()
