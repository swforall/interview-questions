#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nayden
"""

from unittest import TestCase, main
from mars import Rover


class TaxesTest(TestCase):    
    def test_turn_left_1(self):
        '''Test that direction changes from N to E'''
        rover = Rover([5, 5], [1, 2, 'N'])
        self.assertEqual(rover.move('L'), '1 2 E')
        
    def test_turn_left_2(self):
        '''Test that direction changes from W to N'''
        rover = Rover([5, 5], [1, 2, 'W'])
        self.assertEqual(rover.move('L'), '1 2 N')
        
    def test_turn_left_3(self):
        '''Test that direction stays the same after 4 turns to the left'''
        rover = Rover([5, 5], [1, 2, 'W'])
        self.assertEqual(rover.move('L'*4), '1 2 W')
    
    def test_turn_right_1(self):
        '''Test that direction changes from N to W'''
        rover = Rover([5, 5], [1, 2, 'N'])
        self.assertEqual(rover.move('R'), '1 2 W')
        
    def test_turn_right_2(self):
        '''Test that direction changes from W to S'''
        rover = Rover([5, 5], [1, 2, 'W'])
        self.assertEqual(rover.move('R'), '1 2 S')
        
    def test_turn_right_4(self):
        '''Test that direction stays the same after 4 turns to the right'''
        rover = Rover([5, 5], [1, 2, 'W'])
        self.assertEqual(rover.move('R'*4), '1 2 W')
        
    def test_turn_move_w_1(self):
        '''Test that direction stays the same after and x is increased by 1 
        after a move west'''
        rover = Rover([5, 5], [1, 2, 'W'])
        self.assertEqual(rover.move('M'), '2 2 W')
        
    def test_turn_move_e_2(self):
        '''Test that direction stays the same after and x is decreased by 1 
        after a move east'''
        rover = Rover([5, 5], [1, 2, 'E'])
        self.assertEqual(rover.move('M'), '0 2 E')
        
    def test_turn_move_s_3(self):
        '''Test that direction stays the same after and y is decreased by 1 
        after a move south'''
        rover = Rover([5, 5], [1, 2, 'S'])
        self.assertEqual(rover.move('M'), '1 1 S')
        
    def test_turn_move_n_4(self):
        '''Test that direction stays the same after and y is increased by 1 
        after a move north'''
        rover = Rover([5, 5], [1, 2, 'N'])
        self.assertEqual(rover.move('M'), '1 3 N')
    
    def test_turn_move_limits_5(self):
        '''Test that direction and coordinates stays the same when
        rover has command to move outside limits'''
        rover = Rover([5, 5], [0, 0, 'E'])
        self.assertEqual(rover.move('M'), '0 0 E')
        
    def test_turn_move_limits_6(self):
        '''Test that direction and coordinates stays the same when
        rover has command to move outside limits'''
        rover = Rover([5, 5], [0, 0, 'S'])
        self.assertEqual(rover.move('M'), '0 0 S')
        
    def test_turn_move_limits_7(self):
        '''Test that direction and coordinates stays the same when
        rover has command to move outside limits'''
        rover = Rover([5, 5], [5, 5, 'W'])
        self.assertEqual(rover.move('M'), '5 5 W')
        
    def test_turn_move_limits_8(self):
        '''Test that direction and coordinates stays the same when
        rover has command to move outside limits'''
        rover = Rover([5, 5], [5, 5, 'N'])
        self.assertEqual(rover.move('M'), '5 5 N')
    
    def test_11(self):
        '''Test that direction and coordinates are what they should be after a 
        sequence of moves'''
        rover = Rover([5, 5], [1, 2, 'N'])
        self.assertEqual(rover.move('LMLMLMLMM'), '1 3 N')
    
    def test_12(self):
        '''Test that direction and coordinates are what they should be after a 
        sequence of moves'''
        rover = Rover([5, 5], [3, 3, 'E'])
        self.assertEqual(rover.move('MMRMMRMRRM'), '1 5 E')
    
if __name__ == '__main__':
    main()