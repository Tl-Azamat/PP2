import pygame
pygame.init()
W, H = 800, 800
x = W//2
y = H//2    
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((W, H))
sc.fill(WHITE)
mickey = pygame.image.load("C:/Users/Azamat2005/Desktop/jjjj/main-clock.png")
leftHand = pygame.image.load("C:/Users/Azamat2005/Desktop/jjjj/left-hand.png")
rightHand = pygame.image.load("C:/Users/Azamat2005/Desktop/jjjj/right-hand.png")
mickeyRect = mickey.get_rect()
sc.blit(mickey, (x, y))
sc.blit(mickey, mickeyRect)
def blitRotateCenter(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = center).center)
    surf.blit(rotated_image, new_rect)
langle = 0
rangle = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    langle -= 0.05
    rangle -= 0.000833
    
    blitRotateCenter(sc, leftHand, (x,y), langle) 
    blitRotateCenter(sc, rightHand, (x,y), rangle)
    pygame.display.update()