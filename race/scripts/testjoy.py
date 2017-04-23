import pygame
import sys
import time
from pygame.locals import *


if __name__ == '__main__':
    pygame.joystick.init()
    print pygame.joystick.get_count()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    buttonStatus = ["False" for x in range(8)]
    buttonStatus.append('0')

    buttons = [x for x in range(0,9)]

    buttonName = ['key1','key2','key3','key4','l1','r1','l2','r2','lstick']

    buttonMap = dict(zip(buttons,buttonName))

    buttonMsg = dict(zip(buttonName,buttonStatus))
    buttonMsg['lstick'] = '0'

    pygame.init()
    done = False
    diff = 0.5
    move = ''
    prev = ''
    while not done:
        if move!=prev:
            print move
            prev = move
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.JOYBUTTONDOWN:
                move = event.button

