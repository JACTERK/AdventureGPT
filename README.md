# AdventureGPT

## Introduction
A GPT-4 powered adventure game engine. 

## Features
- Ability to generate characters on the fly, as well as allowing the user to add static characters into the game.
- Different world zones, with the ability to add more.
- Ability to add items to the game, and have them interact with the world.

## How to use:
- Clone the repo using `git clone https://github.com/JACTERK/AdventureGPT`
- Install the requirements using `pip install -r requirements.txt`
- Change any settings you want in `settings.py`
- Run the game using `python main.py` or by using one of the startup scripts.

## Features to add:
There are a few features I want to still add to the project. Some of those are:

- [ ] Add a way to save the game, as well as load it from a file.
- [ ] Add a better way to interact with the game, such as a GUI.
- [ ] Add a way to add more items to the game, and manage your inventory better.
- [ ] Add a way to have NPC operate independently of the player, and do actions that fit the NPC's personality.

# Technical Details

## Character Creation Workflow

### Step 1: Creating a list of characters
By default, the `create_entities()` function is called when the game is first loaded. This function creates a list of characters that the player can interact with. This list is stored in the `entities` variable, and is a list of `Entity` objects.

In the `create_entities()` function, the `entities` list is populated with `num` number of `Entity` creation calls. The list of calls is stored in 


The `Entity` class is defined in `entity.py`, and is a class that represents a character in the game. The `Entity` class has the following attributes:
- `name`: The name of the character.
- `role`: The role of the character. This is used in part to determine the character's personality.
- `personality`: The personality of the character. This is used to determine how the character will act in the game.
- `health`: The health of the character. _(Not implemented yet)_
- `attack`: The attack of the character. _(Not implemented yet)_
- `defense`: The defense of the character. _(Not implemented yet)_
- `inventory`: The inventory of the character.
- `location`: The location of the character. This is used to determine where the character is in the game world.

There are two ways to create an `Entity` object. The first way is to use the `Entity` constructor.
