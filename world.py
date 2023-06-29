# 'World' class definition used to store information about the world such as a list of characters, a description of the
# type of game world, and a string of possible locations.
import settings


class World:
    # Constructor
    def __init__(self, characters, desc, locations):
        self.characters = characters
        self.desc = desc
        self.locations = locations

    def __init(self):
        self.characters = settings.default_characters
        self.desc = settings.default_desc
        self.locations = settings.default_location

    # Getters and Setters

    def get_characters(self):
        return self.characters

    def get_desc(self):
        return self.desc

    def get_locations(self):
        return self.locations

    def set_characters(self, characters):
        self.characters = characters

    def set_desc(self, desc):
        self.desc = desc

    def set_locations(self, locations):
        self.locations = locations

    # Other functions

    def add_entity(self, entity):
        self.characters.append(entity)

    def remove_entity(self, entity):
        self.characters.remove(entity)

    def add_location(self, location):
        self.locations.append(location)

    def remove_location(self, location):
        self.locations.remove(location)

    def __str__(self):
        return "World: " + self.desc + "\n" + "Locations: " + self.locations + "\n" + "Characters: " + str(self.characters)
