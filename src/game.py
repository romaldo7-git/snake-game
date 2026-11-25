import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SPEED

class Game:
    def __init__(self):
        # Инициализация Pygame
        pygame.init()
        # Создание окна игры
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Змейка")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        # Главный цикл игры
        while self.running:
            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False # Выход из игры при нажатии на крестик

            # Заливка экрана черным цветом (чтобы окно не было белым)
            self.screen.fill((0, 0, 0))
            
            # Обновление экрана
            pygame.display.flip()
            
            # Ограничение частоты кадров
            self.clock.tick(SNAKE_SPEED)

        # Корректное завершение работы Pygame
        pygame.quit()