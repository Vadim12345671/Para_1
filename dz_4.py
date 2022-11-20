class Woman:
    height = 160
    weight = 55
    gender = "Female"

    def __init__(self):
        self.height = 155
        self.weight = 45
        self.gender = "Female"


class Man:
    height = 180
    weight = 80
    gender = "Male"

    def __init__(self):
        self.height = 170
        self.weight = 65
        self.gender = "Male"


class Child:
    year = 15


class Adults:
    year = 35


class Elderly:
    year = 70


class Dad(Man, Adults):
    def __init__(self):
        super().__init__()
        print(f"Dad height is {super().height} cm")
        print(f"Dad weight is {super().weight} kg")
        print(f"Dad is {self.year} years old")
        print(f"Dad gender is {self.gender}")


class Son(Man, Child):
    def __init__(self):
        super().__init__()
        print(f"Son height is {self.height} cm")
        print(f"Son weight is {self.weight} kg")
        print(f"Son is {self.year} years old")
        print(f"Son gender is {self.gender}")


class Mother(Woman, Adults):
    def __init__(self):
        super().__init__()
        print(f"Mother height is {super().height} cm")
        print(f"Mother weight is {super().weight} kg")
        print(f"Mother is {self.year} years old")
        print(f"Mother gender is {self.gender}")


class Daughter(Woman, Child):
    def __init__(self):
        super().__init__()
        print(f"Daughter height is {self.height} cm")
        print(f"Daughter weight is {self.weight} kg")
        print(f"Daughter is {self.year} years old")
        print(f"Daughter gender is {self.gender}")


print("______Dad______")
dima = Dad()
print("______Son______")
vasya = Son()
print("______Mother______")
vika = Mother()
print("______Daughter______")
liza = Daughter()
