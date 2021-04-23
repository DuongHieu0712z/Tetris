from header import *
import pygame
import random

class Block:
    def __init__(self) -> None:
        self.randomizeBlock()

    def __top(self) -> None:
        for row in range(len(self.block)):
            if '0' in self.block[row]:
                self.top = row
                break

    def __bottom(self) -> None:
        for row in range(len(self.block) - 1, -1, -1):
            if '0' in self.block[row]:
                self.bottom = row
                break

    def __left(self) -> None:
        for col in range(len(self.block[0])):
            if any(map(lambda row: row[col] == '0', self.block)):
                self.left = col
                break

    def __right(self) -> None:
        for col in range(len(self.block[0]) - 1, -1, -1):
            if any(map(lambda row: row[col] == '0', self.block)):
                self.right = col
                break

    def __direction(self) -> None:
        self.__top()
        self.__bottom()
        self.__left()
        self.__right()

    def randomizeBlock(self) -> None:
        self.type = random.randrange(len(BLOCKS))
        self.frame = random.randrange(len(BLOCKS[self.type]))
        self.block = BLOCKS[self.type][self.frame]
        self.color = COLORS[self.type]
        self.__direction()

    def nextFrame(self) -> None:
        self.frame += 1
        if self.frame == len(BLOCKS[self.type]):
            self.frame = 0

    def rotate(self) -> None:
        self.nextFrame()
        self.block = BLOCKS[self.type][self.frame]
        self.__direction()
