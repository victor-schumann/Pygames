from time import time
import pygame
import os
import time
import random

# Screen Config
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Friendly Space Game")

"""
While trying to implement this, I was getting the following error:
```
libGL error: MESA-LOADER: failed to open iris: /home/yui/anaconda3/bin/../lib/libstdc++.so.6: version `GLIBCXX_3.4.29' not found (required by /usr/lib64/dri/iris_dri.so) (search paths /usr/lib64/dri, suffix _dri)
```
If you find this too, deleting the `libstdc++.so.6` file allows the code to run as intended. I'm not sure what this file was supposed to do, but I backed it up just in case. Thus, you should do the same.
"""


# Image Loading
bg = pygame.image.load(os.path.join("assets", "background_black.png"))

# Space Ships
ENEMY_SHIP_V = pygame.image.load(os.path.join("assets", "pixel_ship_vertical.png"))
ENEMY_SHIP_H = pygame.image.load(os.path.join("assets", "pixel_ship_horizontal.png"))
ENEMY_SHIP_BOSS_1 = pygame.image.load(os.path.join("assets", "pixel_ship_boss_1.png"))
ENEMY_SHIP_BOSS_2 = pygame.image.load(os.path.join("assets", "pixel_ship_boss_2.png"))
HERO_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_hero.png"))

# Lasers
RED_LASER_LINE = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
RED_LASER_BALL = pygame.image.load(os.path.join("assets", "pixel_laser_ball_red.png"))
GREEN_LASER_LINE = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
GREEN_LASER_BALL = pygame.image.load(os.path.join("assets", "pixel_laser_ball_green.png"))
BLUE_LASER_LINE = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
BLUE_LASER_BALL = pygame.image.load(os.path.join("assets", "pixel_laser_ball_blue.png"))
YELLOW_LASER_LINE = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))
YELLOW_LASER_BALL = pygame.image.load(os.path.join("assets", "pixel_laser_ball_yellow.png"))
BOSS_LASER_LINE = pygame.image.load(os.path.join("assets", "pixel_laser_vertical_1.png"))
BOSS_LASER_BALL = pygame.image.load(os.path.join("assets", "pixel_laser_vertical_2.png"))

# Main Game Loop
def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock() # Associated with `clock.tick(FPS)`, this makes sure our game stays consistent independently of the device you're running the game.

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type ==pygame.QUIT: # This makes sure our game quits when intended. Nobody wants to get stuck in an infinite loop.
                run = False

main ()