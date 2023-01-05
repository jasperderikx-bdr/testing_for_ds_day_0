def increment(x: int) -> int:
    return x + 1


class Employee:
    def __init__(self, name: str, age: int, salary: int) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def give_birthday(self) -> None:
        self.age = increment(self.age)

    def give_raise(self) -> None:
        self.salary = increment(self.age)
