#! /usr/bin/env python3
# -*- coding: utf-8 -*-


class Rectangle():

    def __init__(self, width, heigth):
        if width == heigth:
            self.size = width
        else:
            self.width = width
            self.heigth = heigth
