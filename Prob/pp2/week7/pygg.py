import pygame
pygame.init()
screen = pygame.display.set_mode((600,300)) #Расширение экрана
pygame.display.set_caption("Pygame itProger Game")

icon = pygame.image.load('C:/Users/Azamat2005/Desktop/Python/Prob/pp2/week7/images/mega.png') #Иконик
pygame.display.set_icon(icon)



running = True
while running:
    #screen.fill((114,157,124)) #цвета фона


    pygame.display.update() #Экранный коньсоль

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: #изменение цвета фона 
                screen.fill((70,44,133))
            if event.key == pygame.K_b:
                screen.fill((186, 37, 181)) #изменение цвета фона

