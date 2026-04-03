import gymnasium as gym
import pygame
from agents.base import BaseAgent
from core.telemetry import SimulationTelemetry
from visuals.renderer import DashboardRenderer

class CartPoleSimulation:
    """Orchestrates Agent, Environment and Rendering (Dependency Inversion Principle)."""
    def __init__(self, agent: BaseAgent, render_mode="human", target_seconds=None):
        self.agent = agent
        self.render_mode = render_mode
        self.target_seconds = target_seconds
        
        # Use rgb_array for human mode to allow custom dashboard blitting
        self.env_render = "rgb_array" if render_mode == "human" else render_mode
        self.env = gym.make("CartPole-v1", render_mode=self.env_render)
        self.telemetry = SimulationTelemetry()
        
        self.screen = None
        self.renderer = None
        self.clock = None
        
        if render_mode == "human":
            pygame.init()
            self.renderer = DashboardRenderer()
            self.screen = pygame.display.set_mode((self.renderer.width, self.renderer.height))
            pygame.display.set_caption("Neural Web Tester - SOLID Dashboard")
            self.clock = pygame.time.Clock()

    def run(self, episodes=1, max_steps=1000):
        """Main loop managing episodes."""
        episode_count = 0
        try:
            while episodes == -1 or episode_count < episodes:
                episode_count += 1
                if self._run_episode(max_steps):
                    break
        except KeyboardInterrupt:
            print("\n🛑 Simulation interrupted by user.")
        finally:
            self.env.close()
            if self.render_mode == "human":
                pygame.quit()

    def _run_episode(self, max_steps):
        obs, _ = self.env.reset()
        self.telemetry.reset_episode()
        
        for step in range(max_steps):
            if self.render_mode == "human":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return True
            
            action = self.agent.act(obs)
            
            if self.render_mode == "human":
                frame = self.env.render()
                self.renderer.render(self.screen, frame, self.telemetry, action)
                pygame.display.flip()
                self.clock.tick(60)

            obs, _, term, trunc, _ = self.env.step(action)
            self.telemetry.update(obs)
            
            # CLI quick report
            print(f"\r🤖 Episode: {self.telemetry.episode} | Step: {self.telemetry.steps}      ", end="", flush=True)
            
            if term or trunc:
                print(f"\n🏁 Finished Episode {self.telemetry.episode} after {self.telemetry.steps} steps.")
                if self.target_seconds and self.telemetry.steps >= self.target_seconds * 50:
                    print(f"✅ GOAL REACHED: Stable for {self.target_seconds}s!")
                    return True
                break
        return False
