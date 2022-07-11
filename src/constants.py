# constant things not game state lol
import pygame
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

GAME_TITLE = "Color Me You"
GAME_ICON = pygame.image.load('assets\images\icon.png')

INTERACT_SOUND = pygame.mixer.Sound("assets/sounds/interact_sound.mp3")
INTERACT_SOUND.set_volume(0.4)

CYAN = (1, 176, 239)
YELLOW = (255, 247, 1)
MAGENTA = (237, 0, 140)
BLUE = (11, 41, 181)
RED = (169, 0, 46)
GREEN = (0, 173, 32)
BLACK = (32, 32, 32)

CYAN_MODE = [CYAN, BLUE, GREEN, BLACK]
MAGENTA_MODE = [MAGENTA, BLUE, RED, BLACK]
YELLOW_MODE = [YELLOW, GREEN, RED, BLACK]

ACCELERATION = 0.6
FRICTION = -0.15

PLAYER_WIDTH = 96
PLAYER_HEIGHT = 120

WEAK_OPACITY = 100
STRONG_OPACITY = 255