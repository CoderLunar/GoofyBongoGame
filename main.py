import pygame
import os

ICON = pygame.image.load(os.path.join('Assets', 'bongo.png'))
BACKGROUND = pygame.image.load(os.path.join('Assets', 'desert.jpeg'))
BACKGROUND_SIZE = pygame.transform.scale(BACKGROUND, (900, 700))
FIRST_BONGO = pygame.image.load(os.path.join('Assets', 'bogno2.png'))
FIRST_BONGO_SIZE = pygame.transform.scale(FIRST_BONGO, (200, 200))
SECOND_BONGO = pygame.image.load(os.path.join('Assets', 'bongo3.png'))
SECOND_BONGO_SIZE = pygame.transform.scale(SECOND_BONGO, (200, 250))
W_LUNAR = pygame.image.load(os.path.join('Assets', 'w lunar.png'))

WHITE = (255, 255, 255)

FPS = 60

WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Goofy Fan Game")
pygame.display.set_icon(ICON)

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND_SIZE, (0, 0))
    WIN.blit(FIRST_BONGO_SIZE, (0, 0))
    WIN.blit(SECOND_BONGO_SIZE, (700, 0))
    WIN.blit(W_LUNAR, (300, 250))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()
