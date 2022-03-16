class Employee:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def give_birthday(self) -> None:
        self.age = self.age + 1
