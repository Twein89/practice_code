from enum import Enum

class State(Enum):
    unvisited = 0
    visiting = 1
    visited = 2

class node(object):
    def __init__(self, key):
        self.key = key
        self.incoming_edges = 0

