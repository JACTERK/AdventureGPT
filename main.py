# Created with <3 by Jacob Terkuc

# works like a generated text based game. allows for a few different features, including a user character,
# the ability to generate npc characters that can interact, and the ability to generate a world where the characters
# can interact with.

import functions, character, ast

# print(functions.generate([{"role": "system", "content": "You are a farmer named john."},
#                          {"role": "user", "content": "what is your name, and what do you do?"}
#                          ]))

# John = entity.Entity("John", "Farmer", 100, 10, 10, [], "Farm")


c = functions.create_character(2)
print(c[0])
print(c[1])

# John = entity.Entity(entity.create_character(c))

# print(John)
