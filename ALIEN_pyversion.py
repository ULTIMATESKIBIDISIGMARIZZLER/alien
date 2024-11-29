import pygame
from random import randint

# Initialize pygame
pygame.init()

# Game Window Setup
WIDTH, HEIGHT = 1250, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shoot the aliens")

# Load the alien image
alien_img = pygame.image.load("Lesson 7/images/alien.png")
alien_rect = alien_img.get_rect()
alien_rect.topleft = (randint(0, WIDTH - alien_rect.width), randint(0, HEIGHT - alien_rect.height))

# Colors and Font
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 40)


# Message Variable
message = ""

# Function to reposition the alien
def place_alien():
    alien_rect.topleft = (randint(0, WIDTH - alien_rect.width), randint(0, HEIGHT - alien_rect.height))

space = pygame.transform.scale(pygame.image.load("Lesson 7/images/space.png"),(WIDTH,HEIGHT))

def draw():
    screen.blit(space,(0,0))

running = True
while running:
    screen.fill(WHITE)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if alien_rect.collidepoint(event.pos):
                message = "Good shot!"
                place_alien()
            else:
                message = "You missed!"

    # Draw the alien and message
    screen.blit(alien_img, alien_rect)
    screen.blit(font.render(message, True, BLACK), (600, 30))

    pygame.display.flip()  # Update screen

pygame.quit()
