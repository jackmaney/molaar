import os
import numpy as np

BLACK = (0, 0, 0)

SCREEN_SIZE = (1024, 768)
MAX_FPS = 60

CANDY_DIR = os.path.join("Game", "Assets", "Images", "Candies")
CANDY_FILES = [os.path.join(CANDY_DIR, file)
               for file in os.listdir(CANDY_DIR) if file[-4:] == '.png']

MOLARR_SWINGING_IMGS = []

for i in list(range(30, 101, 10)):
    MOLARR_SWINGING_IMGS.append(
        os.path.join("Game", "Assets", "Images", "Hammer" + str(i) + ".png"))

MOLARR_SIZE = (91, 109)

HAMMER_COLLISION_RECTS = [
    {"size": (81, 60), "position": (85, 9)},
    {"size": (78, 68), "position": (99, 14)},
    {"size": (71, 71), "position": (113, 26)},
    {"size": (64, 74), "position": (129, 37)},
    {"size": (55, 75), "position": (138, 53)},
    {"size": (45, 76), "position": (150, 67)},
    {"size": (38, 76), "position": (156, 85)},
    {"size": (45, 72), "position": (150, 101)}
]

MOLARR_IMG = os.path.join("Game", "Assets", "Images", "Mo'Larr.png")
HAMMER_IMG = os.path.join("Game", "Assets", "Images", "Hammer.png")
HAMMER_INITIAL_ROTATION_ANGLE = -30
HAMMER_ANGLE_INCREMENT_AMOUNT = 10
HAMMER_NUM_INCREMENTS_IN_SWING = 10

MOLARR_CENTER_OFFSET = np.array([46, 53], np.int32)
MOUSE_MOVEMENT_THRESHOLD = 20
