from main import *
from settings import *
import pygame

vec = pygame.math.Vector2

# Player Class
class player():
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

    def update_player(self):
        #Draw player
        pygame.draw.rect(gameDisplay, self.player_color,
                         (self.player_pos.x, self.player_pos.y, self.player_width,
                          self.player_height))

        # Border collision
        if (self.player_pos.x > (screen_width - self.player_width)):
            self.player_pos.x = screen_width - self.player_width
        elif (self.player_pos.x < 0):
            self.player_pos.x = 0

        #Acceleration
        self.player_vel += self.player_acc
        self.player_pos.x += self.player_vel + self.player_acc * .5
        #Friction
        self.player_acc += (self.player_vel * -PLAYER_FRIC) / 500
        if (self.player_vel > -.1) and (.1 > self.player_vel):
            self.player_acc = 0
            self.player_vel = 0

        # Font and text rendering
        actual_x = myFont.render(str(int(self.player_pos.x)), False, (white))
        actual_y = myFont.render(str(int(self.player_pos.y)), False, (white))
        actual_a = myFont.render(str(float(self.player_acc)), False, (white))
        actual_v = myFont.render(str(float(self.player_vel)), False, (white))

        #More rendering
        gameDisplay.blit(xcolon, (0, 0))
        gameDisplay.blit(actual_x, (25, 0))
        gameDisplay.blit(ycolon, (0, 30))
        gameDisplay.blit(actual_y, (25, 30))
        gameDisplay.blit(acolon, (0,60))
        gameDisplay.blit(actual_a, (25, 60))
        gameDisplay.blit(vcolon, (0,90))
        gameDisplay.blit(actual_v, (25, 90))

        #Updat screen
        pygame.display.update()

class platform():
    platform_color = yellow
    #Constructor
    def __init__(self, x, y, color, width, height):
        self.platform_width = width
        self.platform_height = height
        self.platform_color = color
        self.plat_pos = vec(0, 0)
        self.plat_pos.x = x
        self.plat_pos.y = y

    def platform_update(self):
        pygame.draw.rect(gameDisplay, self.platform_color,
                         (self.plat_pos.x, self.plat_pos.y, self.platform_width,
                          self.platform_height))
        pygame.display.update()

