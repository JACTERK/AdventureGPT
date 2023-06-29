# Made with <3 by Jacob Terkuc

import openai, os, ast
import settings, entity
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

    prompt = ("You are tasked to make up " + str(num) + " entities in a " + settings.game_style + "-style game. Output "
              + "your responses as a list of python lists, the length of the list being the number of entities needing"
              + " to be created, and each of the nested lists laid out like: [NAME(String), RACE(String), ROLE(String),"
              + " HEALTH(Int), ATTACK(Int), DEFENCE(Int), INVENTORY(List), LOCATION(String)]. Make sure none of the characters you create identical, and that they are all unique. An example of a character that you could create is: ['John', 'Human', 'Farmer', 100, 10, 10, [], 'Centretown']. For the LOCATION, you can pick from the following cities: " + settings.locations)

    for i in range(num):
        if desc == "":
            entities.append(ast.literal_eval(generate([{"role": "system", "content": prompt},
                                                       {"role": "user",
                                                        "content": "what is your name, and what do you do?"}
                                                       ])))

        else:
            entities.append(ast.literal_eval(generate([{"role": "system", "content": "You are a farmer named john."},
                                                       {"role": "user", "content": desc}
                                                       ])))

    return entities
