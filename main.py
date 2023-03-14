class Bank:
    def __init__(self, name , money, key):
        self.name = name
        self.__money = money
        self.key = key

    def __str__(self):
        return f"{self.name} - {self.__money}"

user = Bank('Kutman', 1000, '123qwe')

