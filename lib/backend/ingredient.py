from dataclasses import dataclass


@dataclass
class Ingredient:
    name: str
    amount: float = 1
    unit: str = ""

    def __post_init__(self):
        # ensure consistent capitalisation
        self.name = self.name.title()

    def __add__(self, other):
        if not isinstance(other, Ingredient):
            raise ValueError(f"Cannot add {self.__class__.__name__} and {type(other)}")
        if self.name != other.name:
            raise ValueError(f"Cannot add {self.name} and {other.name}")
        if self.unit != other.unit:
            raise ValueError(f"Cannot add {self.unit} and {other.unit}")

        return Ingredient(self.name, self.amount + other.amount, self.unit)
