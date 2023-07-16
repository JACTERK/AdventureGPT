# AdventureGPT

## Introduction
A GPT powered adventure game engine. 

## Features
- Ability to generate characters on the fly, as well as allowing the user to add static characters into the game.
- Different world zones, with the ability to add more.
- Ability to add items to the game, and have them interact with the world.
- Generate profile photos for use in Discord implementations.

## How to use:
- Clone the repo using `git clone https://github.com/JACTERK/AdventureGPT`
- Install the requirements using `pip install -r requirements.txt`
- Change any settings you want in `settings.py`
- Create a file in the main directory called `.env`, and add the following lines:
```
DISCORD_TOKEN=<your discord token>
OPENAI_API_KEY=<your openai api key>
```
- Run the game using `python main.py` or by using one of the startup scripts.

## Features to add:
There are a few feature still to add to the project. Some of those are:

- [ ] Add a way to save the game, as well as load it from a file.
- [ ] Add a better way to interact with the game, such as a GUI.
- [ ] Add a way to add more items to the game, and manage your inventory better.
- [ ] Add a way to have NPC operate independently of the player, and do actions that fit the NPC's personality.

# Technical Details

## Game Startup Workflow

### Step 1: Creating a list of characters (`Character` Class)
The first step in the game startup procedure is to generate a list of characters that will be in the game. The list
is used to track the status of characters throughout the game.

By default, the `create_entities()` function is called when the game is first loaded. 
This function creates a list of characters that the player can interact with. 
This list is stored in the `entities` variable, and is a list of `Entity` objects.

In the `create_character(num, desc='')` function, it will first check if a `desc` was passed. If it was not provided, 
the function will generate `num` number of characters using generated details. If a `desc` was provided, the function
will generate `num` number of characters using the provided description. `num` is an integer, and `desc` is a list of details. (See appendix for details on the `desc` list)


The `Character` class is defined in `character.py`, and is a class that represents a character in the game. 
The `Character` class has the following attributes:

- `name`: The name of the character.
- `role`: The role of the character. This is used in part to determine the character's personality.
- `personality`: The personality of the character. This is used to determine how the character will act in the game.
- `health`: The health of the character. _(Not implemented yet)_
- `attack`: The attack of the character. _(Not implemented yet)_
- `defense`: The defense of the character. _(Not implemented yet)_
- `inventory`: The inventory of the character.
- `location`: The location of the character. This is used to determine where the character is in the game world.

There are two ways to create an `Character` object. The first way is to use the `Character` constructor with the 
above attributes. The second way is to use the `Character` constructor with no attributes, which creates a character 
based on the defaults set in `settings.py`, the rest of the attributes being automatically generated.  

### Step 2: Generating the game world (`World` Class)
The second step in the game startup procedure is to generate the game world. The `World` class is defined in `world.py`,
and has the following attributes:

- `characters`: A list of `Character` objects that are in the game. This is to be the same format as the output for 
the `create_character()` function.
- `locations`: A list of `Location` objects that are in the game. 
- `items`: A list of `Item` objects that are in the game.

The world class, being the first class that is created, is responsible for generating and storing information about the 
characters, locations, and items in the game. To make this possible, the `World` class has the following methods:

- `generate_character(name)`: Generates a character with the name `name`, and stores it in the `characters` attribute.
- `generate_location(name)`: Generates a location with the name `name`, and stores it in the `locations` attribute.
- `generate_item(name)`: Generates an item with the name `name`, and stores it in the `items` attribute.

The three functions call functions that are inside the `Character`, `Location`, and `Item` classes, respectively, and 
return nothing.

### Step 3: Generating locations (`Location` Class)
The third step in the game startup procedure is to generate the locations. The `Location` class is defined in `location.py`,
and has the following attributes:
- `name`: The name of the location.
- `desc`: A description of the location.
- `id`: The id of the location.


### Step 4: Generating the game items (`Item` Class)

The fourth step in the game startup procedure is to generate the game items. The `Item` class is defined in `item.py`,
and has the following attributes:

- `name`: The name of the item.
- `desc`: A description of the item.
- `id`: The id of the item.


# Appendix

## Functions

## `functions.py`

### `generate(msg)`
- `msg` (String): The message to generate a response to.
- Returns `response` (String): The response generated by the model.

### `create_character(num, desc=[])`
- `num` (Integer): The number of characters to create.
- `desc` (List): A list of details to use to create the character.
  - The structure of the list is: `[name, personality, role, health, attack, defense, inventory, location]`
      - Example: ```['John', 'John is a farmer who lives in Centretown. He loves nature, and frequently likes going on walks through nature. He is kind and responds to other characters in a kind and relaxed tone. ' 'Farmer', 100, 10, 10, [], 'Centretown']```
- Returns `c_list` (List): A list of `Character` objects.

## `character.py`

### `new(desc="")`
