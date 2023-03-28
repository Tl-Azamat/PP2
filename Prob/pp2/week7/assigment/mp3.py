import pygame
import sys
import os

pygame.init()
pygame.mixer.init() 

size = [400, 250]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("MP3 player")

Music = r'C:/Users/Саламат/Desktop/PP2/week7/music'
musicfiles = os.listdir(Music)
musicfiles = [os.path.join(Music,file) for file in musicfiles if file.endswith(".mp3")]

# print(musicfiles)
i = 0
pygame.mixer.music.load(musicfiles[i])

def music_play():
    pygame.mixer.music.play()
def music_stop():
    pygame.mixer.music.pause()
def next_music():
    global i
    i+=1
    if i >= len(musicfiles):
        i = 0
    pygame.mixer.music.load(musicfiles[i])
    pygame.mixer.music.play()
def prev_music():
    global i
    i-=1
    if i == 0:
        i == len(musicfiles)-1
    pygame.mixer.music.load(musicfiles[i])
    pygame.mixer_music.play()


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                music_play()
            elif event.key == pygame.K_RETURN:
                music_stop()
            elif event.key == pygame.K_LEFT:
                prev_music()
            elif event.key == pygame.K_RIGHT:
                next_music()
        if event.type == pygame.QUIT:
            print("EXIST")
            pygame.quit()
            sys.exit()
    screen.blit(screen,(0,0))
    pygame.display.update()
    pygame.display.flip()