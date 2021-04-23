import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 410
SCREEN = (SCREEN_WIDTH, SCREEN_HEIGHT)

ROW = 20
COL = 10

BLOCK_SIZE = 20

BOARD_WIDTH = COL * BLOCK_SIZE
BOARD_HEIGHT = ROW * BLOCK_SIZE
BOARD_POS = (10, 0)

SCORE_BOARD_WIDTH = 160
SCORE_BOARD_HEIGHT = 60
SCORE_BOARD_POS = (130, 20)

LINE_BOARD_WIDTH = 160
LINE_BOARD_HEIGHT = 40
LINE_BOERD_POS = (130, 100)

LEVEL_BOARD_WIDTH = 160
LEVEL_BOARD_HEIGHT = 40
LEVEL_BOARD_POS = (130, 160)

NEXT_BOARD_WIDTH = 160
NEXT_BOARD_HEIGHT = 100
NEXT_BOARD_POS = (130, 220)

FPS = 1

# Color
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Color blocks
COLORS = (
    (255, 235,  59),
    (  0, 188, 212),
    ( 76, 175,  80),
    (237,  28,  36),
    (156,  39, 176),
    ( 63,  81, 181),
    (255,  87,  34)
)

# Block
BLOCK_O = (
    ('00',
     '00'),
)
BLOCK_I = (
    ('....',
     '....',
     '0000',
     '....'),
    ('..0.',
     '..0.',
     '..0.',
     '..0.')
)
BLOCK_S = (
    ('...',
     '.00',
     '00.'),
    ('.0.',
     '.00',
     '..0')
)
BLOCK_Z = (
    ('...',
     '00.',
     '.00'),
    ('..0',
     '.00',
     '.0.')
)
BLOCK_T = (
    ('...',
     '000',
     '.0.'),
    ('.0.',
     '.00',
     '.0.'),
    ('.0.',
     '000',
     '...'),
    ('.0.',
     '00.',
     '.0.')
)
BLOCK_J = (
    ('.0.',
     '.0.',
     '00.'),
    ('...',
     '000',
     '..0'),
    ('.00',
     '.0.',
     '.0.'),
    ('0..',
     '000',
     '...')
)
BLOCK_L = (
    ('.0.',
     '.0.',
     '.00'),
    ('..0',
     '000',
     '...'),
    ('00.',
     '.0.',
     '.0.'),
    ('...',
     '000',
     '0..')
)

BLOCKS = (
    BLOCK_O,
    BLOCK_I,
    BLOCK_S,
    BLOCK_Z,
    BLOCK_T,
    BLOCK_L,
    BLOCK_J
)
