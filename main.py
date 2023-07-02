# Created with <3 by Jacob Terkuc

# works like a generated text based game. allows for a few different features, including a user character,
# the ability to generate npc characters that can interact, and the ability to generate a world where the characters
# can interact with.

import functions, character, ast, pickle, pygame, game

# Global variables
screenWidth = 300
screenHeight = 300
fps = 30


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
    pygame.init()
    new_game = game.Game()


def test_3():
    pygame.init()
    timer = pygame.time.Clock()
    window = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("Testing out PyGame!")

    # Load images
    imgGrass = pygame.image.load("content/graphics/grass.png")
    imgBunny = pygame.image.load("content/graphics/bunny.png")

    # Game loop
    done = False
    while not done:

        # Check input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Update screen
        pygame.display.update()
        timer.tick(fps)

        # Change background color
        bgColor = pygame.Color(50, 200, 255)  # Red (0-255), Green (0-255), Blue (0-255)
        window.fill(bgColor)

        # Draw sprites
        window.blit(imgGrass, (0, 0))
        window.blit(imgBunny, (100, 50))

        # Update screen
        pygame.display.update()

    return

def test_4():
    john = character.new()
    print(john)

test_4()



# print(John)
