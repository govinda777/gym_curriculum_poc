import time
import numpy as np

class SimulationTelemetry:
    """Manages simulation state and history (SRP)."""
    def __init__(self, max_history=100):
        self.max_history = max_history
        self.angle_history = []
        self.pos_history = []
        self.high_score = 0
        self.start_time = time.time()
        self.steps = 0
        self.episode = 0

    def reset_episode(self):
        self.steps = 0
        self.start_time = time.time()
        self.episode += 1

    def update(self, observation):
        self.steps += 1
        pos, _, angle, _ = observation
        # Store as degrees for easier visualization
        self.angle_history.append(np.degrees(angle))
        self.pos_history.append(pos)
        
        if self.steps > self.high_score:
            self.high_score = self.steps
            
        if len(self.angle_history) > self.max_history:
            self.angle_history.pop(0)
            self.pos_history.pop(0)
