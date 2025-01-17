import pygame as pg

_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _,_, _, _, _, _, 1],
    [1, _, _, 3, 3, 3, 3, _, _, _, _,2, 2, 2, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _,_, _, 2, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _,_, _, 2, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _,_, _, 2, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _,_, _, 2, _, _, 1],
    [1, _, _, 3, 3, 3, 3, _, _, _, _,_, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _,_, _, _, _, _, 1],
    [1, _, _, _, 4, _, _, _, 4, _, _,_, _, _, _, _, 1],
    [1, _, _, _, 4, _, _, _, 4, _, _,_, _, _, _, _, 1],
    [1, 1, 1, 3, 1, 3, 1, 1, 1, 3, _,_, _, 3, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, _,_, _, 3, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, _,_, _, 3, 1, 1, 1],
    [1, 1, 3, 1, 1, 1, 1, 1, 1, 3, _,_, _, 3, 1, 1, 1],
    [1, 4, _, _, _, _, _, _, _, _, _,_, _, _, _, _, 1],
    [3, _, _, _, _, _, _, _, _, _, _,_, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _,_, _, _, _, _, 1],
    [1, _, _, 2, _, _, _, _, _, 3, 4, _,_, 4, 3, _, 1],
    [1, _, _, 5, _, _, _, _, _, _, 3, _,_, 3, _, _, 1],
    [1, _, _, 5, _, _, _, _, _, _, 3, _,_, 3, _, _, 1],
    [1, _, _, 2, _, _, _, _, _, _, _, _, _,_, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _,_, _, _, 1],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _,_, _, 1],
    [1, 4, _, _, _, _, _, _, 4, _, _, 4, _, _,_, _, 1],
    [1, 4, _, _, _, _, _, _, 4, _, _, 4, _, _,_, _, 1],
    [1, 1, 3, 3, _, _,_, 3, 3, 1, 3, 3, 1, 3, 1, 1, 1],
    [1, 1, 1, 3, _, _,_, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 3, 4, _, _,_, 4, 3, 3, 3, 3, 3, 3, 3, 3, 1],
    [1, 1, 1, 3, _, _, 3,3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [3, _, _, _, _, _, _, _,_, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _,_, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _,_, _, _, _, _, _, _, 3],
    [3, _, _, 5, _, _, _, _, 5, _, _, _, 5, _, _, _, 3],
    [3, _, _, 5, _, _, _, _, 5, _, _, _, 5, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [1, 1, 1, 3, _, _, _, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, 3, 3, 3, 3, 3, 3,3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]


class Map:
    def __init__(self, game):
        self.game = game 
        self.mini_map = mini_map
        self.world_map = {} # Create a dictionary
        self.rows = len(self.mini_map) # rows in the mini map
        self.cols = len(self.mini_map[0]) # columns in the mini map
        self.get_map() 


    def get_map(self):
        y = 0
        for row in self.mini_map: 
            x = 0 
            for value in row: 
                if value: # If not _ in the mini map
                    self.world_map[(x, y)] = value # Add the position and value to the world map e.g (0, 0): 1, (1, 0): 1, etc.
                x += 1 
            y += 1 


    def draw(self):
        for pos in self.world_map:
            # Draw each rectangle on the screen
            x, y = pos[0] * 100, pos[1] * 100  # Calculate the top-left corner
            width, height = 100, 100  # Rectangle dimensions
            pg.draw.rect(self.game.screen, 'darkgrey', (x, y, width, height), 5)
