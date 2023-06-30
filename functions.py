# Made with <3 by Jacob Terkuc

import openai, os, ast, string, random
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


# Function that takes an integer 'num', and an optional string 'desc' and returns a list of 'num' character.
# If 'desc' is not provided, it will default to creating 'num' random character of type 'race'.
def create_character(num=1, desc=""):
    print("Creating character...")
    c_list = []

    if desc == "":
        prompt = "You are tasked to make up " + str(num) + " character(s) in a " + settings.game_style + \
                 "-style game. It is crucial that you do not make more than " + str(num) + " character(s)." \
                 "Output your responses as a list of python lists, the length of the list being the number of " \
                 "character(s) needing to be created, and each of the nested lists separated with '\n\n', and laid out " \
                 "like: " + str(character.character_details) + \
                 ". Make sure none of the character() you create identical, and that they are all unique. An " \
                 "example of a character that you could create is: ['John', 'John is a farmer who lives in Centretown. " \
                 "He loves nature, and frequently likes going on walks through nature. He is kind and responds to other " \
                 "characters in a kind and relaxed tone. ' 'Farmer', 100, 10, 10, [], 'Centretown']. As additional " \
                 "context, NAME is the name of the character, ROLE is the job that the character is tasked to do, " \
                 "PERSONALITY is a short  'role' is the job or role the entity serves, HEALTH, ATTACK, " \
                 "and DEFENCE are attributes that you can pick based on the character's ROLE. INVENTORY is a list of " \
                 "items the character may have based on their ROLE, PERSONALITY is a description of the character, " \
                 "and can be anything, as long as it details at least 100 words about the character's personality. For " \
                 "the LOCATION, choose a location that would fit the ROLE that the entity has (ex. A farmer would be " \
                 "located in a more rural area).You can pick from the following cities/zones: " + \
                 str(settings.default_location) + ". Additionally, DO NOT USE THE ''' CHARACTER IN YOUR RESPONSES. " \

        x = ast.literal_eval(generate([{"role": "system", "content": prompt}])["choices"][0]['message']['content'])

    else:
        x = ast.literal_eval(generate([{"role": "system", "content": desc}])["choices"][0]['message']['content'])

    print(x)

    if num > 1:
        for i in range(len(x)):
            c_list.append(character.Character(x[i][0], x[i][1], x[i][2], x[i][3], x[i][4], x[i][5], x[i][6], x[i][7]))

    else:
        i = 0
        return character.Character(x[i][0], x[i][1], x[i][2], x[i][3], x[i][4], x[i][5], x[i][6], x[i][7])


# Function that generates a random 8-digit 'id' string and returns it.
def generate_id(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters_and_digits) for i in range(length))
    return result_str

