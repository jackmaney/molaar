import os
import numpy as np
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_SIZE = (1024, 768)
MAX_FPS = 60

BACKGROUND = pygame.Surface(SCREEN_SIZE)
BACKGROUND_IMG = pygame.image.load(
    os.path.join("Game", "Assets", "Images", "ground.png"))
BACKGROUND_IMG_SIZE = (512, 256)

for i in [0, 1]:
    for j in [0, 1, 2]:
        BACKGROUND.blit(BACKGROUND_IMG,
                        (i * BACKGROUND_IMG_SIZE[0], j * BACKGROUND_IMG_SIZE[1]))

CANDY_DIR = os.path.join("Game", "Assets", "Images", "Candies")
CANDY_FILES = [os.path.join(CANDY_DIR, file)
               for file in os.listdir(CANDY_DIR) if file[-4:] == '.png']

MOLARR_SWINGING_IMGS = []

for i in list(range(30, 101, 10)):
    MOLARR_SWINGING_IMGS.append(
        os.path.join("Game", "Assets", "Images", "Hammer" + str(i) + ".png"))

MOLARR_SIZE = (91, 109)

TOOTHBRUSH_IMG = os.path.join("Game", "Assets", "Images", "Toothbrush.png")

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
ANDANTE_IMG = os.path.join("Game", "Assets", "Images", "Andante.png")
HAMMER_IMG = os.path.join("Game", "Assets", "Images", "Hammer.png")
HAMMER_INITIAL_ROTATION_ANGLE = -30
HAMMER_ANGLE_INCREMENT_AMOUNT = 10
HAMMER_NUM_INCREMENTS_IN_SWING = 10

MOLARR_CENTER_OFFSET = np.array([46, 53], np.int32)
MOUSE_MOVEMENT_THRESHOLD = 20

TURN_THRESHOLD = 5

SOUND_IMPACT_FILE = os.path.join("Game", "Assets", "Sounds", "pumpkin_break_01_0.wav")
SOUND_DUCT_TAPE_FILE = os.path.join("Game", "Assets", "Sounds", "89782__zerolagtime__tape03-duct-tape-3_MODIFIED.wav")
SOUND_TOOTHBRUSH = os.path.join("Game", "Assets", "Sounds", "shimmer_1.wav")
OPENING_MUSIC_FILE = os.path.join("Game", "Assets", "Music", "Elegy_Dm.wav")
GAME_MUSIC_FILE = os.path.join("Game", "Assets", "Music", "battleThemeA.wav")

MAX_CANDY_THRESHOLDS = {
    30000: 5,
    60000: 7,
    90000: 8,
    120000: 10,
    150000: 12,
    180000: 15
}

CANDY_DAMAGE_THRESHOLDS = {
    20000: {"min": 1, "max": 2},
    30000: {"min": 2, "max": 4},
    45000: {"min": 3, "max": 5},
    60000: {"min": 5, "max": 8},
    90000: {"min": 7, "max": 10},
    120000: {"min": 10, "max": 15},
    180000: {"min": 15, "max": 20}
}

CANDY_SPEED_THRESHOLDS = {
    10000: {"min": 1, "max": 5},
    20000: {"min": 3, "max": 7},
    30000: {"min": 5, "max": 10},
    60000: {"min": 6, "max": 12},
    90000: {"min": 8, "max": 15},
    120000: {"min": 12, "max": 20},
    180000: {"min": 20, "max": 25}
}

CANDY_SEEKER_PROBABILITY_THRESHOLDS = {
    10000: 0,
    20000: 0.1,
    30000: 0.25,
    45000: 0.33,
    60000: 0.5
}

TOOTHBRUSH_THRESHOLDS = {
    60000: 2,
    120000: 1
}

TIME_BETWEEN_ENEMY_LOADS = 500
TIME_BETWEEN_TOOTHBRUSH_SPAWNS = 5000

HEALTH_REGAINED_FROM_TOOTHBRUSH = 20