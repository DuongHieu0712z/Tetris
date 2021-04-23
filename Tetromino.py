import pygame
from Block import *


class Tetromino(Block):
    def __init__(self) -> None:
        self.randomizeBlock()
        self.row_val = 1
        self.col_val = 0
        self.is_rotate = False

    def canRotate(self, board) -> bool:
        if self.row < 0 or self.row + len(self.block) > board.row:
            return False
        if self.col < 0 or self.col + len(self.block[0]) > board.col:
            return False
        return True

    def randomizeBlock(self) -> None:
        super().randomizeBlock()
        self.row = -self.bottom
        self.col = (COL - (self.right - self.left + 1)) // 2 - self.left

    def handleInputKeyDown(self, key) -> None:
        if key == pygame.K_LEFT or key == pygame.K_a:
            self.col_val = -1
        elif key == pygame.K_RIGHT or key == pygame.K_d:
            self.col_val = 1
        elif key == pygame.K_UP or key == pygame.K_w:
            self.is_rotate = True
        elif key == pygame.K_DOWN or key == pygame.K_s:
            self.row_val = 1

    def handleInputKeyUp(self, key) -> None:
        if key == pygame.K_LEFT or key == pygame.K_a:
            self.col_val = 0
        elif key == pygame.K_RIGHT or key == pygame.K_d:
            self.col_val = 0
        elif key == pygame.K_UP or key == pygame.K_w:
            self.is_rotate = False
        elif key == pygame.K_DOWN or key == pygame.K_s:
            self.row_val = 0

    def isCollision(self, board) -> bool:
        if self.col + self.left + self.col_val < 0:
            return False
        elif self.col + self.right + self.col_val == board.col:
            return False
        
        if self.row + self.top + self.row_val < 0:
            return False
        elif self.row + self.bottom + self.row_val == board.row:
            return False

        return True

    def update(self, board) -> None:
        if self.is_rotate:
            if self.canRotate(board):
                self.rotate()
            # self.col = 0
        else:
            if self.isCollision(board):
                self.row += self.row_val
                self.col += self.col_val

    def draw(self, surface) -> None:
        for row in range(len(self.block)):
            for col in range(len(self.block[0])):
                if self.block[row][col] == '0':
                    x = (self.col + col) * BLOCK_SIZE
                    y = (self.row + row) * BLOCK_SIZE
                    pygame.draw.rect(surface, self.color, (x, y, BLOCK_SIZE, BLOCK_SIZE))
