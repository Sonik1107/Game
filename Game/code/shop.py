import pygame
from settings import *

class Shop:
    def __init__(self, player, game):
        self.player = player
        self.game = game
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 30)  # Используем шрифт по умолчанию и размер 30
        self.active = False  # Магазин неактивен при создании

        # Товары в магазине
        self.items = {
            "speed": {"cost": 10, "description": "Увеличивает скорость передвижения."}
        }

    def toggle(self):
        # Переключаем состояние магазина (открыть/закрыть)
        self.active = not self.active

    def draw(self):
        if self.active:
            # Отображение заднего фона магазина
            pygame.draw.rect(self.display_surface, UI_BG_COLOR, (50, 50, WIDTH - 100, HEIGTH - 100))
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, (50, 50, WIDTH - 100, HEIGTH - 100), 3)

            # Отображение товаров в магазине
            item_height = 100
            y_offset = 100
            for item_name, item_data in self.items.items():
                # Отображение названия товара
                name_surf = self.font.render(item_name.capitalize(), False, TEXT_COLOR)
                name_rect = name_surf.get_rect(topleft=(50, y_offset))
                self.display_surface.blit(name_surf, name_rect)

                # Отображение цены товара
                cost_surf = self.font.render(f"Цена: {item_data['cost']}", False, TEXT_COLOR)
                cost_rect = cost_surf.get_rect(topleft=(150, y_offset))
                self.display_surface.blit(cost_surf, cost_rect)

                # Отображение описания товара
                desc_surf = self.font.render(item_data['description'], False, TEXT_COLOR)
                desc_rect = desc_surf.get_rect(topleft=(250, y_offset))
                self.display_surface.blit(desc_surf, desc_rect)

                # Кнопка покупки (просто текст, без функциональности)
                buy_surf = self.font.render("Купить", False, TEXT_COLOR)
                buy_rect = buy_surf.get_rect(topleft=(800, y_offset))
                self.display_surface.blit(buy_surf, buy_rect)

                y_offset += item_height  # Увеличиваем смещение для следующего товара

    def handle_input(self, event):
        #Обработка событий магазина (пока только закрытие по кнопке M)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                self.toggle()

    def run(self):
        self.draw() # отрисовываем магазин если он активен