class Person:
    ID = 0

    def __init__(self, first_name: str, last_name: str, year: int, month: int, day: int) -> None:
        self.name = f'{first_name}, {last_name}'
        self._year = year
        self._month = month
        self._day = day
        Person.ID += 1

    def repr(self):
        return f"<Person: {self.first_name}"

    def str(self):
        return f"<Person: {{name={self.first_name}, {self.last_name}, age={self.age}}}"

    # @property
    # def age(self):
    #     return self.age

    # @age.setter
    # def age(self, year):
    #     if age < 18:
    #         raise ValueError("This website is info is strictly for 18+")
    #     self.age = 2022 - year

    @property
    def age(self):
        return self.age

    @age.deleter
    def age(self):
        print("Age deleted")
        del self.age

    @classmethod
    def get_nun_of_id(cls):
        return cls.ID

    @staticmethod
    def get_age(self):
        return 2022 - self._year


p1 = Person("akin", "tayo", 1990, "april", 22)
print(Person.ID)
