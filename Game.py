import pygame
from header import *
from Board import Board
from Tetromino import Tetromino
from Time import Time


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN)
        pygame.display.set_caption('Tetris')

        self.board = Board()
        self.block = Tetromino()

        self.is_running = True

        self.time = Time()
        self.before_time = 0
        self.current_time = 0
        self.lag = 0

    def handleEvent(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                self.block.handleInputKeyDown(event.key)
            elif event.type == pygame.KEYUP:
                self.block.handleInputKeyUp(event.key)

    def update(self) -> None:
        self.block.update(self.board)
        # self.block.randomizeBlock()

    def render(self) -> None:
        self.screen.fill((240, 240, 240))
        self.board.draw(self.screen, self.block)
        pygame.display.update()

    def getTime(self) -> None:
        self.time.start()
        self.current_time = self.time.getTicks()
        time_past = self.current_time - self.before_time
        self.before_time = self.current_time
        self.lag += time_past

    def run(self) -> None:
        ms_per_frame = 1000 / FPS
        while self.is_running:
            self.getTime()
            self.handleEvent()
            while self.lag >= ms_per_frame:
                self.update()
                self.lag -= ms_per_frame
            self.render()
        pygame.quit()
