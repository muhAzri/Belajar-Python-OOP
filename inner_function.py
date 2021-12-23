class Game:
    def __init__ (self, title, price):
        self.title = title
        self.price = price

    def info(self):
        def print_title():
            return f"Title : {self.title}"
            
        def print_price():
            return f"Price : {self.price}"

        return print_title

zelda = Game("Breath of The Wild", 69)
zelda.info()

title = zelda.info()
print(title)

print(title())