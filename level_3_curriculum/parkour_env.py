import gymnasium as gym
from gymnasium import spaces
import numpy as np

class ParkourEnv(gym.Env):
    """
    Custom 1D Parkour Environment with adjustable difficulty.
    The agent must reach the goal while avoiding gaps.
    Difficulty controls the number and width of gaps.
    """
    def __init__(self, difficulty=0.1):
        super(ParkourEnv, self).__init__()
        self.max_length = 50
        self.difficulty = difficulty

        # Action: 0 (Stay), 1 (Move Left), 2 (Move Right), 3 (Jump)
        self.action_space = spaces.Discrete(4)

        # Observation: Agent position (1D) and local view (next 5 cells)
        self.observation_space = spaces.Box(low=0, high=1, shape=(6,), dtype=np.float32)

        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.agent_pos = 0
        self.steps = 0

        # Generate world: 0 (floor), 1 (gap)
        self.world = np.zeros(self.max_length)
        num_gaps = int(self.difficulty * 10)
        gap_indices = np.random.choice(range(5, self.max_length - 5), size=num_gaps, replace=False)
        for idx in gap_indices:
            gap_width = 1 + int(self.difficulty * 2)
            self.world[idx:idx+gap_width] = 1

        # Ensure start and end are safe
        self.world[0] = 0
        self.world[self.max_length-1] = 0

        return self._get_obs(), {}

    def _get_obs(self):
        # Normalize position and get local view
        norm_pos = self.agent_pos / self.max_length
        local_view = []
        for i in range(1, 6):
            look_ahead = self.agent_pos + i
            if look_ahead < self.max_length:
                local_view.append(self.world[look_ahead])
            else:
                local_view.append(0) # Boundary

        return np.array([norm_pos] + local_view, dtype=np.float32)

    def step(self, action):
        self.steps += 1
        reward = -0.1 # Step penalty
        terminated = False
        truncated = False

        prev_pos = self.agent_pos

        if action == 1: # Move Left
            self.agent_pos = max(0, self.agent_pos - 1)
        elif action == 2: # Move Right
            self.agent_pos = min(self.max_length - 1, self.agent_pos + 1)
        elif action == 3: # Jump
            # A jump moves the agent 2 steps ahead
            self.agent_pos = min(self.max_length - 1, self.agent_pos + 2)
            reward -= 0.1 # Jumping costs more

        # Check if fell into a gap
        if self.world[self.agent_pos] == 1:
            reward = -10
            terminated = True
        elif self.agent_pos == self.max_length - 1:
            reward = 100
            terminated = True
        elif self.agent_pos > prev_pos:
            reward += 1 # Progression reward
        elif self.agent_pos == prev_pos and action != 0:
            reward -= 0.5 # Penalty for trying to move out of bounds or failing to move

        if self.steps >= 200:
            truncated = True

        return self._get_obs(), reward, terminated, truncated, {}

    def render(self):
        env_str = ["_"] * self.max_length
        for i, val in enumerate(self.world):
            if val == 1:
                env_str[i] = " " # Gap
        env_str[self.agent_pos] = "A"
        # print("".join(env_str) + " | Goal")
        return "".join(env_str)
