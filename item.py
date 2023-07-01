# Made with <3 by Jacob Terkuc
# Class defining an item in the game

import functions


def new(name):
    print("Creating item...")

    try:
        return Item(name)
    except Exception as ex:
        print("Error during item creation: ", ex)


class Item:
    # Constructor
    def __init__(self, name):
        self.name = name
        self.identifier = functions.generate_id()

    # Getters and Setters
    def get_name(self):
        return self.name

    def get_identifier(self):
        return self.identifier

    def set_name(self, name):
        self.name = name

    @staticmethod
    def set_identifier(*args):
        print("Cannot set identifier of item. Identifier is generated automatically.")

    # Other functions
    def __str__(self):
        return "Item: " + self.name + "\n" + "ID: " + self.identifier + "\n"
