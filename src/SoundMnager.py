import pygame

def sound():
    pygame.mixer.init()
    pygame.mixer.music.load("../sound/alarm.mp3")
    pygame.mixer.music.play()
    