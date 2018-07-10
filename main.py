import pygame

pygame.init()

def main():
    global flag
    print('Welcome to "Aplatformer"!')

if( __name__ == "__main__"):
    main()

screen_width = 800
screen_height = 600
gameDisplay = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Aplatformer')

pygame.display.update()

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            gameExit = True



