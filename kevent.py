import pygame 
import sys
from pygame.locals import*

pygame.init()

WIDTH,HEIGHT =800,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("KeyBoard Events Demo")

WHITE = (255,255,255)
RED = (255,0,0)
BLUE= (0,0,255)