class Company:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.bus = []
        self.routes = []
        self.driver = []
        self.counter = []
        self.manager = []
        self.fare = []
        self.supervisor = []


class Driver: 
    def __init__(self, name , license, age) -> None:
        self.name  = name
        self.license = license 
        self.age = age
        