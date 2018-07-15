from player import *
import pygame
from settings import *

pygame.init()
vec = pygame.math.Vector2
myFont = pygame.font.SysFont('Comic Sans MS', 30)
gameDisplay = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Aplatformer')
clock = pygame.time.Clock()

class Game:

    def __init__(self):
        pass
    def load_text(self, player_1):
        # Text
        self.actual_x = myFont.render(str(int(player_1.player_pos.x)), False, (white))
        self.actual_y = myFont.render(str(int(player_1.player_pos.y)), False, (white))
        self.actual_a = myFont.render(str(int(player_1.player_acc)), False, (white))
        self.actual_v = myFont.render(str(int(player_1.player_vel)), False, (white))
        self.xcolon = myFont.render('x: ', False, (white))
        self.ycolon = myFont.render('y: ', False, (white))
        self.acolon = myFont.render('a: ', False, (white))
        self.vcolon = myFont.render('v: ', False, (white))

    def update_game(self, player_1):

        gameDisplay.fill(black)
        clock.tick(FPS)
        gameDisplay.blit(self.xcolon, (0, 0))
        gameDisplay.blit(self.actual_x, (25, 0))
        gameDisplay.blit(self.ycolon, (0, 30))
        gameDisplay.blit(self.actual_y, (25, 30))
        gameDisplay.blit(self.acolon, (0, 60))
        gameDisplay.blit(self.actual_a, (25, 60))
        gameDisplay.blit(self.vcolon, (0, 90))
        gameDisplay.blit(self.actual_v, (25, 90))
        Player.update_player(player_1)
        pygame.display.update()

g = Game()
Player_1 = Player(40, 40, yellow)

def main():
    gameExit = False

    # Gameloop
    while not gameExit:
       # Quit event
        for event in pygame.event.get():
            Player.update_player(Player_1)
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
        g.load_text(Player_1)
        g.update_game(Player_1)

if( __name__ == "__main__"):
    main()




