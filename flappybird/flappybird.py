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
game_over = False
bird_flying = False

# load images
background = pygame.image.load('images/background.png')
base = pygame.image.load('images/base3.png')
bird = pygame.image.load('images/bird1.png')
pipe = pygame.image.load('images/pipe.png')
powerup = pygame.image.load('images/powerup.png')


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)  # inherit the class
        self.images = []
        self.index = 0
        self.counter = 0
        for number in range(1, 4):
            image = pygame.image.load(f'images/bird{number}.png')
            self.images.append(image)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()  # prints a rectangle from the boundaries of the image
        self.rect.center = [x, y]  # pos
        self.velocity = 0
        self.clicked = False

    def update(self):

        if bird_flying is True:
            # add gravity of the bird
            self.velocity += 0.5
            if self.velocity > 8:
                self.velocity = 8
            if self.rect.bottom < 710:
                self.rect.y += int(self.velocity)  # add to the y coord of the bird
            # add the jump function of the bird
            if game_over == False:
                if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                    self.velocity = -10
                    self.clicked = True
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False

                # handle the animation
                self.counter += 1  # increase the counter by 1
                birdflap_cooldown = 5

                if self.counter > birdflap_cooldown:
                    self.counter = 0  # reset the counter
                    self.index += 1
                    if self.index >= len(self.images):
                        self.index = 0
                    self.image = self.images[self.index]

                # bird rotation
                self.image = pygame.transform.rotate(self.images[self.index], (self.velocity * -1))
            else:
                self.image = pygame.transform.rotate(self.images[self.index], -90)
        



bird_group = pygame.sprite.Group()  # keeps track of all the sprites added

flappy_bird = Bird(100, int(screen_height/2))
bird_group.add(flappy_bird)

run_game = True
while run_game:

    clock.tick(fps)

    game_screen.blit(background, (0, 0))

    bird_group.draw(game_screen)
    bird_group.update()

    # ground being drawn
    game_screen.blit(base, (ground_scroll, 710))

    # bird hits the ground:
    if flappy_bird.rect.bottom > 710:
        game_over = True
        flying = False

    if game_over == False:
        ground_scroll -= scroll_speed  # decrease the ground scroll by scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0

    for event in pygame.event.get():  # gets all events that are happening
        if event.type == pygame.QUIT:  # if clicked on X/ quit
            run_game = False  # set the run_game to False
        if event.type == pygame.MOUSEBUTTONDOWN and bird_flying == False and game_over == False:
            bird_flying = True

    pygame.display.update()  # updates everything that has been added

pygame.quit()  # quit the game