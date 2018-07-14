from main import *
from settings import *
import pygame

vec = pygame.math.Vector2


# Player Class
class Player:
    player_width = 40
    player_height = 40
    player_color = (255, 215, 0)

    # Player Constructor
    def __init__(self, player_width, player_height, player_color):
        self.player_width = player_width
        self.player_height = player_height
        self.player_pos = vec(0, screen_height / 2)
        self.player_color = player_color
        self.player_vel = 0
        self.player_acc = 0

    # def move_player(self):
    # for event in pygame.event.get():
    # Player movement
    # if (event.type == pygame.KEYDOWN):
    # if (event.key == pygame.K_d):
    # Player_1.player_acc = PLAYER_ACC

    # if (event.key == pygame.K_a):
    # Player_1.player_acc = -PLAYER_ACC

    # Player movement 2.0
    # if (event.type == pygame.KEYUP):
    # if (event.key == pygame.K_d):
    # Player_1.player_acc = 0

    # if (event.key == pygame.K_a):
    # Player_1.player_acc = 0
    def update_player(self):
        # Draw player
        pygame.draw.rect(gameDisplay, self.player_color,
                         (self.player_pos.x, self.player_pos.y, self.player_width,
                          self.player_height))

        # Border collision
        if (self.player_pos.x > (screen_width - self.player_width)):
            self.player_pos.x = screen_width - self.player_width
        elif (self.player_pos.x < 0):
            self.player_pos.x = 0

        # Acceleration
        self.player_vel += self.player_acc
        self.player_pos.x += self.player_vel + self.player_acc * .5
        # Friction
        self.player_acc += (self.player_vel * -PLAYER_FRIC) / 500
        if (self.player_vel > -.1) and (.1 > self.player_vel):
            self.player_acc = 0
            self.player_vel = 0
