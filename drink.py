"""
Code example for IEEE and being able to utilize an abstract base class
and commit to a repository.

WELCOME TO THE IEEE CAFE!

"""
from abc import ABC, abstractmethod

class Drink(ABC):
    """
    Abtract class for a Drink
    """
    def __init__(self, name: str, price: int, size: str, temp: str):
        """ initialize a drink """
        self.name = name
        self.price = price
        self.size = size
        self.temp = temp

    def __str__(self):
        return f"{self.name} was created! Delicious! :D"
    

    def order_drink(self):
        print(f"\nYour \u2728 {self.size} {self.name} \u2728 is ready!\nCome get it while it's {self.temp} {"\U0001F525" if self.temp.lower() == "hot" else "\U0001F9CA"}! \nThat will be ${self.price:0.2f}... plus tip...")
    