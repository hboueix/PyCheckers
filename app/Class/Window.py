#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame


class Window():

    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def open(self):
        return pygame.display.set_mode([self.width, self.heigth])
