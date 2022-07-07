#Abrir e reproduzir um arquivo MP3
import pygame

pygame.init()
pygame.mixer.music.load('df21.mp3')
pygame.mixer.music.play()
pygame.event.wait()