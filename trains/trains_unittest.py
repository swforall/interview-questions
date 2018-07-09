#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nayden
"""

from unittest import TestCase, main
from trains import TrainTracks

class TrainTest(TestCase):
    def setUp(self):
        '''Create train tracks graph'''
        self.routes_input = 'AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7'.split(', ')
        self.exp_graph = {
                'A': {'B': 5, 'D': 5, 'E': 7},
                'B': {'C': 4},
                'C': {'D': 8, 'E': 2},
                'D': {'C': 8, 'E': 6},
                'E': {'B': 3}
                }
        self.tr = TrainTracks(self.routes_input)
        
    def test_graph_creation(self):
        '''Test the graph is as expected'''
        self.assertEqual(self.tr._graph, self.exp_graph)
        
    def test_dist_path_1(self):
        '''Test correct distance is returned for a path'''
        path = 'A-B-C'.split('-')
        self.assertEqual(self.tr.get_distance_along_path(path), 9)
    
    def test_dist_path_2(self):
        '''Test correct distance is returned for a path'''
        path = 'A-D'.split('-')
        self.assertEqual(self.tr.get_distance_along_path(path), 5)
        
    def test_dist_path_3(self):
        '''Test correct distance is returned for a path'''
        path = 'A-D-C'.split('-')
        self.assertEqual(self.tr.get_distance_along_path(path), 13)
        
    def test_dist_path_4(self):
        '''Test correct distance is returned for a path'''
        path = 'A-E-B-C-D'.split('-')
        self.assertEqual(self.tr.get_distance_along_path(path), 22)
        
    def test_dist_path_5(self):
        '''Test 'NO SUCH ROUTE' is returned for an invalid path'''
        path = 'A-E-D'.split('-')
        self.assertEqual(self.tr.get_distance_along_path(path), 'NO SUCH ROUTE')
    
    def test_trips_num_1(self):
        '''Test correct number of trips is returned for a path that starts
        and ends in the same node'''
        self.assertEqual(self.tr.get_trips_number_stops('C', 'C', 4), 2)
    
    def test_trips_num_2(self):
        '''Test correct number of trips is returned for paths from a given
        source to destination'''
        self.assertEqual(self.tr.get_trips_number_stops('A', 'C', 4), 3)
        
    def test_shortest_path_1(self):
        '''Test correct shorted distance is returned between two nodes'''
        self.assertEqual(self.tr.get_shortest_path('A', 'C'), 9)
    
    def test_shortest_path_2(self):
        '''Test correct shorted distance is returned between two nodes'''
        self.assertEqual(self.tr.get_shortest_path('B', 'B'), 9)
        
    def test_number_of_trips_1(self):
        '''Test correct number of trips under a certain length between two 
        nodes is returned'''
        self.assertEqual(self.tr.get_trips_number_distance('C', 'C', 30), 7)
        
    def test_number_of_trips_2(self):
        '''Test correct number of trips under a certain length between two 
        nodes is returned'''
        self.assertEqual(self.tr.get_trips_number_distance('A', 'C', 20), 5)
        
    def test_number_of_trips_3(self):
        '''Test correct number of trips under a certain length between two 
        nodes is returned. If no route from start to end, return 0'''
        self.assertEqual(self.tr.get_trips_number_distance('C', 'A', 20), 0)
    
if __name__ == '__main__':
    main()