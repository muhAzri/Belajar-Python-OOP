class User:
    def __init__ (self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

zelda = User("Azri", "maybeazri@gmail.com", 'Admin')

print(zelda.name)
print(zelda.email)
print(zelda.role)