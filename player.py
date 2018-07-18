from settings import *
import pygame

vec = pygame.math.Vector2
all_sprites = pygame.sprite.Group()
player_sprites = pygame.sprite.Group()
platform_sprites = pygame.sprite.Group()

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
        self.rect = self.image.get_rect()
        self.player_pos = vec(screen_width / 2, screen_height / 2)
        self.player_vel = vec(0, 0)
        self.player_acc = vec(0, PLAYER_GRAVITY)
        self.rect.x = self.player_pos.x
        self.rect.y = self.player_pos.y
        all_sprites.add(self)
        player_sprites.add(self)

    def handle(self, event):
        # Player movement
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_d):
                self.player_acc.x = PLAYER_ACC

            if (event.key == pygame.K_a):
                self.player_acc.x = -PLAYER_ACC

            if (event.key == pygame.K_w):
                self.jump()

        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_d):
                self.player_acc.x = 0

            if (event.key == pygame.K_a):
                self.player_acc.x = 0
    #todo: make it so that you can only jump on a platform
    
    def jump(self):
        self.player_vel.y = -10


    def update_player(self):
        # Gravity
        self.player_vel.y += self.player_acc.y
        self.player_pos.y += self.player_vel.y + self.player_acc.y * .5
        # Acceleration
        self.rect.x = self.player_pos.x
        self.rect.y = self.player_pos.y
        self.player_vel.x += self.player_acc.x
        self.player_pos.x += self.player_vel.x + self.player_acc.x * .5
        # Friction
        self.player_acc.x += (self.player_vel.x * -PLAYER_FRIC) / 1000
        if (self.player_vel.x > -.1) and (.1 > self.player_vel.x):
            self.player_acc.x = 0
            self.player_vel.x = 0
        elif(self.player_vel.x > 10) and (-10 > self.player_vel.x):
            self.player_vel.x = 10
            self.player_acc.x = 10


class Platform(pygame.sprite.Sprite):
    platform_width = screen_width
    platform_height = 40
    platform_color = red

    def __init__(self, platform_width, platform_height, platform_color,x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([platform_width, platform_height])
        self.image.fill(platform_color)
        self.rect = self.image.get_rect()
        self.platform_pos = vec(0, screen_height)
        all_sprites.add(self)
        platform_sprites.add(self)
        self.rect.x = x
        self.rect.y = y


