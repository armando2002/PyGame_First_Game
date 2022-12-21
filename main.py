import pygame
import os

# sets window height and width constants
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# sets window title
pygame.display.set_caption("First Game")

# define screen background constant
WHITE = (255, 255, 255)

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
    # draw images (use values from red and yellow rectangles from main())
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP_IMAGE, (red.x, red.y))
    pygame.display.update()


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
        # if key is pressed, do something (WASD for 1P and arrows for 2P)
        if keys_pressed[pygame.K_a]:  # left
            yellow.x -= VEL
        # refresh the screen each loop & pass ship rectangles
        draw_window(red, yellow)

    pygame.quit()


if __name__ == "__main__":
    main()
