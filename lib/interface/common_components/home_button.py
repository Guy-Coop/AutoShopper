import tkinter as tk
import pathlib
from PIL import Image, ImageTk

ICON_PATH = pathlib.Path(__file__).parent.parent / "assets" / "home.png"
BUTTON_WIDTH = 50
BUTTON_HEIGHT = 50

class HomeButton(tk.Button):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, **kwargs)
        self.controller = controller
        self.config(text="Home", command=lambda: controller.show_frame("StartPage"))
        icon_image = Image.open(ICON_PATH)
        icon_image.thumbnail((BUTTON_WIDTH, BUTTON_HEIGHT))
        self.icon = ImageTk.PhotoImage(icon_image)
        self.config(image=self.icon)