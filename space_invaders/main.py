from time import time
import pygame
import os
import time
import random

# Image Loading

# Space Ships
ENEMY_SHIP_V = pygame.image.load(os.path.join("assets", "pixel_ship_vertical.png"))
ENEMY_SHIP_H = pygame.image.load(os.path.join("assets", "pixel_ship_horizontal.png"))
ENEMY_SHIP_BOSS_1 = pygame.image.load(os.path.join("assets", "pixel_ship_boss_1.png"))
ENEMY_SHIP_BOSS_2 = pygame.image.load(os.path.join("assets", "pixel_ship_boss_2.png"))
HERO_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_hero.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
bg = pygame.image.load(os.path.join("assets", "background_black.png"))