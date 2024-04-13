#EXERCİSE 1
class PracticeClass:
  pass


#EXERCİSE 2
class Cat:
    def __init__(self):
        self.breed = "american shorthair"
        self.color = "black"
        self.name = "kiwi"

my_cat = Cat()
print("Breed:", my_cat.breed)
print("Color:", my_cat.color)
print("Name:", my_cat.name)


#EXERCİSE 3
class SuperHero:
    def __init__(self, name, secret_identity, powers):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers

spider_man = SuperHero("Spider-Man", "Peter Parker", ["superhuman strength", "superhuman speed", "superhuman reflexes", "superhuman durability", "healing factor", "spider-sense alert", "heightened senses", "wallcrawling"])

print("Superhero name:", spider_man.name)
print("Secret identity:", spider_man.secret_identity)
print("Powers:", spider_man.powers)


#EXERCİSE 4
class Observation:
    def __init__(self, date, temperature, elevation, penguins, precipitation=0):
        self.date = date
        self.temperature = temperature
        self.elevation = elevation
        self.precipitation = precipitation
        self.penguins = penguins

observation1 = Observation("October 26, 2019", -47, 329.4, 3)
print("Observation Date:", observation1.date)
print("Temperature (Celsius):", observation1.temperature)
print("Elevation (meters):", observation1.elevation)
print("Precipitation (cm):", observation1.precipitation)
print("Number of Penguins Observed:", observation1.penguins)


#EXERCİSE 5
class BigCat:
    genus = "panthera"

    def __init__(self, species, common_name, habitat):
        self.species = species
        self.common_name = common_name
        self.habitat = habitat



lion = BigCat("leo", "lion", ["africa"])
tiger = BigCat("tigris", "tiger", ["asia"])

print(lion.genus)
print(tiger.species)
print(lion.habitat)
