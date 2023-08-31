class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        return self.name.upper()


    def age(self, current_year):
        return current_year - self.birthyear


user = User("John", 1999)

John = user.age(2023)

print(John)

name = user.get_name()
print(name)