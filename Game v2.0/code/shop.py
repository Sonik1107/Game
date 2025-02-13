import pygame
from settings import *


class Shop:
    def __init__(self, player, game):
        self.player = player
        self.game = game
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 30)
        self.active = False
        self.selected_item = None
        self.items = {
            "speed": {"cost": 10, "description": "Увеличивает скорость передвижения.", "attribute": "speed",
                      "amount": 2}
        }

    def toggle(self):
        self.active = not self.active

    def draw(self):
        if self.active:
            pygame.draw.rect(self.display_surface, UI_BG_COLOR, (50, 50, WIDTH - 100, HEIGTH - 100))
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, (50, 50, WIDTH - 100, HEIGTH - 100), 3)

            item_height = 70
            y_offset = 100
            for item_name, item_data in self.items.items():
                name_surf = self.font.render(item_name.capitalize(), False, TEXT_COLOR)
                name_rect = name_surf.get_rect(topleft=(70, y_offset))
                self.display_surface.blit(name_surf, name_rect)

                cost_surf = self.font.render(f"Цена: {item_data['cost']}", False, TEXT_COLOR)
                cost_rect = cost_surf.get_rect(topleft=(200, y_offset))
                self.display_surface.blit(cost_surf, cost_rect)

                desc_surf = self.font.render(item_data['description'], False, TEXT_COLOR)
                desc_rect = desc_surf.get_rect(topleft=(350, y_offset))
                self.display_surface.blit(desc_surf, desc_rect)

                buy_surf = self.font.render("Купить", False, TEXT_COLOR)
                buy_rect = buy_surf.get_rect(topleft=(WIDTH - 200, y_offset))

                if self.selected_item == item_name:
                    buy_surf = self.font.render("Купить", False, "red")

                self.display_surface.blit(buy_surf, buy_rect)

                item_data['buy_rect'] = buy_rect
                y_offset += item_height

    def buy_item(self):

        with open('scr.txt', 'r') as fl:
            s = fl.readlines()

        self.money = int(''.join(s))
        if self.selected_item and self.selected_item in self.items:
            item_data = self.items[self.selected_item]
            if self.money >= item_data["cost"]:
                self.money -= item_data["cost"]
                if item_data["attribute"] == "speed":
                    self.player.speed += item_data["amount"]
                print(
                    f"Куплен предмет: {self.selected_item}.  Новая скорость: {self.player.speed}, Осталось денег: {self.money}")
                self.selected_item = None
                with open('scr.txt', 'w') as fl:
                    fl.write(str(self.money))
            else:
                print("Недостаточно денег!")

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                self.toggle()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for item_name, item_data in self.items.items():
                    if 'buy_rect' in item_data and item_data['buy_rect'].collidepoint(mouse_pos):

                        if self.selected_item == item_name:
                            self.buy_item()
                        else:
                            self.selected_item = item_name
                        break

    def run(self):
        if self.active:
            self.draw()
