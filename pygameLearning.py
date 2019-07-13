##Nathan Hinton
##Simple pygame program:

import pygame

pygame.init()
displayWidth = 800
displayHeight = 600
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Pygame Learning')

#Vars:
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

carWidth = 73

clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')
crashed = False

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def mainLoop():
    x = (displayWidth * 0.45)
    y = (displayHeight *0.8)
    xChange = 0
    
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            ############################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xChange = -5
                elif event.key == pygame.K_RIGHT:
                    xChange = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xChange = 0
        x += xChange

        gameDisplay.fill(white)
        car(x, y)
        
        if x > displayWidth-carWidth or x < 0:
            crashed = True
        
        pygame.display.update()
        clock.tick(60)
pygame.quit()
