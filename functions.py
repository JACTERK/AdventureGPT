# Made with <3 by Jacob Terkuc

import openai, os, ast
import settings, character
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


# This function takes a library 'msg' and calls the OpenAI API to generate a response.
# It returns the response as a string.
def generate(msg):
    print("Generating response...")
    print(msg)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=msg,
    )
    return response


# Function that takes an integer 'num', and an optional string 'desc' and returns a list of 'num' entities.
# If 'desc' is not provided, it will default to creating 'num' random entities of type 'race'.
def create_entities(num, desc=""):
    print("Creating entities...")
    entities = []
    e_calls = []

    character_details = "[NAME(String), ROLE(String), PERSONALITY(string), HEALTH(Int), ATTACK(Int), DEFENCE(Int), " \
                        "INVENTORY(List), LOCATION(String)]"

    prompt = "You are tasked to make up " + str(num) + " entities in a " + settings.game_style + "-style game. " \
             + "Output your responses as a list of python lists, the length of the list being the number of " \
             + "entities needing to be created, and each of the nested lists laid out like: " \
             + character.character_details \
             + "Make sure none of the characters you create identical, and that they are all unique. An " \
             + "example of a character that you could create is: ['John', 'Human', 'Farmer', 100, 10, 10, [], " \
             + "'Centretown']. As additional context, NAME is the name of the character, ROLE is the job that the character is tasked to do, PERSONALITY is a short  'role' is the job or role the entity serves, 'health', 'attack', and 'defence' are all to be defined in the following message. 'inventory' is an empty list, and 'location' is the zone the entity is in. The PERSONALITY is a description of the character, and can be anything, as long as it details at least 100 words about the character's personality.For the LOCATION, choose a location that would fit the ROLE that the entity has (ex. A farmer would be located in a more rural area).You can pick from the following cities/zones: " + settings.default_location

    p = [{"role": "system", "content": prompt}]

    return generate(p)

    # return entities
