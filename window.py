import pygame
from constants import NATIVE_SCREEN_SIZE


pygame.init()
screen = pygame.Surface(NATIVE_SCREEN_SIZE) # Native drawing context
window = pygame.display.set_mode((960, 720)) # Actual display window
pygame.display.set_caption("Touhou Flower Reflecting Mound ~ Phantasmagoria of Flower View v1.50a")
pygame.display.set_icon(
    pygame.image.load("./images/1.ico")
)