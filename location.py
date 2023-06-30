# Location class

import ast, functions, settings

city_location_generation_prompt = (
    "You are tasked with creating a city in a " + settings.game_style + "setting. The output of your response "
    "should be a python list with the first index being only the name of the city, and the second being a "
    "short (around 20 words) description of the city. An example output would be: "
    "'['Centretown', 'Centretown is a clean and peaceful city full of life and kind people.']'."
)

area_location_generation_prompt = (
    "You are tasked with creating an area in a " + settings.game_style + "setting. The output of your response "
    "should be a python list with the first index being only the name of the area, and the second being a "
    "short (around 20 words) description of the area. An example output would be: "
    "'['Serene Forest', 'Serene forest is a calm and peaceful forest, but look out, "
    "because the monsters come out at night.']'."
)

other_location_generation_prompt = (
    " The output of your response should be a python list with the first index being only the name of the location, "
    "and the second being a short (around 20 words) description of the location. An example output would be: "
    "'['Danger Lakes', 'Danger lakes is not a safe part of town. The lake is full of dangerous creatures, "
    "as well as Jimbob, so look out for him.']'."
)


# There are a few ways to call the new function for generating a location:
# 1. new('city') - Generates a city location
# 2. new('area') - Generates an area location
# 3. new(*Insert Description*) - Generates a location based on the string input.
def new(location_type=""):
    print("Creating location...")

    # If no description is provided, generate a random location
    if location_type == "city":
        x = ast.literal_eval(
            functions.generate([{"role": "system", "content": city_location_generation_prompt}])
                                ["choices"][0]['message']['content'])

    elif location_type == "area":
        x = ast.literal_eval(
            functions.generate([{"role": "system", "content": area_location_generation_prompt}])
                                ["choices"][0]['message']['content'])

    elif location_type == "":
        x = ast.literal_eval(
            functions.generate([{"role": "system", "content": "You are tasked with creating a " + location_type +
                                "in a " + settings.game_style + "setting." + other_location_generation_prompt}])
                                ["choices"][0]['message']['content'])

    # If a description is provided, generate a character based on the description
    else:
        x = ast.literal_eval(
            functions.generate([{"role": "system", "content": "You are tasked with creating a " + location_type +
                                "in a " + settings.game_style + "setting." + other_location_generation_prompt}])
                                ["choices"][0]['message']['content'])

    print(x)

    return Location(x[0], x[1])


class Location:

    # Constructors
    # Takes a string name
    def __init__(self, name, description):
        self.name = name
        self.description = description

    # Getters and Setters

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    # String representation of the object

    def __str__(self):
        return "Location: " + self.name + ", Description: " + self.description + "\n"
