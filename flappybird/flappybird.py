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

# title of the game and game_screen display
game_screen = pygame.display.set_mode((screen_width, screen_height))  # creates the blank game window
pygame.display.set_caption("Welcome to Flappy Bird - New Mod")  # adds caption to the game

# add game variables

ground_scroll = 0
scroll_speed = 4
game_over = False
bird_flying = False
pipe_spacing = 150
pipe_frequency = 1500  # ms
last_pipe = pygame.time.get_ticks() - pipe_frequency  # subtracted w pipe_frequency so pipes get created as soon as game starts
score = 0
pass_pipe = False
game_started = False
powerup_frequency = 10000  # powerup appears every 5000 ms
last_powerup = pygame.time.get_ticks() - powerup_frequency

# load images
background = pygame.image.load('images/background.png')
base = pygame.image.load('images/base3.png')
restart = pygame.image.load('images/restart.png')
start = pygame.image.load('images/startbutton.png')

# define a font
font = pygame.font.SysFont('fredokaone', 40)
# color
yellow = (255, 255, 0)


# reset game
def reset_game():
    global score, bird_flying, game_started, ground_scroll, last_pipe, pass_pipe
    pipe_group.empty()  # empty the pipes
    flappy_bird.rect.x = 100
    flappy_bird.rect.y = int(screen_height / 2)
    flappy_bird.velocity = 0
    flappy_bird.clicked = False
    score = 0
    bird_flying = False
    game_started = False
    ground_scroll = 0
    last_pipe = pygame.time.get_ticks() - pipe_frequency
    pass_pipe = False


# score text
def text_to_image(text, font, text_col, x, y):
    """Converts a text to an image"""
    image = font.render(text, True, text_col)
    game_screen.blit(image, (x, y))


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
            if game_over is False:
                if (pygame.mouse.get_pressed()[0] == 1 or pygame.key.get_pressed()[pygame.K_SPACE]) and not self.clicked:
                    self.velocity = -8
                    self.clicked = True
                if pygame.mouse.get_pressed()[0] == 0 and not pygame.key.get_pressed()[pygame.K_SPACE]:
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


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, pos):
        pygame.sprite.Sprite.__init__(self)  # inherit the class
        self.image = pygame.image.load('images/pipe.png')
        self.rect = self.image.get_rect()
        if pos == 1:  # if pos is 1 it is from top, -1 would be bottom
            self.image = pygame.transform.flip(self.image, False, True)  # true means will be flipped on y axis
            self.rect.bottomleft = [x, y - int(pipe_spacing / 2)]
        if pos == -1:
            self.rect.topleft = [x, y + int(pipe_spacing / 2)]

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/powerup.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()


class Button():
    def __init__(self, x, y, image):
        self.image = image  # store picture
        self.rect = self.image.get_rect()  # create a rectangle from it
        self.rect.topright = (x, y)

    def draw_button(self):
        """ Draws the button """

        # mouse position
        position = pygame.mouse.get_pos()

        # check if mouse clicks the button:
        mouse_clicked = False
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1:
                mouse_clicked = True

        game_screen.blit(self.image, (self.rect.x, self.rect.y))

        return mouse_clicked


# groups & instances
bird_group = pygame.sprite.Group()  # keeps track of all the sprites added
pipe_group = pygame.sprite.Group()
powerup_group = pygame.sprite.Group()

flappy_bird = Bird(100, int(screen_height / 2))
bird_group.add(flappy_bird)

button = Button((screen_width // 2) + 50, screen_height // 2, restart)  # creates an instance for button
startbutton = Button((screen_width // 2) + 50, (screen_height // 2), start)

# main run

run_game = True
while run_game:

    clock.tick(fps)
    game_screen.blit(background, (0, 0))
    bird_group.draw(game_screen)
    bird_group.update()
    pipe_group.draw(game_screen)
    powerup_group.draw(game_screen)

    # ground being drawn
    game_screen.blit(base, (ground_scroll, 710))

    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and \
                bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right and not pass_pipe:
            pass_pipe = True

        if pass_pipe:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                pass_pipe = False

    # score added:
    text_to_image(f"SCORE: {score}", font, yellow, 10, 10)

    # check if collision w pipe occurs
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy_bird.rect.top <= 0:
        game_over = True

    # bird hits the ground:
    if flappy_bird.rect.bottom >= 710:
        game_over = True
        bird_flying = False

    if game_over is False and bird_flying is True:
        time_now = pygame.time.get_ticks()  # gets the current time
        if (time_now - last_pipe) > pipe_frequency:
            pipe_height = random.randint(-100, 100)
            bottom_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)  # screen width used to create just off the screen
            top_pipe = Pipe(screen_width, int((screen_height) / 2) + pipe_height, 1)
            pipe_group.add(bottom_pipe)  # add to group so it can be shown or else will only be an instance
            pipe_group.add(top_pipe)
            last_pipe = time_now

            # check if enough time has gone by before powerup has been addedc
            if (time_now - last_powerup) > powerup_frequency:
                powerup_x = screen_width
                powerup_y = int(screen_height / 2) + pipe_height
                powerup = PowerUp(powerup_x, powerup_y)
                powerup_group.add(powerup)
                last_powerup = time_now

        ground_scroll -= scroll_speed  # decrease the ground scroll by scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0

        pipe_group.update()
        powerup_group.update()

    if pygame.sprite.spritecollide(flappy_bird, powerup_group, True):
        score += 2

    # restart the game
    if game_over is True:
        if button.draw_button() is True:
            reset_game()
            game_over = False
    elif not game_started:
        if startbutton.draw_button() is True:
            game_started = True
            bird_flying = True

    for event in pygame.event.get():  # gets all events that are happening
        if event.type == pygame.QUIT:  # if clicked on X/ quit
            run_game = False  # set the run_game to False
        if event.type == pygame.MOUSEBUTTONDOWN and game_started and not game_over:
            bird_flying = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_started and not game_over:
                bird_flying = True
                flappy_bird.velocity = -8  # jump force when the spacebar is clicked

    pygame.display.update()  # updates everything that has been added

pygame.quit()  # quit the game
