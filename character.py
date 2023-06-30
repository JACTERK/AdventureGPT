# Class defining a character in the game

import functions, pickle, settings, ast

character_details = "[NAME(String), ROLE(String), PERSONALITY(string), HEALTH(Int), ATTACK(Int), DEFENCE(Int), " \
                    "INVENTORY(List), LOCATION(String)]"

character_generation_prompt = (
        "You are tasked to make up a character in a " + settings.game_style + "-style game." +
        "Output your response as a python list, with the list laid out like: " + str(character_details) + "An " +
        "example of a character that you could create is: ['John', 'John is a farmer who lives in Centretown. " +
        "He loves nature, and frequently likes going on walks through nature. He is kind and responds to other " +
        "characters in a kind and relaxed tone.' 'Farmer', 100, 10, 10, ['shovel', 'water bottle'], 'Centretown']. " +
        "As additional context, NAME is the name of the character, ROLE is the job that the character is tasked " +
        "to do, PERSONALITY is a short  'role' is the job or role the entity serves, HEALTH, ATTACK, " +
        "and DEFENCE are attributes that you can pick based on the character's ROLE. INVENTORY is a list of " +
        "items the character may have based on their ROLE, PERSONALITY is a description of the character, " +
        "and can be anything, as long as it details at least 100 words about the character's personality. For " +
        "the LOCATION, choose a location that would fit the ROLE that the entity has (ex. A farmer would be " +
        "located in a more rural area).You can pick from the following cities/zones: " +
        str(settings.default_location) + ". Additionally, DO NOT USE APOSTROPHES IN YOUR RESPONSE. "
        )


# TODO: Possibly remove in place of the world load function
# Function that takes a filename and returns the object stored in the file
def load(filename):
    try:
        with open("save/" + filename + ".p", "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)


# Function that takes an integer 'num', and an optional string 'desc' and returns a list of 'num' character.
# If 'desc' is not provided, it will default to creating 'num' random character of type 'race'.
# If 'num' is not provided, the function will default to creating and returning a single character object.
def new(desc=""):
    print("Creating character...")

    # If no description is provided, generate a random character
    if desc == "":
        x = ast.literal_eval(
            functions.generate([{"role": "system", "content": character_generation_prompt}])
            ["choices"][0]['message']['content'])

    # If a description is provided, generate a character based on the description
    else:
        x = ast.literal_eval(
            functions.generate([{"role": "system", "content": desc}])
            ["choices"][0]['message']['content'])

    print(x)

    return Character(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7])


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

    # TODO: Possibly remove this function to have the character saved in the world object.
    # Save the character to a file named after the character's name
    def save(self):
        pickle.dump(self, open("save/" + self.name + ".p", "wb"))
        print("Saved character to file: " + self.name + ".p")
