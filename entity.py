# Class defining an entity in the game

import functions

msg = "The response to the following query needs to be in the format of a python list. It should be laid " \
      "out in the following way: [NAME(String), RACE(String), ROLE(String), HEALTH(Int), ATTACK(Int), DEFENCE(Int), INVENTORY(List), LOCATION(String)]. As " \
      "additional context, 'race' can be things like 'human', 'dog', 'horse' etc. depending on the contents of the " \
      "message. 'role' is the job or role the entity serves, 'health', 'attack', and 'defence' are all to be defined " \
      "in the following message. 'inventory' is an empty list, and 'location' is the zone the entity is in. I am " \
      "making a character in a fantasy based RPG game. "


def create_character(c):
    print("CREATE")

    c = "The character's name is John, and he is a human farmer. He has 100 health, 10 attack, and 10 defense. He has" \
        + "a torch, and a bottle of water in his inventory, and is currently in centretown."

    t = functions.generate([{"role": "system", "content": msg}, {"role": "user", "content": c}])

    return t['choices'][0]['message']['content']


class Entity:
    # Constructor

    def __init__(self, name, race, role, health, attack, defense, inventory, location):
        self.name = name
        self.race = race
        self.role = role
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = inventory
        self.location = location

    # Getters and Setters

    def get_name(self):
        return self.name

    def get_race(self):
        return self.race

    def get_role(self):
        return self.role

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

    def set_race(self, race):
        self.race = race

    def set_role(self, role):
        self.role = role

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
        return "Entity: " + self.name + ", Role: " + self.role + ", Health: " + str(self.health) + ", Attack: " + str(
            self.attack) + ", Defense: " + str(self.defense) + ", Inventory: " + str(self.inventory) + ", Location: " \
            + str(self.location)

    # Function to generate a new entity
