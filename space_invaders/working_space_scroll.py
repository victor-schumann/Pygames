import pygame
import sys
import os


# Initializers
pygame.init()

# Classes
class Background():
    def __init__(self):
        self.colour = pygame.Color("black")

    def setTiles(self, tiles):
        if type(tiles) is str:
            self.tiles = [[loadImage(tiles)]]
        elif type(tiles[0]) is str:
            self.tiles = [[loadImage(i) for i in tiles]]
        else:
            self.tiles = [[loadImage(i) for i in row] for row in tiles]
        self.stagePosX = 0
        self.stagePosY = 0
        self.tileWidth = self.tiles[0][0].get_width()
        self.tileHeight = self.tiles[0][0].get_height()
        screen.blit(self.tiles[0][0], [0, 0])
        self.surface = screen.copy()

    def scroll(self, x, y):
        self.stagePosX -= x
        self.stagePosY -= y
        col = (self.stagePosX % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth
        xOff = (0 - self.stagePosX % self.tileWidth)
        row = (self.stagePosY % (self.tileHeight * len(self.tiles))) // self.tileHeight
        yOff = (0 - self.stagePosY % self.tileHeight)

        col2 = ((self.stagePosX + self.tileWidth) % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth
        row2 = ((self.stagePosY + self.tileHeight) % (self.tileHeight * len(self.tiles))) // self.tileHeight
        screen.blit(self.tiles[row][col], [xOff, yOff])
        screen.blit(self.tiles[row][col2], [xOff + self.tileWidth, yOff])
        screen.blit(self.tiles[row2][col], [xOff, yOff + self.tileHeight])
        screen.blit(self.tiles[row2][col2], [xOff + self.tileWidth, yOff + self.tileHeight])

        self.surface = screen.copy()

    def setColour(self, colour):
        self.colour = parseColour(colour)
        screen.fill(self.colour)
        pygame.display.update()
        self.surface = screen.copy()

class newSprite(pygame.sprite.Sprite):
    def __init__(self, filename, frames=1, altDims = None):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = loadImage(filename)
        if altDims:
            img = pygame.transform.scale(img, (altDims[0]*frames, altDims[1]))
        self.originalWidth = img.get_width() // frames
        self.originalHeight = img.get_height()
        frameSurf = pygame.Surface((self.originalWidth, self.originalHeight), pygame.SRCALPHA, 32)
        x = 0
        for frameNo in range(frames):
            frameSurf = pygame.Surface((self.originalWidth, self.originalHeight), pygame.SRCALPHA, 32)
            frameSurf.blit(img, (x, 0))
            self.images.append(frameSurf.copy())
            x -= self.originalWidth
        self.image = pygame.Surface.copy(self.images[0])

        self.currentImage = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 0
        self.scale = 1

    def addImage(self, filename):
        self.images.append(loadImage(filename))

    def move(self, xpos, ypos, centre=False):
        if centre:
            self.rect.center = [xpos, ypos]
        else:
            self.rect.topleft = [xpos, ypos]

    def changeImage(self, index):
        self.currentImage = index
        if self.angle == 0 and self.scale == 1:
            self.image = self.images[index]
        else:
            self.image = pygame.transform.rotozoom(self.images[self.currentImage], -self.angle, self.scale)
        oldcenter = self.rect.center
        self.rect = self.image.get_rect()
        originalRect = self.images[self.currentImage].get_rect()
        self.originalWidth = originalRect.width
        self.originalHeight = originalRect.height
        self.rect.center = oldcenter
        self.mask = pygame.mask.from_surface(self.image)
        if screenRefresh:
            updateDisplay()

# Variable Declaration
screenRefresh = True
spriteGroup = pygame.sprite.OrderedUpdates()
textboxGroup = pygame.sprite.OrderedUpdates()
gameClock = pygame.time.Clock()
musicPaused = False
hiddenSprites = pygame.sprite.OrderedUpdates()
screenRefresh = True
background = None
keydict = {"space": pygame.K_SPACE, "esc": pygame.K_ESCAPE, "up": pygame.K_UP, "down": pygame.K_DOWN,
           "left": pygame.K_LEFT, "right": pygame.K_RIGHT, "return": pygame.K_RETURN,
           "a": pygame.K_a,
           "b": pygame.K_b,
           "c": pygame.K_c,
           "d": pygame.K_d,
           "e": pygame.K_e,
           "f": pygame.K_f,
           "g": pygame.K_g,
           "h": pygame.K_h,
           "i": pygame.K_i,
           "j": pygame.K_j,
           "k": pygame.K_k,
           "l": pygame.K_l,
           "m": pygame.K_m,
           "n": pygame.K_n,
           "o": pygame.K_o,
           "p": pygame.K_p,
           "q": pygame.K_q,
           "r": pygame.K_r,
           "s": pygame.K_s,
           "t": pygame.K_t,
           "u": pygame.K_u,
           "v": pygame.K_v,
           "w": pygame.K_w,
           "x": pygame.K_x,
           "y": pygame.K_y,
           "z": pygame.K_z,
           "1": pygame.K_1,
           "2": pygame.K_2,
           "3": pygame.K_3,
           "4": pygame.K_4,
           "5": pygame.K_5,
           "6": pygame.K_6,
           "7": pygame.K_7,
           "8": pygame.K_8,
           "9": pygame.K_9,
           "0": pygame.K_0,
           "num0": pygame.K_KP0,
           "num1": pygame.K_KP1,
           "num2": pygame.K_KP2,
           "num3": pygame.K_KP3,
           "num4": pygame.K_KP4,
           "num5": pygame.K_KP5,
           "num6": pygame.K_KP6,
           "num7": pygame.K_KP7,
           "num8": pygame.K_KP8,
           "num9": pygame.K_KP9}
screen = ""


# Screen Functions
def updateDisplay():
    global background
    spriteRects = spriteGroup.draw(screen)
    textboxRects = textboxGroup.draw(screen)
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_ESCAPE]):
        pygame.quit()
        exit()
    spriteGroup.clear(screen, background.surface)
    textboxGroup.clear(screen, background.surface)

