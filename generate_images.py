import matplotlib.pyplot as plt
import numpy as np
from level_1_pathfinding.grid_env import GridEnv
from level_1_pathfinding.pathfinding import a_star
from level_3_curriculum.parkour_env import ParkourEnv
import os

def save_pathfinding_image():
    env = GridEnv(width=20, height=20, obstacle_prob=0.1)
    start = (0, 0)
    goal = (19, 19)
    path = a_star(env, start, goal)

    grid = np.copy(env.grid)
    if path:
        for x, y in path:
            grid[x, y] = 0.5 # Path color

    plt.figure(figsize=(8, 8))
    plt.imshow(grid.T, cmap='Greys', origin='lower')
    plt.title("A* Pathfinding Visualization (Level 1)")
    plt.savefig("level_1_pathfinding/pathfinding_viz.png")
    print("Saved level_1_pathfinding/pathfinding_viz.png")

def save_parkour_image():
    env = ParkourEnv(difficulty=0.6)
    obs, info = env.reset()
    world = env.world

    plt.figure(figsize=(12, 2))
    plt.imshow([world], cmap='RdYlGn_r', aspect='auto')
    plt.title("Parkour Environment Visualization (Level 3 - Difficulty 0.6)")
    plt.xlabel("Position")
    plt.yticks([])
    plt.savefig("level_3_curriculum/parkour_viz.png")
    print("Saved level_3_curriculum/parkour_viz.png")

if __name__ == "__main__":
    save_pathfinding_image()
    save_parkour_image()
