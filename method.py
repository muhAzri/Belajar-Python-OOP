class User:
    total = 0

    def __init__ (self, name, email, role):
        self.name = name
        self.email = email
        self.role = role
        User.total += 1

    def info(self):
        return f"{self.name} - {self.email} - {self.role}"

    def update_role(self, new_role):
        if self.role != "user" :
            self.role = new_role


azri = User("Azri", "Maybeazri@gmail.com", "admin")
print(azri.info())
azri.update_role('Superior Admin')
print(azri.info())

