import os
import numpy as np

BLACK = (0, 0, 0)

SCREEN_SIZE = (1024, 768)
MAX_FPS = 60

MOLARR_IMG = os.path.join("Game", "Assets", "Images", "Mo'Larr.png")
MOLARR_CENTER_OFFSET = np.array([46, 53], np.int32)
MOUSE_MOVEMENT_THRESHOLD = 20
