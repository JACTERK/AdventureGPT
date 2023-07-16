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
    msglist = []

    # Checks if the type of 'msg' is a list or a string
    if type(msg) == list:
        print("Type is list")
        msglist = msg

    else:
        print("Type is string")
        print("Generating response...")
        msglist = [{"role": "system", "content": str(msg)}]

    # Create a new completion using the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=msglist,
    )
    return response["choices"][0]['message']['content']

