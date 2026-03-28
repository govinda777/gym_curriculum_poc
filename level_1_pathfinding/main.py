import asyncio
import time
from level_1_pathfinding.grid_env import GridEnv
from level_1_pathfinding.pathfinding import a_star

class AsyncAgent:
    def __init__(self, name, env, start, goal):
        self.name = name
        self.env = env
        self.pos = start
        self.goal = goal
        self.path = []
        self.finished = False

    async def run(self):
        print(f"Agent {self.name} starting from {self.pos} to {self.goal}")

        start_time = time.time()
        self.path = a_star(self.env, self.pos, self.goal)
        end_time = time.time()

        if self.path is None:
            print(f"Agent {self.name} could not find a path to {self.goal}")
            return

        print(f"Agent {self.name} found path in {(end_time - start_time) * 1000:.2f}ms")

        for next_step in self.path[1:]:
            # Simulate real-time movement without blocking
            await asyncio.sleep(0.05) # "Movement time"
            self.pos = next_step
            # print(f"Agent {self.name} moved to {self.pos}")

        print(f"Agent {self.name} reached {self.goal}!")
        self.finished = True

async def main():
    # Setup grid environment
    env = GridEnv(width=30, height=30, obstacle_prob=0.1)

    # Create agents
    agent1 = AsyncAgent("Agent 1", env, (0, 0), (29, 29))
    agent2 = AsyncAgent("Agent 2", env, (0, 29), (29, 0))

    # Run agents concurrently
    await asyncio.gather(agent1.run(), agent2.run())

if __name__ == "__main__":
    asyncio.run(main())
