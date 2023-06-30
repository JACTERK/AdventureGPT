# Class defining an entity in the game

import functions, pickle

character_details = "[NAME(String), ROLE(String), PERSONALITY(string), HEALTH(Int), ATTACK(Int), DEFENCE(Int), " \
                    "INVENTORY(List), LOCATION(String)]"

msg = "The response to the following query needs to be in the format of a python list. It should be laid " \
      "out in the following way: [NAME(String), ROLE(String), PERSONALITY(String), HEALTH(Int), " \
      "ATTACK(Int), DEFENCE(Int), INVENTORY(List), LOCATION(String)]. As " \
      "additional context, 'race' can be things like 'human', 'dog', 'horse' etc. depending on the contents of the " \
      "message. 'role' is the job or role the entity serves, 'health', 'attack', and 'defence' are all to be defined " \
      "in the following message. 'inventory' is an empty list, and 'location' is the zone the entity is in. The " \
      "PERSONALITY is a description of the character, and can be anything, as long as it details at least " \
      "100 words about the character's personality.."


# Function that takes a filename and returns the object stored in the file
def load_object(filename):
    try:
        with open("save/" + filename + ".p", "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)


class Character:
    # Constructor

    def __init__(self, name, role, personality, health, attack, defense, inventory, location):
        self.name = name
        self.role = role
        self.personality = personality
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = inventory
        self.location = location

    # Getters and Setters

    def get_name(self):
        return self.name

    def get_role(self):
        return self.role

    def get_personality(self):
        return self.personality

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_inventory(self):
        return self.inventory

    def get_location(self):
        return self.location

    def set_name(self, name):
        self.name = name

    def set_role(self, role):
        self.role = role

    def set_personality(self, personality):
        self.personality = personality

    def set_health(self, health):
        self.health = health

    def set_attack(self, attack):
        self.attack = attack

    def set_defense(self, defense):
        self.defense = defense

    def set_inventory(self, inventory):
        self.inventory = inventory

    def set_location(self, location):
        self.location = location

    # String representation of the object

    def __str__(self):
        return "Entity: " + self.name + ", Role: " + self.role + ", Personality: " + self.personality + ", Health: " + str(
            self.health) + ", Attack: " + str(self.attack) + ", Defense: " + str(self.defense) + ", Inventory: " + str(
            self.inventory) + ", Location: " + str(self.location)

    # Save the character to a file named after the character's name
    def save(self):
        pickle.dump(self, open("save/" + self.name + ".p", "wb"))
        print("Saved character to file: " + self.name + ".p")
