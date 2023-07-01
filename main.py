# Created with <3 by Jacob Terkuc

# works like a generated text based game. allows for a few different features, including a user character,
# the ability to generate npc characters that can interact, and the ability to generate a world where the characters
# can interact with.

import functions, character, ast, pickle, item, location, world


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

    return


def test_2():
    c = character.new()
    print(c)
    return


def test_3():
    loc = location.new("city")
    print(loc)
    return


def test_4():
    w = world.new()

    Sword = item.new("sword")

    print(Sword.get_identifier())

    w.add_item(Sword)

    print(w)
    return


test_4()

# print(John)
