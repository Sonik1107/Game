import pygame, sys
from settings import *
from level import Level
from shop import Shop


class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('The Farm')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.shop = Shop(self.level.player, self)

    def run1(self):
        intro_text = ["Название игры: Ферма",
                      "Управление героем: клавиши:",
                      "WASD",
                      "Нажмите любую кнопку для начала игры",
                      ]

        image = pygame.image.load('../textures/ferma.png')
        fon = pygame.transform.scale(image, (WIDTH, HEIGTH))
        self.screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 350
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 500
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    self.run2()

            pygame.display.flip()
            self.clock.tick(FPS)

    def run2(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.shop.handle_input(event)
            self.screen.fill('black')
            self.level.run()
            self.shop.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run1()
