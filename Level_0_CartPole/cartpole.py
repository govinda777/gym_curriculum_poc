import argparse
import gymnasium as gym
from agents.random_agent import RandomAgent
from core.simulation import CartPoleSimulation

def main():
    parser = argparse.ArgumentParser(description="Neural Web Tester - CartPole Entry Point")
    parser.add_argument("--episodes", type=int, default=1, help="Number of episodes (-1 for infinite)")
    parser.add_argument("--steps", type=int, default=1000, help="Max steps per episode")
    parser.add_argument("--render", type=str, default="human", choices=["human", "rgb_array", "None"], help="Render mode")
    parser.add_argument("--stable", type=float, default=None, help="Target stability in seconds")
    
    args = parser.parse_args()
    
    # 1. Setup Agent
    # Note: We create a temporary env just to get the action space
    temp_env = gym.make("CartPole-v1")
    agent = RandomAgent(temp_env.action_space)
    temp_env.close()
    
    # 2. Setup and Run Simulation
    render_mode = None if args.render == "None" else args.render
    
    simulation = CartPoleSimulation(
        agent=agent,
        render_mode=render_mode,
        target_seconds=args.stable
    )
    
    simulation.run(episodes=args.episodes, max_steps=args.steps)

if __name__ == "__main__":
    main()
