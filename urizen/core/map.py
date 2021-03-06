#!/usr/bin/python3

from urizen.core.cell import Cell


class Map(object):
    """
    Map class

    Attributes:
    w -- Map width
    h -- Map height
    cells -- Cell matrix
    fill_symbol -- Symbol to fill initial cell matrix
    tags -- Map tags
    """

    def __init__(self, w, h, fill_symbol = '.', tags=[]):
        self.w = w
        self.h = h
        self.tags = tags
        self.cells = [[Cell(x, y, symbol=fill_symbol) for x in range(w)] for y in range(h)]
    
    def get_size(self):
        return self.w, self.h