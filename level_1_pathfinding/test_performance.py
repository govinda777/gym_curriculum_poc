import time
import numpy as np
from level_1_pathfinding.grid_env import GridEnv
from level_1_pathfinding.pathfinding import a_star

def test_pathfinding_performance():
    # Large environment to test scalability and performance
    width, height = 50, 50
    env = GridEnv(width=width, height=height, obstacle_prob=0.1)

    start = (0, 0)
    goal = (49, 49)

    # Ensure start and goal are not obstacles for the test
    env.grid[start[0], start[1]] = 0
    env.grid[goal[0], goal[1]] = 0

    print(f"Testing A* performance on {width}x{height} grid...")

    start_time = time.time()
    path = a_star(env, start, goal)
    end_time = time.time()

    execution_time_ms = (end_time - start_time) * 1000

    if path:
        print(f"Path found with length {len(path)}.")
        print(f"Execution time: {execution_time_ms:.2f}ms")

        # Verify no obstacles in the path
        for pos in path:
            assert env.grid[pos[0], pos[1]] == 0, f"Path contains an obstacle at {pos}"

        # Verify path is continuous
        for i in range(len(path) - 1):
            d = abs(path[i+1][0] - path[i][0]) + abs(path[i+1][1] - path[i][1])
            assert d == 1, f"Path is not continuous between {path[i]} and {path[i+1]}"

        print("Path validity check passed.")
    else:
        print("No path found (this can happen due to obstacles).")

    # KPI Check: Execution time < 100ms
    assert execution_time_ms < 100, f"Performance KPI failed: {execution_time_ms:.2f}ms >= 100ms"
    print("Performance KPI check passed (< 100ms).")

if __name__ == "__main__":
    test_pathfinding_performance()
