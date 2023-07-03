# Created with <3 by Jacob Terkuc

# works like a generated text based game. allows for a few different features, including a user character,
# the ability to generate npc characters that can interact, and the ability to generate a world where the characters
# can interact with.

import functions, character, ast, pickle, item, location


# print(functions.generate([{"role": "system", "content": "You are a farmer named john."},
#                          {"role": "user", "content": "what is your name, and what do you do?"}
#                          ]))

def test_1():
    John = character.Character("John", "John is a nice farmer.", "Farmer", 100, 10, 10, [], "Farm")

    print(John)

    print(id(John))

    John.save()

    print(id(John))

    Joe = character.load("John")

    print(id(Joe))

    return 0


def test_2():
    c1 = {"role": "user", "content": "what is your name, and what do you do?"}
    c2 = {"role": "system", "content": "You are a farmer named john."}
    c3 = {"role": "user", "content": "what is your name, and what do you do?"}

    John = character.Character("John", "John is a nice farmer.", "Farmer", 100, 10, 10, [], "Farm")
    Mary = character.Character("Mary", "Mary is a nice farmer.", "Farmer", 100, 10, 10, [], "Farm")
    Sue = character.Character("Sue", "Sue is a nice farmer.", "Farmer", 100, 10, 10, [], "Farm")

    d = {John: [{"role": "user", "content": "what is your name, and what do you do?"},
                {"role": "system", "content": "You are a farmer named john."},
                {"role": "user", "content": "what is your name, and what do you do?"}],
         Mary: [{"role": "user", "content": "what is your name, and what do you do?"},
                {"role": "system", "content": "You are a farmer named john."},
                {"role": "user", "content": "what is your name, and what do you do?"}],
         Sue: [{"role": "user", "content": "what is your name, and what do you do?"},
               {"role": "system", "content": "You are a farmer named john."},
               {"role": "user", "content": "what is your name, and what do you do?"}]}




def world_gen_test():
    running = True

    while running:
        loc = location.new("city")
        print(loc)

    return 0


def character_gen_test():
    running = True

    # Create new character
    shopkeep_1 = character.new()
    print(shopkeep_1)

    # while running:

    return 0


test_2()

# print(John)
