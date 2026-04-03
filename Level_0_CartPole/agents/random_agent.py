from agents.base import BaseAgent

class RandomAgent(BaseAgent):
    """Simple agent that takes random actions."""
    def __init__(self, action_space):
        self.action_space = action_space
        
    def act(self, observation) -> int:
        return self.action_space.sample()
