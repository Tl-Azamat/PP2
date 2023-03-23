import pygame
pygame.init()
screen = pygame.display.set_mode((600,300)) #Расширение экрана
pygame.display.set_caption("Pygame itProger Game")

icon = pygame.image.load('C:/Users/Azamat2005/Desktop/Python/Prob/pp2/week7/images/mega.png') #Иконик
pygame.display.set_icon(icon)

square = pygame.Surface((50,170)) #размер объекта
square.fill('Red') #цвет объекта



running = True
while running:
    screen.blit(square,(10,0))


    pygame.display.update() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

       

