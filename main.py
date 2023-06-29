# Created with <3 by Jacob Terkuc

# works like a generated text based game. allows for a few different features, including a user character,
# the ability to generate npc characters that can interact, and the ability to generate a world where the characters
# can interact with.

import functions, character

#print(functions.generate([{"role": "system", "content": "You are a farmer named john."},
#                          {"role": "user", "content": "what is your name, and what do you do?"}
#                          ]))

#John = entity.Entity("John", "Farmer", 100, 10, 10, [], "Farm")

msg = "The response to the following query needs to be in the format of a function call. The function call is laid " \
      "out in the following way: Entity('name', 'race', 'role', health, attack, defense, inventory, location). As " \
      "additional context, 'race' can be things like 'human', 'dog', 'horse' etc. depending on the contents of the " \
      "message. 'role' is the job or role the entity serves, 'health', 'attack', and 'defence' are all to be defined " \
      "in the following message. 'inventory' is an empty list, and 'location' is the zone the entity is in. I am " \
      "making a character in a fantasy based RPG game. "

c = "The character's name is John, and he is a human farmer. He has 100 health, 10 attack, and 10 defense. He has no " \
    "items in his inventory, and is currently in centretown." \


print(functions.create_entities(3))

#John = entity.Entity(entity.create_character(c))

#print(John)
