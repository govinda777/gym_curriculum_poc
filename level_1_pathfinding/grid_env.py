import numpy as np

class GridEnv:
    def __init__(self, width=20, height=20, obstacle_prob=0.2):
        self.width = width
        self.height = height
        self.grid = np.zeros((width, height))
        self.obstacles = []

        # Randomly place obstacles
        for x in range(width):
            for y in range(height):
                if np.random.rand() < obstacle_prob:
                    self.grid[x, y] = 1 # Obstacle
                    self.obstacles.append((x, y))

    def is_obstacle(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[x, y] == 1
        return True

    def get_neighbors(self, x, y):
        neighbors = []
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height and not self.is_obstacle(nx, ny):
                neighbors.append((nx, ny))
        return neighbors
