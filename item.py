import functions


class Item:
    # Constructor
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    # Getters and Setters
    def get_name(self):
        return self.name

    def get_desc(self):
        return self.desc

    def set_name(self, name):
        self.name = name

    def set_desc(self, desc):
        self.desc = desc

    # Other functions
    def __str__(self):
        return "Item: " + self.name + "\n" + "Description: " + self.desc + "\n"
