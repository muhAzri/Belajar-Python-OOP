class User:
    total = 0

    def __init__ (self, name, email, role):
        self.name = name
        self.email = email
        self.__role = role
        User.total += 1

    def info(self):
        return f"{self.name} - {self.email} - {self.__role}"

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, new_role):
        if self.__role != "user" and self.role != "moderator" :
            self.__role = new_role

    @classmethod
    def setTotal(cls, total):
        cls.total = total

    @classmethod
    def from_string(cls, string_params):
        name , email, role = string_params.split("-")
        return cls(name, email, role)



azri = User("Azri", "Maybeazri@gmail.com", "moderator")

string_params = "Zelda-zelda@gmail.com-admin"

zelda = User.from_string(string_params)

print(zelda.info())