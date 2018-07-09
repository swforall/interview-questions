#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nayden
"""

class Rover:
    moves = {
    'M':    {
            0: [0, 1, 0],
            1: [-1, 0, 0],
            2: [0, -1, 0],
            3: [1, 0, 0]
            },
    
    'L':    {
            0: [0, 0, 1],
            1: [0, 0, 1],
            2: [0, 0, 1],
            3: [0, 0, 1]
            },
    
    'R':    {
            0: [0, 0, -1],
            1: [0, 0, -1],
            2: [0, 0, -1],
            3: [0, 0, -1]
            }}
    
    directions = {'N': 0, 'E': 1, 'S': 2, 'W': 3,
                  0: 'N', 1: 'E', 2: 'S', 3: 'W'}
    
    def __init__(self, grid_shape, pos):
        self._grid_shape = grid_shape
        self._pos = pos
        self._pos[-1] = self.directions[self._pos[-1]]
        
    def move(self, commands):
        for cmd in commands:
            self._update_pos(cmd)
        ret_str = '{} {} {}'.format(self._pos[0], self._pos[1], self.directions[self._pos[2]])
        return ret_str
    
    def _update_pos(self, cmd):
        m = self.moves[cmd][self._pos[-1]]
        for i in range(len(self._pos)):
            self._pos[i] += m[i]
        for i in range(len(self._pos)-1):
            if self._pos[i] < 0:
               self._pos[i] = 0
            if self._pos[i] > self._grid_shape[i]:
               self._pos[i] = self._grid_shape[i]
        self._pos[-1] = self._pos[-1] % 4