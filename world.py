# 'World' class definition used to store information about the world such as a list of entities, a description of the
# type of game world, and a string of possible locations.
import settings


class World:
    # Constructor
    def __init__(self, entities, desc, locations):
        self.entities = entities
        self.desc = desc
        self.locations = locations

    def __init(self):
        self.entities = settings.default_entities
        self.desc = settings.default_desc
        self.locations = settings.default_location

    # Getters and Setters

    def get_entities(self):
        return self.entities

    def get_desc(self):
        return self.desc

    def get_locations(self):
        return self.locations

    def set_entities(self, entities):
        self.entities = entities

    def set_desc(self, desc):
        self.desc = desc

    def set_locations(self, locations):
        self.locations = locations

    # Other functions

    def add_entity(self, entity):
        self.entities.append(entity)

    def remove_entity(self, entity):
        self.entities.remove(entity)

    def add_location(self, location):
        self.locations.append(location)

    def remove_location(self, location):
        self.locations.remove(location)

    def __str__(self):
        return "World: " + self.desc + "\n" + "Locations: " + self.locations + "\n" + "Entities: " + str(self.entities)
