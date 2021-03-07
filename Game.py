import pygame
from header import *
from Board import Board


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN)
        pygame.display.set_caption('Tetris')

        self.board = Board()

        self.is_running = True

    def handleEvent(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                pass

    def update(self) -> None:
        pass

    def render(self) -> None:
        self.screen.fill(WHITE)
        self.board.draw(self.screen)
        pygame.display.update()

    def run(self) -> None:
        while self.is_running:
            self.handleEvent()
            self.update()
            self.render()
        pygame.quit()
