import pygame

# sets height and width
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# sets window title
pygame.display.set_caption("First Game")

WHITE = (255, 255, 255)


def main():
    run = True
    while run:
        # check for events in pygame
        for event in pygame.event.get():
            # if user quits
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(WHITE)
        # give white background
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
