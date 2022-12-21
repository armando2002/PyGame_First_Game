import pygame
import os

# sets window height and width constants
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# sets window title
pygame.display.set_caption("First Game")

# define screen background constant
WHITE = (255, 255, 255)
# define border color
BLACK = (0, 0, 0)
# set a border in the middle of the screen to keep ships apart (use known width and height)
BORDER = pygame.Rect(WIDTH/2 - 10, 0, 10, HEIGHT)

# define FPS constant
FPS = 60
# set velocity constant for ship movement
VEL = 5
# set spaceship height and width constants
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# import images for spaceships using OS library
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
# resize image to be smaller & rotate
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,
                                                                        (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,
                                                                     (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window(red, yellow):
    # give white background
    WIN.fill(WHITE)
    # draw middle black border on window (window, color, border)
    pygame.draw.rect(WIN, BLACK, BORDER)
    # draw images (use values from red and yellow rectangles from main())
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP_IMAGE, (red.x, red.y))
    pygame.display.update()


# controls yellow ship movement
def yellow_ship_movement(keys_pressed, yellow):
    # if key is pressed, do something (WASD for 1P and arrows for 2P) - inline comments apply to red ship as well
    # 1p left only allow movement to left border (0)
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
    # right only up to border in middle of screen (including width of ship to prevent crossing border)
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
        yellow.x += VEL
    # up only allow movement to top border (0)
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL
    # down only allow movement to right border
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT:
        yellow.y += VEL


def red_ship_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # 2p left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT:  # down
        red.y += VEL


def main():
    # define rectangles for spaceships
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    # controls speed of while loop at 60 FPS
    clock = pygame.time.Clock()
    run = True
    while run:
        # set FPS
        clock.tick(FPS)
        # check for events in pygame
        for event in pygame.event.get():
            # if user quits
            if event.type == pygame.QUIT:
                run = False
        # determine which keys are being pressed down
        keys_pressed = pygame.key.get_pressed()
        # use the ship movement functions to move
        yellow_ship_movement(keys_pressed, yellow)
        red_ship_movement(keys_pressed, red)
        # refresh the screen each loop & pass ship rectangles
        draw_window(red, yellow)

    # quit the game
    pygame.quit()


if __name__ == "__main__":
    main()
