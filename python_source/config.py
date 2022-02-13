__all__ = (
    'FPS',

    'WIN_WIDTH',
    'WIN_HEIGHT',

    'CELLS_ALONG_X',
    'CELLS_ALONG_Y',
    'CELLS_WIDTH',
    'CELLS_HEIGHT',
    'CELLS_X_OFFSET',
    'CELLS_Y_OFFSET',

    'BACKGROUND_COLOR',
    'DEAD_CELL_COLOR',
    'LIVE_CELL_COLOR',
    'CHECKED_CELL_COLOR',
)

FPS = 200

WIN_WIDTH = 1000
WIN_HEIGHT = 650

CELLS_ALONG_X = 100*2
CELLS_ALONG_Y = 65*2
CELLS_SPACE_WIDTH = 0
CELLS_WIDTH = WIN_WIDTH / CELLS_ALONG_X - CELLS_SPACE_WIDTH
CELLS_HEIGHT = WIN_HEIGHT / CELLS_ALONG_Y - CELLS_SPACE_WIDTH
CELLS_X_OFFSET = CELLS_WIDTH + CELLS_SPACE_WIDTH
CELLS_Y_OFFSET = CELLS_HEIGHT + CELLS_SPACE_WIDTH

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_DARK_GREEN = (0, 50, 0)
DARK_GREEN = (0, 170, 0)
ORANGE = (255, 150, 100)
DARK_DARK_GREY = (20, 20, 20)
GREY = (150, 150, 150)
LIGHT_GREY = (200, 200, 200)

BACKGROUND_COLOR = DARK_DARK_GREY
DEAD_CELL_COLOR = BLACK
LIVE_CELL_COLOR = GREEN
CHECKED_CELL_COLOR = DARK_DARK_GREEN
