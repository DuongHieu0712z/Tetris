import pygame
from header import *


class Board:
    def __init__(self) -> None:
        self.pos = pygame.Vector2(BOARD_POS)
        self.width = BOARD_WIDTH
        self.height = BOARD_HEIGHT
        self.row = 20
        self.col = 10
        self.size = BLOCK_SIZE
        self.surface = pygame.Surface((self.width, self.height))

    def draw(self, surface: pygame.Surface) -> None:
        self.surface.fill(WHITE)

        y = 0
        for row in range(self.row):
            x = 0
            for col in range(self.col):
                if (row + col) % 2:
                    color = (232, 232, 232)
                else:
                    color = (248, 248, 248)
                rect = pygame.Rect(x, y, self.size, self.size)
                pygame.draw.rect(self.surface, color, rect)
                x += self.size
            y += self.size

        surface.blit(self.surface, self.pos)
        frame = pygame.Rect(self.pos.x - 1, self.pos.y - 1,
                            self.width + 2, self.height + 2)
        pygame.draw.rect(surface, BLACK, frame, 1)
