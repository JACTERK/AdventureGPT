import pygame
import pytmx
import pyscroll


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True

        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("purple")

            # displays text on the screen
            pygame.display.set_caption("Game")

            pygame.display.flip()

            self.clock.tick(60)

    pygame.quit()
