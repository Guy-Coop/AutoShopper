import tkinter as tk
from lib.backend.recipe import load_all_recipes, Recipe
from PIL import Image, ImageTk
from pathlib import Path
ASSETS_PATH = Path(__file__).parent.parent.parent.parent / "recipes" / "assets"

class RecipeSelector(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        label = tk.Label(self, text="Recipe Selector", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button_home = tk.Button(
            self,
            text="Back to Home",
            command=lambda: controller.show_frame("StartPage"),
        )
        button_home.pack()

        # load all the recipes from file and display them as squares 250x250 with the recipe name, a tick box, and an image if the recipe contains the "image" key
        self.recipes = load_all_recipes()

        # display the recipes in a grid 2 wide
        for recipe in self.recipes.values():
            recipe_frame = tk.Frame(self)
            recipe_frame.pack()
            recipe_label = tk.Label(recipe_frame, text=recipe.name)
            recipe_label.pack()
            recipe_image_fname = recipe.image if recipe.image else "default.png"

            # if the image is not 1:1 aspect ratio then crop it to 1:1
            recipe_image = Image.open(ASSETS_PATH / recipe_image_fname)
            if recipe_image.width != recipe_image.height:
                recipe_image = recipe_image.crop((0, 0, min(recipe_image.width, recipe_image.height), min(recipe_image.width, recipe_image.height)))
            recipe_image.thumbnail((250, 250))
            recipe_image = ImageTk.PhotoImage(recipe_image)
            recipe_image_label = tk.Label(recipe_frame, image=recipe_image)
            recipe_image_label.image = recipe_image
            recipe_image_label.pack()
            recipe_checkbox = tk.Checkbutton(recipe_frame)
            recipe_checkbox.pack()




