"""
Example of creating your own beverage using the abstract base class from the repo!
"""
from drink import Drink


class Coffee(Drink):
    """ Example of creating a subclass of abstract base class of drink"""
    def __init__(self, name: str, price:int, size:str, temp:str, roast:str):
        self.name = name
        self.price = price
        self.size = size
        self.temp = temp
        self.roast = roast # I added roast to my specific coffee drink!

    def coffee_joke(self):
        """ funtion that is unique to Coffee and not under abstract class of Drink"""
        print(f"\nI like my outlook on life the way I like my coffee, bitter. \u2615 \n")


if __name__ == "__main__":
    c = Coffee("Americano", 2.00, "Large", "Hot", "Medium-Dark") # creating my coffee!
    print(c) 
    c.order_drink() # ordering my drink
    c.coffee_joke() # using my coffee function! :)
    