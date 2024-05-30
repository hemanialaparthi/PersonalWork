import pygame
from pygame.locals import *
import random

pygame.init()  # initialize the pygame class

# define a timer
clock = pygame.time.Clock()
fps = 60


# assign the variables screen_ width & screen_height to values
screen_width = 865
screen_height = 800

game_screen = pygame.display.set_mode((screen_width, screen_height))  # creates the blank game window
pygame.display.set_caption("Welcome to Flappy Bird - New Mod")  # adds caption to the game

# add the game variables

ground_scroll = 0
scroll_speed = 4

# load images
background = pygame.image.load('images/background.png')
base = pygame.image.load('images/base3.png')
bird = pygame.image.load('images/bird.png')
pipe = pygame.image.load('images/pipe.png')
powerup = pygame.image.load('images/powerup.png')

run_game = True
while run_game:

    clock.tick(fps)

    game_screen.blit(background, (0, 0))
    game_screen.blit(base, (ground_scroll, 7))
    ground_scroll -= scroll_speed  # decrease the ground scroll by scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0

    for event in pygame.event.get():  # gets all events that are happening
        if event.type == pygame.QUIT:  # if clicked on X/ quit
            run_game = False  # set the run_game to False

    pygame.display.update()  # updates everything that has been added

pygame.quit()  # quit the game