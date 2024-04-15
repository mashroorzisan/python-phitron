class Animal:
    def __init__(self, name, breaths, moves, eats, sleeps) -> None:
        self.name = name
        self.breaths = breaths
        self.moves = moves
        self.eats = eats
        self.sleeps = sleeps
    def __repr__(self) -> str:
        return f"this one is {self.name}"


class Aquatic(Animal):
    def __init__(self, name, breaths, moves, eats, sleeps, gills) -> None:
        self.gills = gills
        super().__init__(name, breaths, moves, eats, sleeps)
    
    def __repr__(self) -> str:
        return f"this one is {self.name} and has {self.gills}"


class Mammalian(Animal):
    def __init__(self, name, breaths, moves, eats, sleeps, runs, feeds_milk) -> None:
        self.runs = runs
        self.feeds_milk = feeds_milk
        super().__init__(name, breaths, moves, eats, sleeps)
    
    def __repr__(self) -> str:
        return f"this one is {self.name} and feeds on {self.feeds_milk}"


class Apes(Mammalian):
    def __init__(self, name, breaths, moves, eats, sleeps, runs, feeds_milk, two_legged) -> None:
        self.two_legged = two_legged
        super().__init__(name, breaths, moves, eats, sleeps, runs, feeds_milk)
    
    def __repr__(self) -> str:
        return f"this one is {self.name} and feeds on {self.feeds_milk} and they are {self.two_legged}"


class Humans(Apes):
    def __init__(self, name, breaths, moves, eats, sleeps, runs, feeds_milk, two_legged, technological) -> None:
        self.technological = technological
        super().__init__(name, breaths, moves, eats, sleeps, runs, feeds_milk, two_legged)
    
    def __repr__(self) -> str:
        return f"this one is {self.name} and feeds on {self.feeds_milk} and they are {self.two_legged} and they are {self.technological}"



lion = Animal("Lion",True, True, True, True)
print(lion)
fish = Aquatic("Fish", True,True,True,True,"gills")
print(fish)
elephant = Mammalian("Elephant",True,True,True,True,True,"mother's milk")
print(elephant)
Shimpanzee = Apes("Shimpanzee", True,True,True,True,True,"mother's milk", "bipedal")
print(Shimpanzee)
humans = Humans("Humans",True,True,True,True,True,"mother's milk", "bipedal", "the only technologically advanced species on Earth")
print(humans)