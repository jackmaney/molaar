import os
import numpy as np

BLACK = (0, 0, 0)

SCREEN_SIZE = (1024, 768)
MAX_FPS = 60

MOLARR_SWINGING_IMGS = []

for i in list(range(30, 101, 10)):
    MOLARR_SWINGING_IMGS.append(os.path.join("Game", "Assets", "Images", "Hammer" + str(i) + ".png"))

MOLARR_IMG = os.path.join("Game", "Assets", "Images", "Mo'Larr.png")
HAMMER_IMG = os.path.join("Game", "Assets", "Images", "Hammer.png")
HAMMER_INITIAL_ROTATION_ANGLE = -30
HAMMER_ANGLE_INCREMENT_AMOUNT = 10
HAMMER_NUM_INCREMENTS_IN_SWING = 10

MOLARR_CENTER_OFFSET = np.array([46, 53], np.int32)
MOUSE_MOVEMENT_THRESHOLD = 20
