
from circular_queue import CircularQueue

#Data structure for pathfinding

class PathFinding:
    '''Path finding class
    Get graph and path'''
    def __init__(self, game):
        self.game = game
        self.map = game.map.mini_map
        self.ways = [-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1], [1, 1], [-1, 1] # a list of tuples representing  possible directions to move (up, down, left, right, diagonal)
        self.graph = {} # a dictionary to store the graph representation of the map
        self.get_graph()

    def get_path(self, start, goal):
        '''Get path from start to goal
        Return path'''

        self.visited = self.bfs(start, goal, self.graph)
        path = [goal]
        step = self.visited.get(goal, start)

        while step and step != start:
            path.append(step)
            step = self.visited[step]
        return path[-1]

    def bfs(self, start, goal, graph):
        '''Breadth-first search
        Return visited nodes'''

        queue = CircularQueue(1000)  # Initialize CircularQueue with a capacity of 1000
        queue.enqueue(start)
        visited = {start: None}

        while not queue.is_empty():
            current = queue.dequeue()
            if current == goal:
                break
            for direction in self.ways:
                next_node = (current[0] + direction[0], current[1] + direction[1])
                if next_node in graph and next_node not in visited:
                    queue.enqueue(next_node)
                    visited[next_node] = current
        return visited

    def get_next_nodes(self, x, y):
        '''Get next nodes
        Return next nodes'''

        valid_moves = []
        for dx, dy in self.ways:
            new_pos = (x + dx, y + dy)
            if new_pos not in self.game.map.world_map:
                valid_moves.append(new_pos)
        return valid_moves

    def get_graph(self):
        '''Create graph from map'''
        for y, row in enumerate(self.map):
            for x, value in enumerate(row):
                if value != 1:  # Assuming 1 represents a wall
                    self.graph[(x, y)] = []
                    for dx, dy in self.ways:
                        next_x, next_y = x + dx, y + dy
                        if 0 <= next_x < len(row) and 0 <= next_y < len(self.map) and self.map[next_y][next_x] != 1:
                            self.graph[(x, y)].append((next_x, next_y))