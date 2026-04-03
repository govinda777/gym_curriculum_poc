from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """Abstract base class for all agents (DIP, LSP)."""
    @abstractmethod
    def act(self, observation) -> int:
        pass
