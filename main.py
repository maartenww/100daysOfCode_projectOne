import pygame
from settings import *

pygame.init()
vec = pygame.math.Vector2

#Player Class
class player():
    player_width = 40
    player_height = 40

    player_color = (255,215,0)

    #Player Constructor
    def __init__(self,player_width,player_height,player_speed,player_color):
        self.player_width = player_width
        self.player_height = player_height
        self.player_pos = vec(screen_width/2,screen_height/2)
        self.player_color = player_color
        self.player_speed = 5
    #Draws player unto screen
    def draw_player(self,surface, player_pos):
        pygame.draw.rect(surface, self.player_color, (self.player_pos.x,self.player_pos.y, self.player_width,self.player_height))

def main():
    # Colors
    yellow = (255, 215, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)

    #FPS stuff
    clock = pygame.time.Clock()
    gameExit = False
    FPS = 50

    #Resolution and other position stuff
    moveX, moveY = 0, 0


    #Surface window
    gameDisplay = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Aplatformer')

    #Font and text rendering
    myFont = pygame.font.SysFont('Comic Sans MS', 30)
    xcolon = myFont.render('x: ', False, (white))
    ycolon = myFont.render('y: ', False, (white))

    #Player initialization
    Player_1 = player(40,40,5,yellow)

    print('Welcome to "Aplatformer"!')

    #Gameloop
    while not gameExit:

        #Quit event
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                gameExit = True

            #Player movement
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_d):
                    moveX = 5
                if (event.key == pygame.K_a):
                    moveX = -5

            #Player movement 2.o
            if (event.type == pygame.KEYUP):
                if (event.key == pygame.K_d):
                    moveX = 0
                if (event.key == pygame.K_a):
                    moveX = 0

            #Border collision
            if (Player_1.player_pos.x >= (screen_width - Player_1.player_width)):
                Player_1.player_pos.x = screen_width - Player_1.player_width
            elif (Player_1.player_pos.x <= 0):
                Player_1.player_pos.x = 0

        #Background color
        gameDisplay.fill(black)

        Player_1.player_pos.x += moveX


        #Character and text rendering
        Player_1.draw_player(gameDisplay,Player_1.player_pos)
        actual_x = myFont.render(str(Player_1.player_pos.x), False, (white))
        actual_y = myFont.render(str(Player_1.player_pos.y), False, (white))

        #More rendering
        gameDisplay.blit(xcolon, (0, 0))
        gameDisplay.blit(actual_x, (25, 0))
        gameDisplay.blit(ycolon, (0, 30))
        gameDisplay.blit(actual_y, (25, 30))

        #Fps
        clock.tick(FPS)

        #Update
        pygame.display.update()



if( __name__ == "__main__"):
    main()








