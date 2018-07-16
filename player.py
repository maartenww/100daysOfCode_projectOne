from settings import *
import pygame

vec = pygame.math.Vector2
all_sprites = pygame.sprite.Group()

# Player Class
class Player(pygame.sprite.Sprite):
    player_width = 40
    player_height = 40
    player_color = (255, 215, 0)

    # Player Constructor
    def __init__(self, player_width, player_height, player_color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([player_width, player_height])
        self.image.fill(player_color)
        self.player_height = player_height
        self.rect = self.image.get_rect()
        # todo: Make y start in middle of screen
        self.player_pos = vec(0, screen_height / 2)
        self.player_color = player_color
        self.player_vel = 0
        self.player_acc = 0
        all_sprites.add(self)

    def handle(self, event):
        # Player movement
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_d):
                self.player_acc = PLAYER_ACC

            if (event.key == pygame.K_a):
                self.player_acc = -PLAYER_ACC

        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_d):
                self.player_acc = 0

            if (event.key == pygame.K_a):
                self.player_acc = 0

    def update_player(self):
        # Draw player
        #pygame.draw.rect(gameDisplay, self.player_color,
                         #(self.player_pos.x, self.player_pos.y, self.player_width,
                          #self.player_height))

        # Border collision
        #if (self.player_pos.x > (screen_width - self.player_width)):
            #self.player_pos.x = screen_width - self.player_width
        #elif (self.player_pos.x < 0):
            #self.player_pos.x = 0

        # Acceleration
        self.player_pos = self.rect
        self.player_vel += self.player_acc
        self.player_pos.x += self.player_vel + self.player_acc * .5
        # Friction
        self.player_acc += (self.player_vel * -PLAYER_FRIC) / 1000
        if (self.player_vel > -.1) and (.1 > self.player_vel):
            self.player_acc = 0
            self.player_vel = 0
        elif(self.player_vel > 15) and (-15 > self.player_vel):
            self.player_vel = 15
            self.player_acc = 15
