#inheritance, extend, override, polymorphism

class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def work(self):
        return f"{self.name} is working"

class Programmer(Employee):
    # Extend
    def __init__(self, name, email, level):
        super().__init__(name, email)
        self.level = level

    def debug(self):
        return "debugging"

    # Override
    def work(self):
        return f"{self.name} is writting Code"

class UiDesigner(Employee):
    # Extend
    def __init__(self, name , email, level, tools):
        super().__init__(name, email)
        self.level = level
        self.tools = tools

    # Override
    def work(self):
        return f"{self.name} is designing new product"

employee = Employee("Azri", "maybeazri@gmail.com")
# print(employee.work())

programmer = Programmer("Muhammad Azri", "maybeazri@gmail.coms", "Junior Programmer")
# print(programmer.work())

designer = UiDesigner("Rizki haddi Prayoga", "maybeazri@gmail.coms", "Junior Ui Designer", " Figma")
# print(designer.work())

# Polymorphism
def working(system):
    print(system.work())

class Manager:
    def __init__ (self, name):
        self.name = name

    def work(self):
        return f"{self.name} is managing"

manager = Manager("Fariz")

working(employee)
working(programmer)
working(designer)
working(manager)