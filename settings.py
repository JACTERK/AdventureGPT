game_style = "fantasy RPG "

demo_characters = []
demo_desc = "A fantasy based RPG game. "
demo_location = "Centretown, Northtown, Southtown, Easttown, Westtown, and the following zones: Forest, Plains, " \
                "Mountains, Desert, and Ocean."

default_characters = []
default_desc = "A fantasy game."
default_location = ""

character_details = "[NAME(String), ROLE(String), PERSONALITY(string), HEALTH(Int), ATTACK(Int), DEFENCE(Int), " \
                    "INVENTORY(List), LOCATION(String)]"
character_generation_prompt = (
        "You are tasked to make up a character in a " + game_style + "-style game." +
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
        str(default_location) + ". Additionally, DO NOT USE APOSTROPHES IN YOUR RESPONSE. "
)


def get_game_style():
    return game_style


def get_demo_characters():
    return demo_characters


def get_demo_desc():
    return demo_desc


def get_demo_location():
    return demo_location


def get_default_characters():
    return default_characters


def get_default_desc():
    return default_desc


def get_default_location():
    return default_location


def get_character_details():
    return character_details


def get_character_gen_prompt():
    return character_generation_prompt