def screenSize(sizex, sizey, xpos=None, ypos=None, fullscreen=False):
    global screen
    global background
    if xpos != None and ypos != None:
        os.environ['SDL_VIDEO_WINDOW_POS'] = f"{xpos}, {ypos + 50}"
    else:
        windowInfo = pygame.display.Info()
        monitorWidth = windowInfo.current_w
        monitorHeight = windowInfo.current_h
        os.environ['SDL_VIDEO_WINDOW_POS'] = f"{(monitorWidth - sizex) // 2}, {(monitorHeight - sizey) // 2}"
    if fullscreen:
        screen = pygame.display.set_mode([sizex, sizey], pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode([sizex, sizey])
    background = Background()
    screen.fill(background.colour)
    pygame.display.set_caption("Graphics Window")
    background.surface = screen.copy()
    pygame.display.update()
    return screen

def setAutoUpdate(val):
    global screenRefresh
    screenRefresh = val

# Background Functions
def setBackgroundColour(colour):
    background.setColour(colour)
    if screenRefresh:
        updateDisplay()

def setBackgroundImage(img):
    global background
    background.setTiles(img)
    if screenRefresh:
        updateDisplay()

def scrollBackground(x, y):
    global background
    background.scroll(x, y)

# Sprite Functions
def makeSprite(filename, frames=1, altDims = None):
    thisSprite = newSprite(filename, frames, altDims)
    return thisSprite

def moveSprite(sprite, x, y, centre=False):
    """This function is responsible for defining the position of our sprite in the screen.

    Args:
        sprite ('newSprite' class object): currently imported from "images/links.gif"
        x (int): x axis position
        y (int): y axis position
        centre (bool, optional): Automatically centers the character onto the given position. Defaults to False.
    """
    sprite.move(x, y, centre)
    if screenRefresh:
        updateDisplay()

def showSprite(sprite):
    spriteGroup.add(sprite)
    if screenRefresh:
        updateDisplay()

def transformSprite(sprite, angle, scale, hflip=False, vflip=False):
    oldmiddle = sprite.rect.center
    if hflip or vflip:
        tempImage = pygame.transform.flip(sprite.images[sprite.currentImage], hflip, vflip)
    else:
        tempImage = sprite.images[sprite.currentImage]
    if angle != 0 or scale != 1:
        sprite.angle = angle
        sprite.scale = scale
        tempImage = pygame.transform.rotozoom(tempImage, -angle, scale)
    sprite.image = tempImage
    sprite.rect = sprite.image.get_rect()
    sprite.rect.center = oldmiddle
    sprite.mask = pygame.mask.from_surface(sprite.image)
    if screenRefresh:
        updateDisplay()

def changeSpriteImage(sprite, index):
    sprite.changeImage(index)

# Game Functions
def clock():
    current_time = pygame.time.get_ticks()
    return current_time

def keyPressed(keyCheck=""):
    global keydict
    keys = pygame.key.get_pressed()
    if sum(keys) > 0:
        if keyCheck == "" or keys[keydict[keyCheck.lower()]]:
            return True
    return False

def tick(fps):
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and event.key == keydict["esc"]) or event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    gameClock.tick(fps)
    return gameClock.get_fps()

def endWait():
    updateDisplay()
    print("Press ESC to quit")
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == keydict["esc"]):
                waiting = False
    pygame.quit()
    exit()

def loadImage(fileName, useColorKey=False):
    if os.path.isfile(fileName):
        image = pygame.image.load(fileName)
        image = image.convert_alpha()
        # Return the image
        return image
    else:
        raise Exception(f"Error loading image: {fileName} – Check filename and path?")

# Test
screenSize(1280,720)
setAutoUpdate(False)

setBackgroundImage( ["images/full_space.png"])


testSprite  = makeSprite("images/links.gif",32)  # links.gif contains 32 separate frames of animation. Sizes are automatically calculated.

moveSprite(testSprite,320,360,True)


showSprite(testSprite)

nextFrame = clock()
frame=0
while True:
    if clock() > nextFrame:                         # We only animate our character every 80ms.
        frame = (frame+1)%8                         # There are 8 frames of animation in each direction
        nextFrame += 80                             # so the modulus 8 allows it to loop

    if keyPressed("right"):
        changeSpriteImage(testSprite, 0*8+frame)    # 0*8 because right animations are the 0th set in the sprite sheet
        scrollBackground(-5,0)                      # The player is moving right, so we scroll the background left

    elif keyPressed("down"):
        changeSpriteImage(testSprite, 1*8+frame)    # down facing animations are the 1st set
        scrollBackground(0, -5)

    elif keyPressed("left"):
        changeSpriteImage(testSprite, 2*8+frame)    # and so on
        scrollBackground(5,0)

    elif keyPressed("up"):
        changeSpriteImage(testSprite,3*8+frame)
        scrollBackground(0,5)

    else:
        changeSpriteImage(testSprite, 1 * 8 + 5)  # the static facing front look

    updateDisplay()
    tick(120)

endWait()
