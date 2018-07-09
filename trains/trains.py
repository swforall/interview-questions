#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nayden
"""

from math import inf

class TrainTracks:
    def __init__(self, routes):
        self._graph = self._build_graph(routes)
        
    def get_distance_along_path(self, path):
        '''Calculate distance along a path in the graph.'''
        
        dist = 0
        start = path[0]
        for node in path[1:]:
            try:
                dist += self._graph[start][node]
                start = node
            except KeyError:
                return 'NO SUCH ROUTE'
        return dist
    
    def get_trips_number_stops(self, start, end, num_stops):
        '''Calculate number of trips of length num_stops from start to end'''
        
        all_trips = {start}
        
        for i in range(num_stops):
            new_trips = set()
            for tr in all_trips:
                for k in self._graph[tr[-1]].keys():
                    new_tr = tr + k
                    new_trips.add(new_tr)
            all_trips = new_trips
            
        num_trips = 0
        
        for trip in all_trips:
            if end == trip[-1]:
                num_trips += 1
        return num_trips
    
    def get_shortest_path(self, start, end):
        '''Get shortest path from start to end nodes'''
        
        # add dummy_start in case start == end
        self._graph['dummy_start'] = self._graph[start]
        distances = {k: inf for k in self._graph.keys()}
        distances['dummy_start'] = 0
        visited = set()
        while len(visited) < len(self._graph):
            cur_node = get_min_elem_from_dict(distances)
            if cur_node == end:
                break
            for node in self._graph[cur_node].keys():
                try:
                    if cur_node not in visited and \
                    self._graph[cur_node][node] + distances[cur_node] < distances[node]:
                           distances[node] = self._graph[cur_node][node] + \
                                               distances[cur_node]
                except KeyError:
                    pass
            distances.pop(cur_node)
            visited.add(cur_node)
        self._graph.pop('dummy_start')
        return distances[cur_node]
    
    def get_trips_number_distance(self, start, end, dist):
        '''Get number of trips of length less than dist'''
        
        # all_trips - a container for all paths in the graph from the starting node
        # of length less than dist, the paths will have the node count equal to
        # the depth we have reached
        all_trips = {start: 0}
        valid_trips = {}
        
        # later if there are no paths with length less than dist, all_trips will
        # be empty
        while len(all_trips) > 0:
            new_trips = {}
            for tr in all_trips:
                # construct new paths with all connected nodes
                if all_trips[tr] < dist:
                    # take into consideration only those with dist smaller than what we want
                    for k in self._graph[tr[-1]]:
                        new_tr = tr + k
                        new_trips[new_tr] = all_trips[tr] + self._graph[tr[-1]][k]
                        if k == end and new_trips[new_tr] < dist:
                            valid_trips[new_tr] = new_trips[new_tr]
            # update the pahs container with the new paths
            all_trips = new_trips
        
        return len(valid_trips)
    
    def _build_graph(self, routes):
        '''Build the graph of train tracks. If a route is input two times,
        the last occurence will be valid.'''
        
        gr = {}
        for route in routes:
            try:
                gr[route[0]][route[1]] = int(route[2])
            except KeyError:
                gr[route[0]] = {}
                gr[route[0]][route[1]] = int(route[2])
        return gr
     
def get_min_elem_from_dict(d):
    minel = inf
    minel_key = ''
    for elem in d:
        if d[elem] < minel:
            minel = d[elem]
            minel_key = elem
    return minel_key
            