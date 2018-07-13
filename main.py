import pygame
from settings import *
from player import *

pygame.init()
vec = pygame.math.Vector2

#Game window
gameDisplay = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Aplatformer')

#Font init
myFont = pygame.font.SysFont('Comic Sans MS', 30)

#Text
xcolon = myFont.render('x: ', False, (white))
ycolon = myFont.render('y: ', False, (white))
acolon = myFont.render('a: ', False, (white))
vcolon = myFont.render('v: ', False, (white))

#Clock
clock = pygame.time.Clock()

def main():
    gameExit = False

    # Player initialization
    Player_1 = player(40, 40, yellow)
    Platform_1 = platform(0, screen_width - 40, yellow, screen_width, 40)

    # Gameloop
    while not gameExit:
       # Quit event
        for event in pygame.event.get():
            player.update_player(Player_1)
            if (event.type == pygame.QUIT):
                gameExit = True

            #Player movement
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_d):
                    Player_1.player_acc = PLAYER_ACC

                if (event.key == pygame.K_a):
                    Player_1.player_acc = -PLAYER_ACC

            #Player movement 2.0
            if (event.type == pygame.KEYUP):
                if (event.key == pygame.K_d):
                    Player_1.player_acc = 0

                if (event.key == pygame.K_a):
                    Player_1.player_acc = 0

        #Character and text rendering
        gameDisplay.fill(black)
        clock.tick(FPS)
        player.update_player(Player_1)
        platform.platform_update(Platform_1)

if( __name__ == "__main__"):
    main()








