# 'World' class definition used to store information about the world such as a list of characters, a description of the
# type of game world, and a string of possible locations.
import functions
import settings, pickle


# Function that loads a 'world' object from a file
def load(filename):
    try:
        with open("save/" + filename + ".world", "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)


# Function that takes a string 'name' and returns a 'world' object with the name 'name'. If 'name' is not provided,
# the function will default to creating a world with a random generated name.
def new(name=functions.generate(settings.default_world_generation_prompt)):
    print("Creating world...")
    return World(name)


class World:
    # Constructor
    def __init__(self, name):
        self.name = name
        self.characters = {}
        self.locations = {}
        self.items = {}

    # Getters and Setters

    def get_characters(self):
        return self.characters

    def get_locations(self):
        return self.locations

    def get_items(self):
        return self.items

    # TODO: Remove 'set' functions
    def set_characters(self, characters):
        self.characters = characters

    def set_locations(self, locations):
        self.locations = locations

    def set_items(self, items):
        self.items = items

    # Other functions

    # TODO: Change the add and remove functions to add and remove from dictionaries
    def add_character(self, c):
        self.characters.append(c)

    def remove_entity(self, entity):
        self.characters.remove(entity)

    def add_location(self, location):
        self.locations.append(location)

    def remove_location(self, location):
        self.locations.remove(location)

    def add_item(self, item):
        self.items[item.get_identifier()] = item
        print("Added item '" + str(item.get_name()) + "' with identifier '" + str(item.get_identifier()) + "'")
        return item.get_identifier()

    def remove_item(self, item):
        del self.items[item.get_identifier()]
        print("Removed item with identifier: " + str(item.get_identifier()))
        return item.get_identifier()

    def __str__(self):
        return "World: " + str(self.name) + "\n" + "\n" + "Characters: " + str(self.characters) + ", Items: " + \
        str(self.items)

    # Function that saves the 'world' object to a file 'filename'
    def save(self, filename):
        try:
            with open("save/" + filename + ".world", "wb") as f:
                pickle.dump(self, f)
        except Exception as ex:
            print("Error during pickling object:", ex)
