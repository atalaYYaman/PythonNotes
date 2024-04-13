#EXERCİSE 1
class CelestialBody:
    def __init__(self, name, diameter, distance, moons):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.moons = moons

    def compared_to_earth(self):
        earth = 12756.3
        relative_size = self.diameter / earth
        return relative_size


planet = CelestialBody("Jupiter", 142984, 778360000, 79)
print(planet.compared_to_earth())


#EXERCİSE 2
class Library:
    def __init__(self):
        self.available = []
        self.on_loan = []

    def add_books(self, book_titles):
        self.available.extend(book_titles)

    def borrow_book(self, book_title):
        if book_title in self.available:
            self.available.remove(book_title)
            self.on_loan.append(book_title)
        else:
            print(f"{book_title} is not available for borrowing.")

    def return_book(self, book_title):
        if book_title in self.on_loan:
            self.on_loan.remove(book_title)
            self.available.append(book_title)
        else:
            print(f"{book_title} is not currently on loan.")


my_library = Library()

my_library.add_books(["Four Seasons", "Say Nothing", "Milkman", "Harry Potter and the Order of the Phoenix"])

print("Available books:", my_library.available)

my_library.borrow_book("Harry Potter and the Order of the Phoenix")
my_library.borrow_book("Say Nothing")

print("Available books:", my_library.available)
print("Books on loan:", my_library.on_loan)

my_library.return_book("Say Nothing")

print("Available books:", my_library.available)
print("Books on loan:", my_library.on_loan)


#EXERCİSE 3
class Subway:
    fare = 2.4

    def __init__(self):
        self.stops = ["Alewife", "Davis", "Porter", "Harvard", "Central", "Kendall"]
        self.current_stop = "Alewife"
        self.passengers = 0
        self.total_fares = 0

    def board(self, num_passengers):
        self.passengers += num_passengers
        self.total_fares += num_passengers * self.fare

    def disembark(self, num_passengers):
        if num_passengers >= self.passengers:
            self.passengers = 0
        else:
            self.passengers -= num_passengers

    def distance(self, desired_stop):
        current_index = self.stops.index(self.current_stop)
        desired_index = self.stops.index(desired_stop)
        return abs(desired_index - current_index)


subway = Subway()

subway.board(45)
print("Total passengers after boarding:", subway.passengers)
print("Total fares collected:", subway.total_fares)

subway.disembark(23)
print("Total passengers after disembarking:", subway.passengers)

current_stop = "Davis"
desired_stop = "Central"
print("Distance between", current_stop, "and", desired_stop, "is", subway.distance(desired_stop), "stops.")
