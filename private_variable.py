class User:
    total = 0

    def __init__ (self, name, email, role):
        self.name = name
        self.email = email
        self.__role = role
        User.total += 1

    def info(self):
        return f"{self.name} - {self.email} - {self.__role}"

    def update_role(self, new_role):
        if self.__role != "user" :
            self.__role = new_role

    def getRole(self):
        return self.__role


azri = User("Azri", "Maybeazri@gmail.com", "admin")
# print(azri.info())
# azri.update_role('Superior Admin')
# print(azri.info())

print(azri.__dict__)
print(azri._User__role)
print(azri.getRole)

