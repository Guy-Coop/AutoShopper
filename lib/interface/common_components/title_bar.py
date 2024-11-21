import tkinter as tk
from .home_button import HomeButton
# create a top bar that has the title, and optionally a home button to the left of the title

class TitleBar(tk.Frame):
    def __init__(self, parent, controller, title, show_home_button=True, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        self.title = title

        offset = 0
        if show_home_button:
            home_button = HomeButton(self, controller)
            home_button.pack(side="left")
            offset = home_button.winfo_reqwidth() * 2

        label = tk.Label(self, text=self.title, font=controller.title_font)
        # pack the label so it is always in the center of the whole frame
        label.pack(side="left", padx=offset)