
class animals:
    name = 'animals'
    weight = 0
    def feed(self,animalss = 'Животное'):
        self.animalss = animals
        print(f"Покормить {animalss}")
    def vote(self,votes = "Животного"):
        self.votes = votes
        print(f"Голос {votes}")
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class bird(animals):
    def collect_eggs(self):
        print("Собираем яйца")

class mammals(animals):
    def milk(self):
        print("Доить")

class goose(bird):
    def vote(self, votess = "Гуся"):
        super().vote("Гуся")
        print("Га-га-га")
    def feed(self):
        super().feed("гуся")

class duck(bird):
    def vote(self, votess = "Утки"):
        super().vote("Утки")
        print("Кря-кря")
    def feed(self):
        super().feed("утку")

class chicken(bird):
    def vote(self, votess = "Курицы"):
        super().vote("Курицы")
        print("Куд-куда")
    def feed(self):
        super().feed("курицу")

class goat(mammals):
    def vote(self, votess = "Коза"):
        super().vote("Козы")
        print("Ме-ме-ме")
    def feed(self):
        super().feed("козу")

class cow(mammals):
    def vote(self, votess="Корова"):
        super().vote("Коровы")
        print("Му-му-му")
    def feed(self):
        super().feed("корову")

class sheep(animals):
    def vote(self, votess = "Овца"):
        super().vote("Овцы")
        print("Бе-бе-бе")
    def feed(self):
        super().feed("овцу")
    def shave(self):
        print("Стричь овцу")

goose1 = goose("Серый", 1)
goose2 = goose("Белый", 1)
cow1 = cow("Манька", 90)
sheep1 = sheep("Барашек",25)
sheep2 = sheep("Кудрявый", 30)
chicken1 = chicken("Ко-Ко",2)
chicken2 = chicken("Кукареку",2)
goat1 = goat("Рога",20)
goat2 = goat("Копыта",22)
duck1 = duck("Кряква",5)

All_weight = goose1.weight + goose2.weight + cow1.weight + \
             sheep1.weight + sheep2.weight + chicken1.weight + \
             chicken2.weight + goat1.weight + goat2.weight + duck1.weight

print(f"Общий вес всех животных: {All_weight}")

list_animals = [goose1, goose2, cow1,
                sheep1, sheep2, chicken1,
                chicken2, goat1, goat2, duck1]

weight = 0
test_name = ''
for animal in list_animals:
    if animal.weight > weight:
        weight = animal.weight
        test_name = animal.name
print(f"Самое тяжелое животное: {test_name}")
