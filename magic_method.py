class Game:
    def __init__ (self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"{self.title} - ${self.price}"

    def __eq__(self, other):
        return self.title == other.title

    def __gt__(self, other):
        return self.price > other.price

    def __add__(self, other):
        return self.price + other.price
    

zelda = Game("Breath of The Wild", 69)
zelda2 = Game("Breath of The Wild", 90)
mario = Game("Mario Bross", 65)


print(zelda + zelda2)