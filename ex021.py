""" Exercício para tocar um arquivo mp3 """

import pygame
pygame.init()
pygame.mixer.music.load('')
pygame.mixer.music.play()
pygame.event.wait()