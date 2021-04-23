import pygame
from header import *


class Board:
    def __init__(self) -> None:
        self.pos = pygame.Vector2(BOARD_POS)
        self.width = BOARD_WIDTH
        self.height = BOARD_HEIGHT
        self.row = ROW
        self.col = COL
        self.matrix = [[-1] * self.col] * self.row
        self.size = BLOCK_SIZE
        self.surface = pygame.Surface((self.width, self.height))

    def draw(self, surface: pygame.Surface, block) -> None:
        self.surface.fill(WHITE)

        for row in range(self.row):
            for col in range(self.col):
                if self.matrix[row][col] == -1:
                    if (row + col) % 2:
                        color = (232, 232, 232)
                    else:
                        color = (248, 248, 248)
                else:
                    color = COLORS[self.matrix[row][col]]

                x = self.size * col
                y = self.size * row
                rect = pygame.Rect(x, y, self.size, self.size)

                pygame.draw.rect(self.surface, color, rect)

        block.draw(self.surface)
        surface.blit(self.surface, self.pos)
        frame = pygame.Rect(self.pos.x - 1, self.pos.y - 1,
                            self.width + 2, self.height + 2)
        pygame.draw.rect(surface, BLACK, frame, 1)
