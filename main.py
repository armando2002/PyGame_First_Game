import pygame
import os

# sets height and width
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# sets window title
pygame.display.set_caption("First Game")

# define screen background
WHITE = (255, 255, 255)

# define FPS
FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# import images for spaceships using OS
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
# resize image to be smaller
YELLOW_SPACESHIP_IMAGE = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP_IMAGE = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))


def draw_window():
    # give white background
    WIN.fill(WHITE)
    # draw images
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (300, 100))
    pygame.display.update()


def main():
    # controls speed of while loop at 60 FPS
    clock = pygame.time.Clock()
    run = True
    while run:
        # check for events in pygame
        for event in pygame.event.get():
            # if user quits
            if event.type == pygame.QUIT:
                run = False
        # refresh the screen each loop
        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
