import random


brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},
}
job_list = {
 "Java developer": {"salary": 50, "gladness_less": 10},
 "Python developer": {"salary": 40, "gladness_less": 3},
 "C++ developer": {"salary": 45, "gladness_less": 25},
 "Rust developer": {"salary": 70, "gladness_less": 1},
}
cat_breeds = {
    "Siamese": {"feed": 10, "price": 25, "playfulness": 10},
    "Bengal": {"feed": 7, "price": 30, "playfulness": 8},
    "Persian": {"feed": 12, "price": 20, "playfulness": 9},
}


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None, cat=None):
        self.name = name
        self.money = 180
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.power = 30
        self.fatigue = 0
        self.cat = cat

    def time_with_cat(self):
        if self.cat.feed < 4:
            print("My cat want eat! I feed my cat.")
            self.cat.eat()
        else:
            print("My cat wants to play!")
            self.cat.play()
        self.gladness += 1

    def meet_with_fr(self):
        self.money -= 2
        self.gladness += 10

    def go_restaurant(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money -= 30
        self.gladness += 30
        self.satiety += 5

    def walk(self):
        self.gladness += 1
        self.satiety -= 1
        self.fatigue -= 2

    def vacation(self):
        self.money -= 500
        self.fatigue = 0
        self.gladness += 200
        self.power -= 5

    def go_concert(self):
        self.money -= 40
        self.gladness += 15
        self.fatigue -= 1

    def do_sports(self):
        self.money -= 15
        self.gladness -= 2
        self.satiety -= 5
        self.power += 2
        self.fatigue += 2

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def buy_cat(self):
        self.cat = Cat(cat_breeds)
        self.money -= self.cat.price

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        elif self.gladness <= 30 and self.money >= 140:
            print("I can eat in a restaurant!")
            self.go_restaurant()
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5
            self.fatigue -= 1

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4
        self.power -= 1
        self.fatigue += 5

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
        self.power -= 1
        self.fatigue -= 3

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
        self.fatigue += 1

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        print(f"Power - {self.power}")
        print(f"Fatigue - {self.fatigue}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")
        cat_indexes = f"{self.cat.breed} cat indexes"
        print(f"{cat_indexes:^50}", "\n")
        print(f"Feed - {self.cat.feed}")
        print(f"Playfulness - {self.cat.playfulness}")


    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            return False
        if self.money < -500:
            print("Bankrupt…")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.cat is None:
            self.buy_cat()
            print(f"I bought a cat {self.cat.breed} for {self.cat.price} $")
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, I'm going to get a job {self.job.job} with salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1, 10)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…\nSo I will clean the house")
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif self.power < 0:
            print("I have to go to the gym!")
            self.do_sports()
        elif self.fatigue > 100 and self.money > 600:
            print("I'm very tired. Me need a vacation")
            self.vacation()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")
        elif dice == 5:
            print("Time for sports")
            self.do_sports()
        elif dice == 6:
            print("I'm going to a concert!!!")
            self.go_concert()
        elif dice == 7:
            print("I'm going for a walk!")
            self.walk()
        elif dice == 8:
            print("I'll meet my friends")
            self.meet_with_fr()
        elif dice == 9:
            print(f"Time for my {self.cat.breed}")
            self.time_with_cat()

class Cat():
    def __init__(self, cat_breeds):
        self.breed = random.choice(list(cat_breeds))
        self.feed = cat_breeds[self.breed]["feed"]
        self.price = cat_breeds[self.breed]["price"]
        self.playfulness = cat_breeds[self.breed]["playfulness"]

    def play(self):
        self.feed -= 1
        self.playfulness += 2

    def eat(self):
        self.feed += 3


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


vadim = Human(name="Vadim")
for day in range(1, 365):
    if vadim.live(day) == False:
        break