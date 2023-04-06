import pygame, time
import random
pygame.init()
width = 800
height = 600

#the screen(Площадь)
screen = pygame.display.set_mode((width, height))

#load the image 
carimg = pygame.image.load("C:/Users/Azamat2005/Desktop/Python/Prob/pp2/week8/assigment/racer/racerimages/Player.png")

#width of the car
car_width = 44

#load all the images
grass = pygame.image.load("C:/Users/Azamat2005/Desktop/Python/Prob/pp2/week8/assigment/racer/racerimages/grass.jpg")
yellow_strip = pygame.image.load("C:/Users/Azamat2005/Desktop/Python/Prob/pp2/week8/assigment/racer/racerimages/yellow_strip.jpg")
strip = pygame.image.load("C:/Users/Azamat2005/Desktop/Python/Prob/pp2/week8/assigment/racer/racerimages/strip.jpg")

#crashed message
MyFont = pygame.font.SysFont("None", 100)
render_text  = MyFont.render("CAR CRASHED", 0 , (255,255,255) )

#for the caption(Имена)
pygame.display.set_caption("RACER")

#function for the obstiacle
def obstacle(obs_x, obs_y, obs):
    if obs == 0:
        obs_pic = pygame.image.load("C:/Users/Azamat2005/Desktop/Python/Prob/pp2/week8/assigment/racer/racerimages/1.png")
    if obs == 1:
        obs_pic = pygame.image.load("C:/Users/Azamat2005/Desktop/Python/Prob/pp2/week8/assigment/racer/racerimages/2.png")
    if obs == 2:
        obs_pic = pygame.image.load("C:/Users/Azamat2005/Desktop/Python/Prob/pp2/week8/assigment/racer/racerimages/3.png")
    if obs == 3:
        obs_pic = pygame.image.load("C:/Users/Azamat2005/Desktop/Python/Prob/pp2/week8/assigment/racer/racerimages/4.png")
    if obs == 4:
        obs_pic = pygame.image.load("C:/Users/Azamat2005/Desktop/Python/Prob/pp2/week8/assigment/racer/racerimages/5.png")
    if obs == 5:
        obs_pic = pygame.image.load("C:/Users/Azamat2005/Desktop/Python/Prob/pp2/week8/assigment/racer/racerimages/6.png")
    screen.blit(obs_pic, (obs_x, obs_y))
    


#function for adding the backround image
def backround():
    screen.blit(grass,(0,0))
    screen.blit(grass,(700,0))
    screen.blit(yellow_strip,(375,0))
    screen.blit(yellow_strip,(375,100))
    screen.blit(yellow_strip,(375,200))
    screen.blit(yellow_strip,(375,300))
    screen.blit(yellow_strip,(375,400))
    screen.blit(yellow_strip,(375,500))
    screen.blit(yellow_strip,(375,600))
    screen.blit(strip, (120,0))
    screen.blit(strip, (680,0))


#image appearing 
def car(x,y):
    screen.blit(carimg,(x,y))#start coordinade 

#for the backround color(фон)
screen.fill((119,119,119))

#time module
clock = pygame.time.Clock() #Типа фпс

def game_loop():
    bump = True
    x_change = 0
    x = 400
    y = 500
    obstacle_speed = 10
    obs = 0
    y_change = 0
    obs_x = random.randrange(200,650)
    obs_y = -750
    enemy_width = 56
    enemy_height = 125
    
    #game cycle
    while bump:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bump  = False
        
        #moving in x,y coordinates
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP: #для ожидания
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        
        x += x_change
        

        #for the backround color (фон)
        screen.fill((119,119,119))
        backround()
        obs_y -= (obstacle_speed / 4)
        obstacle(obs_x,obs_y,obs)
        obs_y += obstacle_speed

        #calling car function
        car(x,y)
        if x > 680 - car_width or x < 110:
            screen.blit(render_text, (80,200))
            pygame.display.update()
            time.sleep(5)
            game_loop()

        if obs_y > height:
            obs_y = 0 - enemy_height
            obs_x = random.randrange(170, width - 170)
            obs = random.randrange(0,6)
        
        if y < obs_y + enemy_height:
            if x > obs_x and x < obs_x + enemy_width or x + car_width > obs_x and x + car_width < obs_x + enemy_width: 
                screen.blit(render_text, (100,200))
                pygame.display.uptate()
                time.sleep(2)
                game_loop()
            #right side
            #if x > obs_x or x + car_width > obs_x:
                    
            #left side
            #if x < obs_x or x + car_width < obs_x + enemy_width:


        #update the game
        pygame.display.update()
        clock.tick(100)


game_loop()
pygame.quit()
quit()



