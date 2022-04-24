import pygame
import os
import time
import random

# Inits
pygame.font.init() # In pygame, it's necessary to initialize a few things before we can run the code.

# Scrolling Class
class Space(pygame.sprite.Sprite):
    def __init__(self, num):
        pygame.sprite.Sprite.__init__(self)
        self.rect.top = num * 600
        self.image, self.rect = load_image("space.png", 10)
        self.dx = -5
        self.reset()

    def update(self):
        self.rect.top += self.dx
        if self.rect.top <= -1200:
            self.reset() 

    def reset(self):
        self.rect.top = 600
 


# Screen Config
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Friendly Space Shooter by @schumann_victor")

"""
While trying to implement the resolution, I was getting the following error:

```libGL error: MESA-LOADER: failed to open iris: /home/yui/anaconda3/bin/../lib/libstdc++.so.6: version `GLIBCXX_3.4.29' not found (required by /usr/lib64/dri/iris_dri.so) (search paths /usr/lib64/dri, suffix _dri)```

If you get this too, deleting the `libstdc++.so.6` file allows the code to run as intended. I'm not sure what this file was supposed to do, but I backed it up just in case, and I recommend you do the same.
"""


# Image Loading
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background_space_black.png")), (WIDTH, HEIGHT))

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
    level = 1
    lives = 10
    main_font = pygame.font.SysFont("couriernew", 20)
    title_font = pygame.font.SysFont("couriernew", 50)

    def redraw_window(): # Manages game rendering
        WIN.blit(BG, (0,0)) # Draws the background
        # x_text initializes our text variables
        lives_text = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_text = title_font.render(f"WORK IN PROGRESS - COME BACK LATER!!", 1, (255, 230, 0))
        # Friendly reminder to add ": {level}", 1," instead of "!!"

        WIN.blit(lives_text, (10, 10))
        WIN.blit(level_text, level_text.get_rect(center = WIN.get_rect().center))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type ==pygame.QUIT: # This makes sure our game quits when intended. Nobody wants to bargain with Dormamu.
                run = False

main ()