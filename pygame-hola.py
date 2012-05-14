#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys 
import pygame
from pygame.locals import *
 
if not pygame.font: print 'estilos y letras desactivadas!'
if not pygame.mixer: print 'sonidos desactivados!'

WIDTH = 640
HEIGHT = 480

def main():

        window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("¡Hola pyGame!")
        while True:
                for eventos in pygame.event.get():
                        if eventos.type == QUIT:
                                sys.exit(0)
        return 0

if __name__ == '__main__':
        pygame.init()
        main()