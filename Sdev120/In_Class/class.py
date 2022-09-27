from importlib.util import spec_from_file_location
from shutil import SpecialFileError
from tokenize import Special


class Pet:
    def __init__(self, breed, color, species, name,):
        self.breed = breed
        self.color = color
        self.species = species
        self.name = name


def main():
    pets = []
    breed = input("What breed is your pet?: ")
    color = input("What color is your pet?: ")
    species = input("What species is your pet?: ")
    name = input("What is your pets name?: ")
    pets.append(Pet(breed, color, species, name))
    print(f"{pet1.name} is a {pet1.species}, and is the color {pet1.color} {pet1.breed}")

if __name__ =="__main__":
    main()