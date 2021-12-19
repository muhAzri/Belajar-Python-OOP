class User:
    total = 0

    def __init__ (self, name, email, role):
        self.name = name
        self.email = email
        self.role = role
        User.total += 1

print(User.total)

zelda = User("Azri", "maybeazri@gmail.com", 'Admin')
print(User.total)

link = User("link", "maybeazri@gmail.com", 'Admin')
print(User.total)

ryan = User("ryan", "maybeazri@gmail.com", 'Admin')
print(User.total)