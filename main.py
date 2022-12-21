# NEED to do:
# 1. Refactor into cleaner code with separate .py files for various related functions
# 2. Add custom ship sprites

import pygame
import os

# set fonts for  score
pygame.font.init()
# adds sounds
pygame.mixer.init()

# sets window height and width constants
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# sets window title
pygame.display.set_caption("First Game")

# define screen background constant
WHITE = (255, 255, 255)
# define border color
BLACK = (0, 0, 0)
# set red color
RED = (255, 0, 0)
# set yellow color
YELLOW = (255, 255, 0)
# set a border in the middle of the screen to keep ships apart (use known width and height)
BORDER = pygame.Rect(WIDTH // 2 - 10, 0, 10, HEIGHT)
# bullet hit sound effect
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
# bullet fire sound
BULLET_FIRE_SOUND= pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))

# set health font
HEALTH_FONT = pygame.font.SysFont('Arial', 40)
# set winner font
WINNER_FONT = pygame.font.SysFont('Arial', 100)

# define FPS constant
FPS = 60
# set velocity constant for ship movement
VEL = 5
# set velocity constant for bullets
BULLET_VEL = 7
# set max # of bullets on screen (3)
MAX_BULLETS = 2
# set spaceship height and width constants
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# add unique event for each bullet collision
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# import images for spaceships using OS library
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
# resize image to be smaller & rotate
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,
                                                                        (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
# same for red
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,
                                                                     (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
# load background and make same width height as window
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))


# function for drawing background, ships, bullets
def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    # give space background
    WIN.blit(SPACE, (0, 0))
    # draw middle black border on window (window, color, border)
    pygame.draw.rect(WIN, BLACK, BORDER)
    # show health (1 = anti-aliasing) with white color
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    # get width of red text and subtract from top left of screen, add 10 px padding and put 10 px down from top
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    # put yellow health 10 px from left of window (0)
    WIN.blit(yellow_health_text, (10, 10))
    # draw images (use values from red and yellow rectangles from main())
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP_IMAGE, (red.x, red.y))

    # draw red bullet
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    # draw yellow bullet
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    # update the screen
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


# controls red ship movement
def red_ship_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # 2p left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT:  # down
        red.y += VEL


# move the bullets, handle collision, and remove bullets
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        # move the yellow bullet left
        bullet.x += BULLET_VEL
        # if ship collides with bullet
        if red.colliderect(bullet):
            # cause RED_HIT event when yellow bullet hits red ship
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        # if yellow bullet reaches end of screen, remove
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        # move the red bullet right
        bullet.x -= BULLET_VEL
        # if ship collides with bullet
        if yellow.colliderect(bullet):
            # cause YELLOW_HIT event when red bullet hits yellow ship
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        # if red bullet reaches end of screen, remove
        elif bullet.x < 0:
            red_bullets.remove(bullet)


# draw winning text and put it in the middle of the screen, use integer division to avoid float errors
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH // 2 - draw_text.get_width() // 2, HEIGHT // 2 - draw_text.get_height() // 2))
    pygame.display.update()
    # show (pause game) for 5 seconds to show screen
    pygame.time.delay(5000)


def main():
    # define rectangles for spaceships
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    # define bullets
    red_bullets = []
    yellow_bullets = []

    # set health of ships
    red_health = 10
    yellow_health = 10

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
                # quit the game
                pygame.quit()
                exit()
            # if key is pressed down
            if event.type == pygame.KEYDOWN:
                # if Left Control is pressed, also check for max bullets on screen
                if event.key == pygame.K_LCTRL and len(yellow_bullets) <= MAX_BULLETS:
                    # make a rectangle for the bullet (add width to spawn in middle), use integer division
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                # if Right Control is pressed
                if event.key == pygame.K_RCTRL and len(red_bullets) <= MAX_BULLETS:
                    # spawn bullet at left position (x default since spawn is upper left)
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)
            # if red hit, remove health
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
            # if yellow hit, remove health
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
        # set winning text and show if health is 0
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow wins!"
        if yellow_health <= 0:
            winner_text = "Red wins!"
        # once winner text appears (winning player), show text and break loop
        if winner_text != "":
            draw_winner(winner_text)
            break

        # determine which keys are being pressed down
        keys_pressed = pygame.key.get_pressed()
        # use the ship movement functions to move
        yellow_ship_movement(keys_pressed, yellow)
        red_ship_movement(keys_pressed, red)
        # deal with the bullets
        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        # refresh the screen each loop & pass ship rectangles & bullets
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    main()


if __name__ == "__main__":
    main()
